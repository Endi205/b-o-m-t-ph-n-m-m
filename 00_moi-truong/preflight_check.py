# -*- coding: utf-8 -*-
"""Kiểm tra môi trường trước buổi thực hành học phần 04211 Bảo mật sinh trắc.

Chương trình chỉ dùng thư viện chuẩn của Python để tự chạy được cả khi thiếu gói; mỗi gói được
nhập thử trong một tiến trình con riêng, nên một gói hỏng (ví dụ lỗi DLL của TensorFlow trên
Windows) không làm dừng toàn bộ phép kiểm tra. Không cần mạng, không tải trọng số mô hình.

Cách chạy (trong môi trường ảo của học phần):
    python preflight_check.py            kiểm tra đầy đủ; lần chạy đầu tiên sau khi cài có thể
                                         mất 2 đến 3 phút vì TensorFlow và PyTorch nhập lần đầu rất
                                         chậm, các lần sau khoảng 20 đến 30 giây
    python preflight_check.py --nhanh    bỏ qua bước nhập thử TensorFlow, PyTorch, DeepFace
Kết quả in ra màn hình và ghi vào tệp preflight-bao-cao.txt ở thư mục hiện hành.
Báo cáo không chứa tên người dùng, tên máy hay đường dẫn thư mục cá nhân.

Mức độ của từng dòng:
- [LỖI]: thiếu hoặc hỏng một thành phần của môi trường chung (Python, gói thư viện, OpenCV).
- [CẢNH BÁO]: cần xử lý trước bài thực hành được nêu trong dòng đó, nhưng không chặn các bài
  khác; ví dụ tệp trọng số DeepFace thiếu hoặc hỏng chỉ ảnh hưởng TH04 trở đi.
Dòng "Sẵn sàng cho TH01" ở cuối báo cáo chỉ xét các thành phần TH01 cần: Python 3.12, numpy,
scipy, matplotlib, setuptools và pyeer, phép tính numpy và phép vẽ hình.
"""
import argparse
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

HERE = Path(__file__).resolve().parent
EXPECTED_PYTHON = (3, 12)

# tên gói trên PyPI -> tên mô-đun khi import, và mức độ: "bat_buoc" hoặc "nang" (nhập chậm)
PACKAGES = {
    "numpy": ("numpy", "bat_buoc"),
    "scipy": ("scipy", "bat_buoc"),
    "pandas": ("pandas", "bat_buoc"),
    "matplotlib": ("matplotlib", "bat_buoc"),
    "scikit-learn": ("sklearn", "bat_buoc"),
    "scikit-image": ("skimage", "bat_buoc"),
    "pillow": ("PIL", "bat_buoc"),
    "opencv-python": ("cv2", "bat_buoc"),
    "setuptools": ("pkg_resources", "bat_buoc"),
    "pyeer": ("pyeer.eer_info", "bat_buoc"),
    "fingerprint_enhancer": ("fingerprint_enhancer", "bat_buoc"),
    "fingerprint-feature-extractor": ("fingerprint_feature_extractor", "bat_buoc"),
    "lightphe": ("lightphe", "bat_buoc"),
    "lightdsa": ("lightdsa", "bat_buoc"),
    "tenseal": ("tenseal", "bat_buoc"),
    "bchlib": ("bchlib", "bat_buoc"),
    "galois": ("galois", "bat_buoc"),
    "soundfile": ("soundfile", "bat_buoc"),
    "huggingface_hub": ("huggingface_hub", "bat_buoc"),
    "tensorflow": ("tensorflow", "nang"),
    "tf-keras": ("tf_keras", "nang"),
    "torch": ("torch", "nang"),
    "torchaudio": ("torchaudio", "nang"),
    "speechbrain": ("speechbrain", "nang"),
    "deepface": ("deepface.DeepFace", "nang"),
}


# Các mục mà TH01 thực sự cần; một [LỖI] ở mục khác không chặn TH01.
TH01_ITEMS = {"Phiên bản Python", "numpy", "scipy", "matplotlib", "setuptools", "pyeer",
              "Phép tính numpy (nghịch đảo ma trận 200 x 200)", "Phép tính numpy",
              "Vẽ hình có chữ tiếng Việt (matplotlib Agg)", "Vẽ hình (matplotlib)"}

# Tệp trọng số DeepFace và bài thực hành cần đến tệp đó (theo DEEPFACE_MODELS của download_weights.py).
WEIGHT_LABS = {
    "facenet512_weights.h5": "TH04, TH05, TH09, TH10",
    "arcface_weights.h5": "TH04",
    "retinaface.h5": "TH04",
    "face_recognition_sface_2021dec.onnx": "TH04",
    "2.7_80x80_MiniFASNetV2.pth": "TH08, TH10",
    "4_0_0_80x80_MiniFASNetV1SE.pth": "TH08, TH10",
}


