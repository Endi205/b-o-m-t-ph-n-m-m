# Hướng dẫn cài đặt môi trường thực hành

Học phần 04211 Bảo mật sinh trắc, dùng cho cả mười bài thực hành TH01 đến TH10.

| Mục | Nội dung |
|---|---|
| Phiên bản Python | 3.12 |
| Công cụ quản lý | uv (tạo môi trường ảo và cài gói) |
| Tệp gói | `requirements.txt` (máy cá nhân, phòng máy), `requirements-colab.txt` (Google Colab) |
| Kiểm tra sau cài | `python preflight_check.py` |
| Tải trước trọng số | `python download_weights.py tai` |
| Thời gian cài lần đầu | 20 đến 60 phút tuỳ tốc độ mạng |
| Buổi 1 | dùng máy phòng thực hành đã cài sẵn (mục 5.1); cài máy cá nhân sau Buổi 1 |

Các con số thời gian và dung lượng trong tài liệu này được đo trên máy thử Linux 2 nhân ảo, 7,8 GB RAM, Python 3.12, trừ thời gian cài đặt (ước lượng theo tốc độ mạng) và kích thước tệp cài lấy từ PyPI.

## 1. Vì sao cả lớp dùng chung một môi trường ghim phiên bản

Ở TH01, các bạn sẽ tự tính tỷ lệ lỗi cân bằng (equal error rate, EER) và đối chiếu với thư viện pyeer. Ở TH04, cả lớp so sánh EER của nhiều mô hình khuôn mặt trên cùng các cặp ảnh LFW. Những con số này chỉ đem ra thảo luận được khi mọi máy chạy cùng một phiên bản thư viện: chỉ cần OpenCV nâng từ nhánh 4 lên nhánh 5, bộ phát hiện khuôn mặt mặc định của DeepFace đã ngừng hoạt động (OpenCV 5.0.0.93 bỏ `CascadeClassifier` và `dnn.readNetFromCaffe`). Vì vậy `requirements.txt` ghim đúng phiên bản của mọi gói cấp cao, và bảng khắc phục lỗi ở mục 9 liệt kê những lần "nâng cấp ngầm" hay gặp nhất.

Ta chọn uv thay cho pip thuần vì uv tự tải được Python 3.12 mà không cần quyền quản trị, giải phụ thuộc nhanh và cho cùng một kết quả trên Windows, macOS và Linux.

## 2. Yêu cầu phần cứng

| Thành phần | Tối thiểu | Ghi chú |
|---|---|---|
| Bộ nhớ RAM | 8 GB | TensorFlow và PyTorch cùng nạp trong TH08, TH10 |
| Đĩa trống | 10 GB | môi trường ảo, trọng số mô hình, dữ liệu; trên máy thử Linux, môi trường ảo chiếm 7,2 GB vì bản PyTorch cho Linux kéo theo thư viện CUDA |
| CPU | 4 nhân (khuyến nghị) | toàn bộ bài chạy trên CPU, không cần GPU; máy thử 2 nhân ảo chạy được mọi bài trên dữ liệu tổng hợp nhưng chậm hơn |
| Camera, micro | không bắt buộc | chỉ dùng khi sinh viên tự nguyện tham gia TH08 theo phiếu đồng ý |

Kích thước tệp cài đặt chính lấy từ PyPI (truy cập 16/09/2026): TensorFlow 2.21.0 cho Python 3.12 là 351 MB (Windows), 223 MB (macOS Apple silicon), 573 MB (Linux); PyTorch 2.11.0 là 115 MB (Windows), 81 MB (macOS Apple silicon), 531 MB (Linux, chưa tính thư viện CUDA đi kèm).

## 3. Windows 10 và Windows 11

**Bước 1. Bật hỗ trợ đường dẫn dài.** TensorFlow có nhiều tệp nằm sâu trong cây thư mục; khi đường dẫn vượt 260 ký tự, việc cài đặt dừng giữa chừng với lỗi không tìm thấy tệp. Mở PowerShell bằng quyền quản trị và chạy:

```powershell
New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force
```

