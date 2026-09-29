# -*- coding: utf-8 -*-
"""Tải trước và đóng gói trọng số mô hình cho phòng máy, để buổi thực hành không phụ thuộc mạng.

Vì sao cần: DeepFace tải trọng số từ GitHub (tệp phát hành và tệp raw) ở lần gọi đầu tiên. Khi
40 đến 60 máy cùng tải trong một phòng, giới hạn tần suất của GitHub hoặc proxy có thể trả về
một trang báo lỗi vài trăm byte; DeepFace lưu trang đó thành tệp trọng số và các lần chạy sau
báo lỗi khó hiểu. Giảng viên nên tải một lần, kiểm tra kích thước, đóng gói, rồi chép sang các máy.

Cách dùng:
    python download_weights.py tai                 tải trọng số DeepFace và mô hình SpeechBrain
    python download_weights.py kiem-tra            kiểm tra các tệp đã có, đánh dấu tệp nghi hỏng
    python download_weights.py dong-goi goi-trong-so.zip
    python download_weights.py giai-nen goi-trong-so.zip   (chạy trên từng máy phòng thực hành)
"""
import argparse
import os
import sys
import time
import zipfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass

HERE = Path(__file__).resolve().parent
MIN_BYTES = 100_000     # tệp nhỏ hơn ngưỡng này gần như chắc chắn là trang báo lỗi
SB_REPO = "speechbrain/spkrec-ecapa-voxceleb"
SB_DIR = Path.home() / ".cache" / "bmst04211" / "spkrec-ecapa-voxceleb"

# (tác vụ của DeepFace.build_model, tên mô hình); đủ cho TH04, TH05, TH08, TH09, TH10
DEEPFACE_MODELS = [
    ("facial_recognition", "Facenet512"),
    ("facial_recognition", "ArcFace"),
    ("facial_recognition", "SFace"),
    ("face_detector", "retinaface"),
    ("face_detector", "mtcnn"),
    ("spoofing", "Fasnet"),
]


def weights_dir():
    return Path(os.environ.get("DEEPFACE_HOME", str(Path.home()))) / ".deepface" / "weights"


def check_files(delete_bad=False):
    bad = []
    for d in (weights_dir(), SB_DIR):
        if not d.exists():
            print(f"Chưa có thư mục {d.name}")
            continue
        for p in sorted(d.rglob("*")):
            if not p.is_file():
                continue
            size = p.stat().st_size
            suspicious = size < MIN_BYTES and p.suffix in {".h5", ".onnx", ".pth", ".ckpt", ".pt"}
            print(f"  {'NGHI HỎNG' if suspicious else 'ổn       '} {p.name:45s} {size / 2**20:9.1f} MB")
            if suspicious:
                bad.append(p)
    if bad and delete_bad:
        for p in bad:
            p.unlink()
        print(f"Đã xoá {len(bad)} tệp nghi hỏng; hãy chạy lại lệnh tai.")
    return bad


def download_deepface():
    from deepface import DeepFace
    for task, name in DEEPFACE_MODELS:
        t0 = time.perf_counter()
        try:
            DeepFace.build_model(model_name=name, task=task)
            print(f"[ĐẠT] {task}/{name} ({time.perf_counter() - t0:.1f} s)")
        except Exception as exc:
            print(f"[LỖI] {task}/{name}: {type(exc).__name__}: {str(exc)[:200]}")


def download_speechbrain():
    from huggingface_hub import snapshot_download
    t0 = time.perf_counter()
    try:
        snapshot_download(repo_id=SB_REPO, local_dir=str(SB_DIR))
        print(f"[ĐẠT] {SB_REPO} -> {SB_DIR} ({time.perf_counter() - t0:.1f} s)")
    except Exception as exc:
        print(f"[LỖI] {SB_REPO}: {type(exc).__name__}: {str(exc)[:200]}")


def pack(zip_path):
    n = 0
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_STORED) as z:
        for base, arc in ((weights_dir(), "deepface-weights"), (SB_DIR, "spkrec-ecapa-voxceleb")):
            if not base.exists():
                continue
            for p in sorted(base.rglob("*")):
                if p.is_file() and not (p.stat().st_size < MIN_BYTES and p.suffix in {".h5", ".onnx", ".pth"}):
                    z.write(p, f"{arc}/{p.relative_to(base).as_posix()}")
                    n += 1
    print(f"Đã đóng gói {n} tệp vào {zip_path} ({Path(zip_path).stat().st_size / 2**20:.0f} MB)")


def unpack(zip_path):
    targets = {"deepface-weights": weights_dir(), "spkrec-ecapa-voxceleb": SB_DIR}
    with zipfile.ZipFile(zip_path) as z:
        for info in z.infolist():
            top, _, rest = info.filename.partition("/")
            if top not in targets or not rest or info.is_dir() or ".." in Path(rest).parts:
                continue
            dest = targets[top] / rest
            dest.parent.mkdir(parents=True, exist_ok=True)
            with z.open(info) as src, open(dest, "wb") as dst:
                dst.write(src.read())
    print("Đã giải nén; kiểm tra lại:")
    check_files()


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("tai")
    k = sub.add_parser("kiem-tra")
    k.add_argument("--xoa-tep-hong", action="store_true")
    d = sub.add_parser("dong-goi")
    d.add_argument("zip")
    g = sub.add_parser("giai-nen")
    g.add_argument("zip")
    args = ap.parse_args()
    if args.cmd == "tai":
        download_deepface()
        download_speechbrain()
        bad = check_files(delete_bad=True)
        sys.exit(1 if bad else 0)
    elif args.cmd == "kiem-tra":
        sys.exit(1 if check_files(delete_bad=args.xoa_tep_hong) else 0)
    elif args.cmd == "dong-goi":
        pack(args.zip)
    else:
        unpack(args.zip)


if __name__ == "__main__":
    main()