class Report:
    def __init__(self):
        self.lines, self.n_ok, self.n_warn, self.n_fail = [], 0, 0, 0
        self.failed_items = []

    def add(self, status, item, detail=""):
        mark = {"OK": "[ĐẠT]     ", "WARN": "[CẢNH BÁO]", "FAIL": "[LỖI]     ", "INFO": "[THÔNG TIN]"}[status]
        if status == "OK":
            self.n_ok += 1
        elif status == "WARN":
            self.n_warn += 1
        elif status == "FAIL":
            self.n_fail += 1
            self.failed_items.append(item)
        line = f"{mark} {item}" + (f": {detail}" if detail else "")
        self.lines.append(line)
        print(line, flush=True)


def anonymize(text):
    """Thay đường dẫn thư mục cá nhân bằng dấu ~ để báo cáo không lộ tên người dùng."""
    home = str(Path.home())
    return text.replace(home, "~") if home and home != "/" else text


def installed_version(dist):
    try:
        from importlib.metadata import PackageNotFoundError, version
    except ImportError:
        return None
    try:
        return version(dist)
    except PackageNotFoundError:
        return None


def marker_applies(marker):
    """Đánh giá điều kiện nền tảng trong requirements.txt; ưu tiên thư viện packaging."""
    marker = marker.strip()
    if not marker:
        return True
    try:
        from packaging.markers import Marker
        return Marker(marker).evaluate()
    except Exception:
        env = {"sys_platform": sys.platform, "platform_machine": platform.machine()}
        expr = marker
        for k, v in env.items():
            expr = re.sub(rf"\b{k}\b", repr(v), expr)
        if not re.fullmatch(r"[\s'\"\w.!=()-]+", expr.replace(" and ", " ").replace(" or ", " ")):
            return True
        try:
            return bool(eval(expr, {"__builtins__": {}}, {}))
        except Exception:
            return True


def pinned_versions():
    req = HERE / "requirements.txt"
    pins = {}
    if not req.exists():
        return pins
    for raw in req.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if "==" not in line:
            continue
        spec, _, marker = line.partition(";")
        name, _, ver = spec.partition("==")
        if marker_applies(marker):
            pins[name.strip().lower().replace("_", "-")] = ver.strip()
    return pins


def try_import(module, timeout):
    code = f"import {module}"
    t0 = time.perf_counter()
    try:
        r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                           timeout=timeout, encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return False, f"quá {timeout} giây", time.perf_counter() - t0
    dt = time.perf_counter() - t0
    if r.returncode == 0:
        return True, "", dt
    err = [ln for ln in r.stderr.strip().splitlines() if ln.strip()]
    return False, anonymize(err[-1] if err else f"mã thoát {r.returncode}"), dt


def check_python(rep):
    v = sys.version_info
    detail = f"{v.major}.{v.minor}.{v.micro}, {platform.system()} {platform.machine()}"
    if (v.major, v.minor) == EXPECTED_PYTHON:
        rep.add("OK", "Phiên bản Python", detail)
    else:
        rep.add("FAIL", "Phiên bản Python", detail + "; học phần dùng Python 3.12 (xem huong-dan-cai-dat.md)")
    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    rep.add("OK" if in_venv else "WARN", "Môi trường ảo",
            "đang chạy trong môi trường ảo" if in_venv else "đang dùng Python hệ thống, nên kích hoạt .venv")


def check_packages(rep, quick, timeout):
    pins = pinned_versions()
    if not pins:
        rep.add("WARN", "requirements.txt", "không tìm thấy tệp cạnh preflight_check.py, bỏ qua so phiên bản")
    for dist, (module, level) in PACKAGES.items():
        key = dist.lower().replace("_", "-")
        if key in pins or not pins:
            pass
        elif dist in ("tensorflow", "tf-keras", "deepface", "torch", "torchaudio", "speechbrain"):
            rep.add("INFO", dist, "không cài trên nền tảng này theo requirements.txt (xem mục macOS Intel)")
            continue
        ver = installed_version(dist)
        want = pins.get(key)
        if ver is None:
            rep.add("FAIL", dist, "chưa cài")
            continue
        vdetail = f"phiên bản {ver}" + ("" if not want or want == ver else f", requirements.txt ghim {want}")
        if quick and level == "nang":
            rep.add("OK" if (not want or want == ver) else "WARN", dist, vdetail + " (bỏ qua nhập thử)")
            continue
        ok, err, dt = try_import(module, timeout)
        if not ok:
            rep.add("FAIL", dist, f"{vdetail}; nhập lỗi: {err}")
        elif want and want != ver:
            rep.add("WARN", dist, vdetail)
        else:
            rep.add("OK", dist, f"{vdetail}, nhập trong {dt:.1f} s")