Sau đó khởi động lại máy. Trên máy phòng thực hành, bước này do bộ phận quản trị thực hiện.

**Bước 2. Cài Microsoft Visual C++ Redistributable** (bản x64) từ trang của Microsoft. TensorFlow trên Windows cần thư viện này; thiếu nó, lệnh `import tensorflow` báo lỗi nạp DLL.

**Bước 3. Cài uv** trong PowerShell thường (không cần quyền quản trị):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Đóng và mở lại PowerShell để lệnh `uv` có hiệu lực.

**Bước 4. Tạo thư mục làm việc và môi trường ảo.** Ta nên đặt thư mục ở đường dẫn ngắn, không dấu, không khoảng trắng, ví dụ `C:\bmst04211`, vì một số thư viện xử lý sai đường dẫn có ký tự tiếng Việt.

```powershell
mkdir C:\bmst04211
cd C:\bmst04211
# chép thư mục 04_Thuc-hanh của học phần vào đây
uv python install 3.12
uv venv --python 3.12 .venv
.venv\Scripts\activate
uv pip install -r 04_Thuc-hanh\00_moi-truong\requirements.txt
```

Nếu PowerShell từ chối chạy `activate`, chạy một lần `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` rồi thử lại.

**Bước 5. Đặt mã hoá UTF-8 cho Python.** Các chương trình của học phần in thông báo tiếng Việt; bảng mã mặc định của cửa sổ lệnh Windows có thể gây lỗi `UnicodeEncodeError`.

```powershell
setx PYTHONUTF8 1
```

Biến này có hiệu lực ở cửa sổ lệnh mở sau đó.

**Lưu ý về GPU.** Từ TensorFlow 2.11, bản chạy trực tiếp trên Windows chỉ dùng CPU; muốn dùng GPU phải qua WSL2. Học phần không cần GPU nên sinh viên không phải cấu hình thêm.

## 4. macOS