def check_opencv(rep):
    try:
        import cv2
    except Exception as exc:
        rep.add("FAIL", "OpenCV", f"không nhập được: {type(exc).__name__}")
        return
    major = int(cv2.__version__.split(".")[0])
    if major >= 5:
        rep.add("FAIL", "OpenCV < 5", f"đang là {cv2.__version__}; DeepFace 0.0.100 cần nhánh 4.x "
                                      "(OpenCV 5 bỏ CascadeClassifier và dnn.readNetFromCaffe)")
    else:
        rep.add("OK", "OpenCV < 5", cv2.__version__)
    rep.add("OK" if hasattr(cv2, "CascadeClassifier") else "FAIL", "cv2.CascadeClassifier")
    has_caffe = hasattr(cv2, "dnn") and hasattr(cv2.dnn, "readNetFromCaffe")
    rep.add("OK" if has_caffe else "FAIL", "cv2.dnn.readNetFromCaffe")
    try:
        xml = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
        clf = cv2.CascadeClassifier(str(xml))
        rep.add("OK" if xml.exists() and not clf.empty() else "FAIL", "Bộ phân loại Haar mặc định")
    except Exception as exc:
        rep.add("FAIL", "Bộ phân loại Haar mặc định", type(exc).__name__)
    n_opencv = [d for d in ("opencv-python", "opencv-contrib-python", "opencv-python-headless",
                            "opencv-contrib-python-headless") if installed_version(d)]
    if len(n_opencv) > 1:
        rep.add("WARN", "Nhiều bản OpenCV cùng cài", ", ".join(n_opencv) + "; nên giữ một bản opencv-python")


def check_matplotlib(rep, workdir):
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(2, 1))
        ax.set_title("Đường cong DET, tỷ lệ lỗi cân bằng")
        path = workdir / "thu-ve.png"
        fig.savefig(path)
        plt.close(fig)
        rep.add("OK" if path.stat().st_size > 0 else "FAIL", "Vẽ hình có chữ tiếng Việt (matplotlib Agg)")
    except Exception as exc:
        rep.add("FAIL", "Vẽ hình (matplotlib)", f"{type(exc).__name__}: {exc}")


def check_numeric(rep):
    try:
        import numpy as np
        rng = np.random.default_rng(4211)
        a = rng.standard_normal((200, 200))
        ok = np.allclose(a @ np.linalg.inv(a), np.eye(200), atol=1e-6)
        rep.add("OK" if ok else "FAIL", "Phép tính numpy (nghịch đảo ma trận 200 x 200)")
    except Exception as exc:
        rep.add("FAIL", "Phép tính numpy", f"{type(exc).__name__}")


def check_weights(rep):
    """Trọng số chỉ cần từ TH04 trở đi, nên thiếu hay hỏng đều là [CẢNH BÁO], không chặn TH01."""
    home = Path(os.environ.get("DEEPFACE_HOME", str(Path.home()))) / ".deepface" / "weights"
    if not home.exists():
        rep.add("WARN", "Trọng số DeepFace",
                "chưa có thư mục ~/.deepface/weights; cần trước TH04 (không ảnh hưởng TH01 đến TH03). "
                "Chép gói trọng số của phòng máy bằng `python download_weights.py giai-nen <gói .zip>` "
                "hoặc tải ở nhà bằng `python download_weights.py tai`")
        return
    files = sorted(p for p in home.iterdir() if p.is_file())
    small = [p.name for p in files if p.stat().st_size < 100_000]
    total = sum(p.stat().st_size for p in files) / 2**20
    rep.add("OK" if files else "WARN", "Trọng số DeepFace",
            f"{len(files)} tệp, tổng {total:.0f} MB" + ("" if files else "; cần trước TH04"))
    for name in small:
        labs = WEIGHT_LABS.get(name, "TH04 trở đi")
        rep.add("WARN", f"Tệp trọng số nghi hỏng: {name}",
                f"nhỏ hơn 100 KB, thường là trang báo lỗi của proxy; cần cho {labs}, không chặn TH01. "
                "Trước bài đó, xoá tệp hỏng bằng `python download_weights.py kiem-tra --xoa-tep-hong`, "
                "rồi chép lại từ gói trọng số của phòng máy (`python download_weights.py giai-nen <gói .zip>`) "
                "hoặc tải lại ở nhà (`python download_weights.py tai`)")