### 4.1. Máy chip Apple (M1, M2, M3, M4)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
mkdir -p ~/bmst04211 && cd ~/bmst04211
# chép thư mục 04_Thuc-hanh của học phần vào đây
uv python install 3.12
uv venv --python 3.12 .venv
source .venv/bin/activate
uv pip install -r 04_Thuc-hanh/00_moi-truong/requirements.txt
```

Nên dùng macOS 14 trở lên: gói TenSEAL 0.3.18 chỉ có bản cài sẵn gắn nhãn macOS 14 cho chip Apple, còn OpenCV 4.14.0.94 cần macOS 13 (theo tên tệp wheel trên PyPI, truy cập 16/09/2026). Không cần cài `tensorflow-metal`, vì các bài chạy tốt trên CPU.

### 4.2. Máy chip Intel

Đây là nền tảng có giới hạn thật sự, và sinh viên dùng máy này cần biết trước để chủ động:

- TensorFlow 2.21.0 không phát hành bản cho macOS Intel; trong các bản đã kiểm tra, bản mới nhất còn hỗ trợ macOS Intel với Python 3.12 là 2.16.2.
- PyTorch 2.11.0 không có bản macOS Intel; bản cuối cùng có là 2.2.2.
- TenSEAL 0.3.18 và numba (gói mà galois cần) cũng không có bản cài sẵn cho macOS Intel.
- OpenCV 4.14.0.94 cho macOS Intel yêu cầu macOS 14 trở lên.

`requirements.txt` đã có điều kiện nền tảng, nên cùng lệnh cài ở mục 4.1 sẽ tự bỏ qua TensorFlow, tf-keras, DeepFace, PyTorch, torchaudio, SpeechBrain, TenSEAL và galois trên máy Intel. Với phần còn lại, máy Intel làm trọn TH01, TH02, TH03, TH07 và phần BioHashing, cam kết mờ (dùng bchlib hoặc mã lặp) của TH09. Các bài TH04, TH05, TH06, TH08, phần mã hoá đồng cấu của TH09 và TH10 được làm trên máy phòng thực hành, hoặc trên Colab với dữ liệu công khai (mục 7). Ta không khuyến nghị tự ghép TensorFlow 2.16 với các gói khác trên máy Intel, vì tổ hợp đó chưa được kiểm thử cho học phần và kết quả sẽ không so sánh được với cả lớp.

## 5. Máy phòng thực hành

### 5.1. Sinh viên dùng máy phòng thực hành

Ở Buổi 1, và ở các buổi sau khi máy cá nhân chưa sẵn sàng, sinh viên làm bài trên máy phòng thực hành. Môi trường của học phần đã được cài sẵn ở một đường dẫn cố định; giảng viên thông báo đường dẫn đó ở Buổi 1. Các bước:

1. Đăng nhập máy bằng tài khoản phòng máy.
2. Mở thư mục học phần đã được chép sẵn trên máy (thư mục chứa `04_Thuc-hanh`), không làm việc trực tiếp trên thư mục dùng chung của cả lớp, vì bài của người này có thể ghi đè bài của người khác.
3. Kích hoạt môi trường đã chuẩn bị: trên Windows chạy `<đường dẫn môi trường>\Scripts\activate`, trên Linux hoặc macOS chạy `source <đường dẫn môi trường>/bin/activate`. Không tạo môi trường mới và không cài thêm gói, vì một gói cài thêm có thể nâng ngầm OpenCV hay setuptools cho mọi người dùng chung máy.
4. Trong thư mục `04_Thuc-hanh/00_moi-truong`, chạy `python preflight_check.py --nhanh` và xem dòng cuối "Sẵn sàng cho TH01". Nếu có dòng `[LỖI]` ở mục TH01 cần, báo trợ giảng để được chuyển máy.

Cuối buổi, sinh viên chép thư mục bài làm của mình sang thiết bị cá nhân rồi nộp theo `quy-uoc-nop-bai.md`, vì một số phòng máy khôi phục ổ đĩa sau khi khởi động lại.

### 5.2. Chuẩn bị của giảng viên và trợ giảng

Phòng máy phục vụ 40 đến 60 sinh viên cùng lúc, nên mọi thứ cần tải qua mạng phải được chuẩn bị trước buổi học:

1. Trước học kỳ, gửi bộ phận quản trị tệp `requirements.txt` và mục 3 của tài liệu này, đề nghị cài sẵn môi trường ảo dùng chung tại một đường dẫn cố định. Lý do: cài trên 60 máy cùng lúc trong giờ học vừa chậm vừa dễ bị giới hạn băng thông.
2. Hỏi bộ phận quản trị máy có phần mềm khôi phục trạng thái sau khi khởi động lại hay không. Nếu có, môi trường ảo và thư mục trọng số phải nằm trên ổ đĩa không bị khôi phục, nếu không mọi thứ biến mất sau mỗi buổi.
3. Trên một máy có mạng ổn định, chạy `python download_weights.py tai`, rồi `python download_weights.py dong-goi goi-trong-so.zip`. Chép gói lên thư mục chia sẻ hoặc USB.
4. Trên từng máy phòng thực hành, chạy `python download_weights.py giai-nen goi-trong-so.zip`. Tệp được đặt đúng vào `~/.deepface/weights` và thư mục mô hình SpeechBrain, nên DeepFace không gọi GitHub nữa.
5. Chép sẵn dữ liệu công khai (mục 8) vào thư mục `du-lieu` dùng chung, và chép bản phát hành cho sinh viên của thư mục bài thực hành lên từng máy, để sinh viên làm được mục 5.1 ngay ở Buổi 1.
6. Chạy `python preflight_check.py` trên vài máy mẫu; báo cáo phải kết thúc bằng dòng "Môi trường sẵn sàng".

## 6. Tải trước trọng số mô hình

DeepFace tải trọng số ở lần gọi đầu tiên của mỗi mô hình và lưu vào `~/.deepface/weights` (đổi thư mục gốc bằng biến môi trường `DEEPFACE_HOME`). Có hai rủi ro khi để việc này xảy ra trong giờ học. Rủi ro thứ nhất là thời gian: cả lớp cùng chờ. Rủi ro thứ hai khó thấy hơn: khi GitHub hoặc proxy từ chối yêu cầu, thứ được lưu xuống là một trang báo lỗi vài trăm byte mang tên tệp trọng số; các lần chạy sau DeepFace không tải lại mà báo những lỗi không liên quan. Trong lần kiểm thử bộ bài, một tệp SFace hỏng loại này khiến DeepFace báo thiếu `opencv-contrib-python`, còn tệp MiniFASNet hỏng gây lỗi `UnpicklingError` của PyTorch.

Lệnh `python download_weights.py tai` gọi `DeepFace.build_model` cho các mô hình cần dùng, tải mô hình SpeechBrain, rồi xoá tệp nào nhỏ hơn 100 KB. Bảng dưới đây ghi dung lượng đo trên máy thử; ô trống là tệp mà mạng của máy thử không tải được.

| Tệp | Dùng ở | Dung lượng |
|---|---|---|
| `facenet512_weights.h5` | TH04, TH05, TH09, TH10 | 90,6 MB |
| `arcface_weights.h5` | TH04 | 130,7 MB |
| `retinaface.h5` | TH04 (bộ phát hiện RetinaFace) | 113,2 MB |
| `face_recognition_sface_2021dec.onnx` | TH04 | |
| `2.7_80x80_MiniFASNetV2.pth`, `4_0_0_80x80_MiniFASNetV1SE.pth` | TH08, TH10 | |
| mô hình `speechbrain/spkrec-ecapa-voxceleb` | TH06 | |

Trọng số chỉ cần từ TH04 trở đi. Vì vậy `preflight_check.py` báo tệp thiếu hoặc nghi hỏng bằng dòng `[CẢNH BÁO]` ghi rõ bài cần tệp đó, không bằng `[LỖI]`: sinh viên vẫn làm TH01 đến TH03 bình thường và xử lý tệp hỏng trước bài được nêu.

Mô hình mặc định VGG-Face nặng 553 MB; học phần cố ý không dùng nó để giảm thời gian tải. Tương tự, ta không gọi `DeepFace.analyze`, vì hàm này tải thêm bốn mô hình thuộc tính khuôn mặt không phục vụ mục tiêu của học phần.

Mô hình SpeechBrain được tải từ Hugging Face (https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb, giấy phép Apache-2.0) vào `~/.cache/bmst04211/spkrec-ecapa-voxceleb`. Nếu cần tải tay, dùng lệnh `hf download speechbrain/spkrec-ecapa-voxceleb --local-dir <thư mục>` của gói huggingface_hub đã cài trong môi trường.

## 7. Phương án dự phòng: Google Colab

Khi máy cá nhân không cài được, sinh viên có thể dùng Colab. Máy ảo Colab bắt đầu với thư mục làm việc trống, nên lệnh cài chỉ chạy được khi tệp danh sách gói đã có ở đó. Các bước:

1. Mở bảng Tệp (biểu tượng thư mục ở thanh bên trái của notebook) và tải lên `requirements-colab.txt` từ thư mục `04_Thuc-hanh/00_moi-truong` của học phần, cùng thư mục bài thực hành cần làm (không kèm dữ liệu cá nhân).
2. Chạy ô đầu tiên:

```python
!pip install -q -r requirements-colab.txt
```

Nếu không tải tệp lên được, sinh viên dán các dòng không bắt đầu bằng dấu `#` của `requirements-colab.txt` vào sau `!pip install -q`, mỗi gói đặt trong dấu ngoặc kép, ví dụ `!pip install -q "deepface==0.0.100" "tf-keras==2.20.1" "opencv-python<5"` và tiếp tục như vậy cho các gói còn lại.

Tệp `requirements-colab.txt` không cài lại TensorFlow và PyTorch mà dùng bản Colab có sẵn (Colab bản 2026.07: Python 3.12.13, TensorFlow 2.20.0, PyTorch 2.11.0), nên tf-keras được ghim ở nhánh 2.20 cho khớp. Khi chạy `preflight_check.py` trên Colab, các dòng `[CẢNH BÁO]` về phiên bản TensorFlow, tf-keras hay numpy khác với `requirements.txt` là dự kiến và không cần xử lý.

**Giới hạn bắt buộc về dữ liệu.** Colab chạy trên máy chủ của Google. Tải ảnh khuôn mặt, giọng nói hay vân tay của bản thân hoặc của bạn cùng lớp lên Colab là chuyển dữ liệu sinh trắc học (một loại dữ liệu cá nhân nhạy cảm) cho bên thứ ba, trái với cam kết xử lý cục bộ trong `cam-ket-dao-duc-va-dong-y.md` và với tinh thần của Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15. Vì vậy trên Colab chỉ dùng tập công khai (LFW, FVC set B, Mini LibriSpeech) hoặc dữ liệu tổng hợp do chính bộ bài sinh ra.

## 8. Dữ liệu công khai và nơi đặt

Dữ liệu tải tay đặt trong thư mục `du-lieu/` cạnh `04_Thuc-hanh/`, không đưa vào Git (dùng `gitignore-mau.txt`). Riêng LFW do scikit-learn tự tải và tự quản lý trong thư mục `~/scikit_learn_data`, nên không cần chép vào `du-lieu/`. Các tập dưới đây chỉ dùng cho mục đích học tập; ta không phát tán lại lên mạng.