def check_speechbrain_model(rep):
    candidates = [HERE / "mo-hinh" / "spkrec-ecapa-voxceleb",
                  Path.home() / ".cache" / "bmst04211" / "spkrec-ecapa-voxceleb"]
    found = [p for p in candidates if (p / "hyperparams.yaml").exists()]
    if found:
        rep.add("OK", "Mô hình SpeechBrain ECAPA", anonymize(str(found[0])))
    else:
        rep.add("WARN", "Mô hình SpeechBrain ECAPA", "chưa tải trước; cần cho TH06 (xem download_weights.py)")


def check_system(rep, workdir):
    free = shutil.disk_usage(workdir).free / 2**30
    rep.add("OK" if free >= 10 else "WARN", "Dung lượng đĩa trống", f"{free:.1f} GB (khuyến nghị từ 10 GB)")
    try:
        if hasattr(os, "sysconf") and "SC_PHYS_PAGES" in os.sysconf_names:
            ram = os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / 2**30
            rep.add("OK" if ram >= 7.5 else "WARN", "Bộ nhớ RAM", f"{ram:.1f} GB (khuyến nghị từ 8 GB)")
    except (ValueError, OSError):
        pass
    if sys.platform == "win32":
        try:
            import winreg
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Control\FileSystem")
            val, _ = winreg.QueryValueEx(key, "LongPathsEnabled")
            rep.add("OK" if val == 1 else "WARN", "Windows LongPathsEnabled",
                    "đã bật" if val == 1 else "chưa bật; cài TensorFlow có thể lỗi đường dẫn dài")
        except OSError:
            rep.add("WARN", "Windows LongPathsEnabled", "không đọc được khoá registry")
    enc = os.environ.get("PYTHONUTF8")
    rep.add("OK" if enc == "1" or sys.platform != "win32" else "WARN", "Mã hoá UTF-8",
            f"PYTHONUTF8={enc}" if enc else "PYTHONUTF8 chưa đặt (chỉ cần trên Windows)")
    proxies = [k for k in ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy") if os.environ.get(k)]
    rep.add("INFO", "Biến proxy", ("có đặt: " + ", ".join(proxies)) if proxies else "không đặt")


def main():
    ap = argparse.ArgumentParser(description="Kiểm tra môi trường thực hành 04211")
    ap.add_argument("--nhanh", action="store_true", help="bỏ qua nhập thử các gói nặng")
    ap.add_argument("--timeout", type=int, default=180, help="giới hạn giây cho mỗi lần nhập thử")
    ap.add_argument("--bao-cao", default="preflight-bao-cao.txt")
    args = ap.parse_args()

    t0 = time.perf_counter()
    rep = Report()
    print("Kiểm tra môi trường học phần 04211 Bảo mật sinh trắc\n")
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        check_python(rep)
        check_system(rep, workdir)
        check_packages(rep, args.nhanh, args.timeout)
        check_opencv(rep)
        check_numeric(rep)
        check_matplotlib(rep, workdir)
        check_weights(rep)
        check_speechbrain_model(rep)
    elapsed = time.perf_counter() - t0
    summary = (f"\nTổng kết: {rep.n_ok} đạt, {rep.n_warn} cảnh báo, {rep.n_fail} lỗi; "
               f"thời gian kiểm tra {elapsed:.1f} s.")
    verdict = ("Môi trường sẵn sàng." if rep.n_fail == 0 else
               "Môi trường CHƯA sẵn sàng: xử lý các dòng [LỖI] theo bảng khắc phục trong huong-dan-cai-dat.md.")
    th01_block = [i for i in rep.failed_items if i in TH01_ITEMS]
    th01_line = ("Sẵn sàng cho TH01: có." if not th01_block else
                 "Sẵn sàng cho TH01: CHƯA, vì lỗi ở: " + ", ".join(th01_block) + ".")
    print(summary)
    print(verdict)
    print(th01_line)
    header = [
        "Báo cáo kiểm tra môi trường, học phần 04211 Bảo mật sinh trắc",
        f"Thời điểm: {time.strftime('%Y-%m-%d %H:%M')}",
        f"Hệ điều hành: {platform.system()} {platform.release()} ({platform.machine()})",
        f"Chế độ: {'nhanh' if args.nhanh else 'đầy đủ'}",
        "",
    ]
    try:
        Path(args.bao_cao).write_text("\n".join(header + rep.lines + [summary, verdict, th01_line]) + "\n",
                                      encoding="utf-8")
        print(f"Đã ghi báo cáo: {args.bao_cao}")
    except OSError as exc:
        print(f"Không ghi được báo cáo: {exc}")
    sys.exit(0 if rep.n_fail == 0 else 1)


if __name__ == "__main__":
    main()