| Tập dữ liệu | Bài | Nguồn chính thức | Dung lượng | Điều kiện |
|---|---|---|---|---|
| LFW (cặp ảnh và ảnh theo người) | TH04, TH05 | tự tải qua `sklearn.datasets.fetch_lfw_pairs` và `fetch_lfw_people`, lưu ở `~/scikit_learn_data` | chưa đo (máy thử không tải được) | ảnh người nổi tiếng, không có giấy phép chính thức |
| FVC2004 DB1 set B | TH02, TH03 | http://bias.csr.unibo.it/fvc2004/download.asp (truy cập 16/09/2026) | 10,0 MB | tải miễn phí; 10 ngón (số hiệu 101 đến 110), mỗi ngón 8 lần thu |
| SOCOFing | TH03 | Kaggle, bộ dữ liệu `ruizgara/socofing` | 773 MB | nghiên cứu phi thương mại; 6.000 ảnh thật của 600 người |
| CASIA-IrisV4 Interval | TH07 | đăng ký với đơn vị phát hành | 30,9 MB | nghiên cứu và giáo dục, cần đăng ký |
| Mini LibriSpeech dev-clean-2 | TH06 | https://www.openslr.org/31/ | 126 MB | CC BY 4.0 |

Mọi bài đều có dữ liệu tổng hợp thay thế (TH01, TH02, TH03, TH07, TH09, TH10) hoặc chế độ kiểm thử mã không cần dữ liệu thật (TH05, TH06, TH08), để sinh viên không bị chặn khi mạng hỏng.

## 9. Bảng khắc phục lỗi thường gặp

| Hiện tượng | Nguyên nhân | Cách xử lý |
|---|---|---|
| DeepFace báo thiếu `CascadeClassifier` hoặc `readNetFromCaffe` | một gói khác đã kéo OpenCV lên 5.x | `uv pip install "opencv-python==4.14.0.94"`; gỡ `opencv-contrib-python` hoặc bản headless nếu có; chạy lại `preflight_check.py` |
| `ValueError: You have tensorflow 2.21.0 and this requires tf-keras package` | thiếu tf-keras (bắt buộc từ TensorFlow 2.16) | `uv pip install "tf-keras==2.21.0"`; phiên bản tf-keras phải cùng nhánh với TensorFlow |
| Lần gọi DeepFace hoặc SpeechBrain đầu tiên đứng rất lâu | đang tải trọng số hàng trăm MB | tải trước theo mục 6; trong phòng máy dùng gói đã đóng |
| SFace báo cần `opencv-contrib-python`, hoặc anti-spoofing báo `UnpicklingError` | tệp trọng số là trang báo lỗi vài trăm byte | `python download_weights.py kiem-tra --xoa-tep-hong`, rồi tải lại |
| Cài TensorFlow trên Windows dừng với lỗi không tìm thấy tệp có đường dẫn rất dài | chưa bật LongPathsEnabled | làm bước 1 mục 3, khởi động lại; đặt thư mục làm việc ở đường dẫn ngắn |
| `ImportError: DLL load failed` khi `import tensorflow` trên Windows | thiếu Visual C++ Redistributable | làm bước 2 mục 3 |
| `SSL: CERTIFICATE_VERIFY_FAILED` hoặc `ProxyError` khi cài gói, tải trọng số | mạng trường đi qua proxy hoặc kiểm tra TLS | đặt biến `HTTPS_PROXY`; với uv thêm tuỳ chọn `--native-tls` để dùng chứng chỉ của hệ điều hành; nếu proxy chặn hẳn tên miền (lỗi 403), dùng gói trọng số chép tay |
| `ModuleNotFoundError: No module named 'pkg_resources'` khi nhập pyeer | setuptools từ 82 đã bỏ `pkg_resources` | `uv pip install "setuptools==81.0.0"` |
| `UserWarning: pkg_resources is deprecated ...` khi nhập pyeer | setuptools 81 báo trước việc gỡ `pkg_resources`; đây là cảnh báo, không phải lỗi | không cần xử lý; môi trường ghim setuptools 81 chính vì lý do này, và `th01_main.py` đã lọc cảnh báo |
| Trọng số DeepFace thiếu hoặc nghi hỏng trong báo cáo `preflight_check.py` | chưa chép gói trọng số, hoặc proxy trả trang báo lỗi | dòng này là `[CẢNH BÁO]` và không chặn TH01 đến TH03; trước bài được nêu, chạy `python download_weights.py kiem-tra --xoa-tep-hong` rồi chép gói trọng số của phòng máy hoặc tải lại ở nhà |
| `UnicodeEncodeError` khi chương trình in tiếng Việt | cửa sổ lệnh Windows không dùng UTF-8 | `setx PYTHONUTF8 1`, mở cửa sổ lệnh mới |
| SpeechBrain trên Windows báo thiếu quyền tạo liên kết tượng trưng | chế độ tải mặc định dùng symlink | mã của TH06 đã dùng `LocalStrategy.COPY`; nếu tự viết, thêm tham số này |
| `HFValidationError: Repo id must be in the form ...` khi nạp ECAPA | đường dẫn thư mục mô hình không tồn tại nên SpeechBrain hiểu nhầm là tên kho Hugging Face | kiểm tra lại đường dẫn truyền cho `--model-dir` |
| `RuntimeError` về khởi động tiến trình con khi dùng LightPHE trên Windows | LightPHE mã hoá song song bằng multiprocessing | đặt mã chính trong khối `if __name__ == "__main__":` |
| Cảnh báo `square is deprecated` từ fingerprint-feature-extractor | thư viện dùng hàm cũ của scikit-image | giữ `scikit-image==0.26.0`; cảnh báo nói hàm sẽ bị gỡ ở 0.27, khi đó thư viện sẽ lỗi |

## 10. Kiểm tra cuối cùng

Trong thư mục `00_moi-truong`, với môi trường ảo đã kích hoạt:

```bash
python preflight_check.py
```

Chương trình nhập thử từng gói trong tiến trình con riêng, kiểm tra OpenCV thuộc nhánh 4 và còn `CascadeClassifier`, vẽ thử một hình có chữ tiếng Việt, liệt kê trọng số đã có và đánh dấu tệp nghi hỏng. Nó không cần mạng. Lần chạy đầu tiên ngay sau khi cài có thể mất 2 đến 3 phút, vì TensorFlow và PyTorch nhập lần đầu rất chậm; chương trình không bị treo. Trên máy thử Linux 2 nhân ảo, các lần chạy sau mất khoảng 20 đến 30 giây ở chế độ đầy đủ và dưới 15 giây ở chế độ `--nhanh`.

Dòng `[LỖI]` là thành phần của môi trường chung bị thiếu hoặc hỏng; dòng `[CẢNH BÁO]` ghi rõ bài thực hành cần xử lý trước. Dòng cuối "Sẵn sàng cho TH01" chỉ xét những gì TH01 cần. Tệp `preflight-bao-cao.txt` là sản phẩm nộp của bước 1 trong TH01.
