# Quy ước kho cá nhân và cách nộp bài

Bản dành cho sinh viên, học phần 04211 Bảo mật sinh trắc, lớp 2610421101. Áp dụng từ LAB_2. Bản 1.2, ngày 23/09/2026.

Mười bài thực hành của học phần sinh ra mười báo cáo, vài chục tệp mã và bảng số liệu. Tài liệu này quy định một cách làm duy nhất cho cả lớp: một kho riêng tư tên `sinhtrac-<MSSV>` tạo từ kho mẫu của học phần, mỗi bài một thư mục `labNN`, và bài nộp là đường dẫn của một lần ghi nhận (commit).

Cách làm này giống hệt môn 04210 Bảo mật phần mềm. Ai đã lập kho `minishop-<MSSV>` ở môn ấy thì dùng lại đúng tài khoản GitHub và đúng các thao tác; chỉ khác tên kho, tên thư mục bài, danh sách tệp cấm, và thẻ Actions ở đây chạy thêm kiểm thử của bài.

Mọi thao tác làm được trên giao diện web của GitHub, không phải gõ lệnh git nào. Nghĩa tiếng Việt của các nhãn tiếng Anh nằm ở bảng cuối tài liệu.

## 1. Tóm tắt

1. Kho tạo từ kho mẫu `04211-kho-mau` (đường dẫn ở đầu khoá học trên LMS), tên `sinhtrac-<MSSV>`, chế độ riêng tư (Private). Lập kho ở nhà, **trước 12h00 thứ Tư 30/09/2026**.
2. Ngay khi tạo kho, mời tài khoản GitHub của giảng viên làm cộng tác viên (collaborator). Tên tài khoản giảng viên ghi ở đầu khoá học trên LMS.
3. Mọi thứ của bài LAB_N nằm trong thư mục `labNN` (LAB_2 là `lab02`). Tệp `README.md` trong thư mục ghi đúng các tệp của bài.
4. Bài nộp là đường dẫn commit dán vào ô nộp của bài trên LMS, hạn 12h00 thứ Tư tuần kế tiếp. LAB_1 nộp bằng tệp như đã hướng dẫn. LAB_2: em nào chưa lập được kho kịp thì vẫn nộp tệp như LAB_1, và đầu ca thực hành 30/09 trợ giảng giúp lập kho.
5. **Không bao giờ** đưa lên kho dữ liệu sinh trắc: ảnh vân tay, khuôn mặt, mống mắt, tệp âm thanh giọng nói, thư mục `data/`, tệp `.db` (kể cả `fingerprint_templates.db`), `.pkl`, `.npy`, thư mục `cache-embedding/`, `db-tham-chieu/`, trọng số mô hình.

## 2. Kho trông như thế nào

```text
sinhtrac-<MSSV>/            kho riêng tư (private)
  README.md                 họ tên, MSSV, tài khoản GitHub
  AI-SUDUNG.md              khai báo dùng trợ lý lập trình
  .gitignore                có sẵn
  .github/workflows/        phép tự kiểm, không sửa
  .kiem/                    kịch bản tự kiểm, không sửa
  lab01/ ... lab10/
    README.md               tệp của bài này, có sẵn
    bao-cao.md              mẫu báo cáo, viết thẳng vào đây
    *.py                    mã nguồn của bài
    ket-qua/                bảng số liệu và đồ thị do chương trình ghi ra
    hinh/                   ảnh chụp màn hình
```

Chương trình của mỗi bài tự ghi bảng số liệu và đồ thị vào thư mục `ket-qua/` cạnh nó, với tên do chương trình đặt, ví dụ `TH01_2305CT0001_bang-ket-qua.csv`. Em tải đúng các tệp ấy vào `labNN/ket-qua/` trên kho, **giữ nguyên tên**. Với LAB_2, chạy `python th01_main.py --ma-sv <MSSV>` để tên tệp mang MSSV của em.

Mẫu `bao-cao.md` có đúng mười mục như mẫu báo cáo chung đã phát. Các dòng nằm giữa `<!--` và `-->` là hướng dẫn: chúng hiện ra khi sửa tệp nhưng không hiện khi xem trên GitHub, nên không cần xoá. Thay mọi chỗ trong ngoặc nhọn `{...}` bằng nội dung của em. Chèn đồ thị bằng dòng `![Hình 1: đường DET](ket-qua/TH01_2305CT0001_det.png)`.

| LAB | Nội dung | Thư mục trong portfolio |
|---|---|---|
| 1 | Phân tích hệ thống nhận dạng vân tay (AFIS) | theo đề trên LMS |
| 2 | Tự tính FMR, FNMR, EER, DET | `TH01_danh-gia-hieu-nang` |
| 3 | Tăng cường ảnh vân tay và trích minutiae | `TH02_tang-cuong-anh-van-tay` |
| 4 | Xác minh khuôn mặt 1:1 | `TH04_xac-minh-khuon-mat` |
| 5 | Định danh khuôn mặt 1:N | `TH05_dinh-danh-khuon-mat` |
| 6 | Xác minh người nói | `TH06_xac-minh-nguoi-noi` |
| 7 | IrisCode và hợp nhất điểm | `TH07_mong-mat-iriscode` |
| 8 | Phát hiện tấn công trình diện | `TH08_phat-hien-tan-cong-trinh-dien` |
| 9 | Bảo vệ mẫu sinh trắc | `TH09_bao-ve-mau-sinh-trac` |
| 10 | Bài nhóm tích hợp (buổi bù) | `TH10_tich-hop-nhom` |

Kế hoạch có thể đổi; đề bài trên LMS mỗi tuần là căn cứ cuối cùng.

## 3. Lập kho, một lần, trước 12h00 thứ Tư 30/09

1. Đăng nhập GitHub, mở đường dẫn kho mẫu ở đầu khoá học trên LMS.
2. Bấm **Use this template**, chọn **Create a new repository**. Đặt tên `sinhtrac-<MSSV>`, thí dụ `sinhtrac-2305CT0001`, chọn **Private**, bấm **Create repository**.
3. Vào **Settings**, mục **Collaborators**, bấm **Add people**, dán tên tài khoản giảng viên, xác nhận. Lời mời hết hạn sau bảy ngày; hết hạn thì mời lại.
4. Mở `README.md`, bấm biểu tượng cây bút, điền họ tên, MSSV, tài khoản GitHub, rồi bấm **Commit changes**.
5. Mở `lab01`, mở `bao-cao.md`, bấm cây bút, dán nội dung báo cáo LAB_1 của em vào các mục tương ứng, rồi **Commit changes**. Bước này để tập thao tác, không tính điểm.
6. Mở thẻ **Actions**: lần chạy mới nhất có dấu tích xanh là kho đã sẵn sàng.

**Tải tệp vào đúng thư mục.** Nút **Upload files** tải tệp vào thư mục đang mở. Muốn tệp vào `lab02/ket-qua` thì bấm vào `lab02`, rồi `ket-qua`, rồi mới bấm **Add file**, **Upload files**.

## 4. Phép tự kiểm sau mỗi lần ghi nhận

Mỗi lần em ghi nhận, thẻ **Actions** chạy hai bước trên máy của GitHub:

1. **Kiem tep, bao cao, so lieu**: tìm tệp cấm, ảnh sai chỗ, tệp thiếu; kiểm báo cáo; kiểm các tiêu chí số liệu công khai của bài (ghi ở `README.md` của thư mục bài).
2. **Chay kiem thu cong khai cua bai**: với bài có bộ kiểm thử phát sẵn, chạy mã của em với bộ kiểm thử ấy. Ở LAB_2 là `python test_bio_metrics.py`, phải đạt 21/21.

Dấu tích xanh là không thấy lỗi nào máy bắt được; dấu X đỏ là có lỗi, bấm vào lần chạy rồi vào bước bị đỏ để đọc từng dòng. Một bài chỉ được xem khi em đã bắt đầu viết `bao-cao.md` của bài ấy.

| Máy báo | Nghĩa | Cách sửa |
|---|---|---|
| `CO TEP CAM` | Có dữ liệu sinh trắc, tệp `.db`, `.pkl`, `.npy`, thư mục `data/` hay `venv/` | Xoá tệp (Mục 7). Với ảnh hay mẫu của người thật, báo giảng viên |
| `ANH SAI CHO` | Có ảnh nằm ngoài `hinh/` mà không phải đồ thị do chương trình của bài ghi ra | Chuyển ảnh vào `hinh/` |
| `TEP QUA LON` | Tệp trên 5 MB | Thường là dữ liệu, không phải bài làm; xoá |
| `THIEU TEP` | Thiếu một tệp bắt buộc của bài | Xem `README.md` của thư mục bài |
| `CON CHO TRONG CUA MAU`, `BAO CAO THIEU MUC`, `BAO CAO QUA NGAN`, `ANH KHONG CO TRONG KHO` | Báo cáo chưa hoàn chỉnh (còn `{...}`, thiếu mục `##`, viết thêm dưới 250 từ so với mẫu, chèn ảnh không có trong kho) | Viết tiếp, sửa tên mục, tải ảnh lên |
| `SO LIEU CHUA DAT`, `SAI DINH DANG SO LIEU`, `THIEU TEP SO LIEU` | Bảng số liệu thiếu cột, thiếu dòng, hoặc chưa đạt một tiêu chí công khai của bài | Chạy lại chương trình, không sửa tay con số |
| `TEN TEP KHONG MANG MSSV` | Chạy chương trình mà quên `--ma-sv` | Chạy lại với `--ma-sv <MSSV>` |
| `KIEM THU CHUA DAT` | Mã của em chưa qua bộ kiểm thử của bài | Chạy kiểm thử trên máy mình, sửa tới khi đạt |

Đừng sửa các tệp trong `.kiem/`, `.github/`, và các tệp kiểm thử phát sẵn như `test_bio_metrics.py`. Giảng viên so mã băm của chúng ở commit em nộp với bản phát; lệch là bài bị gắn cờ và phải giải thích trực tiếp.

## 4a. Điểm của mỗi bài

Mỗi bài chấm trên thang 10, theo bốn tầng giống môn 04210. Đạt khi từ 5,0 điểm, kho không có tệp cấm, và giảng viên mở được đúng commit em nộp.

| Tầng | Đo gì | Ai chấm | Trọng số |
|---|---|---|---|
| L0 | Nộp đúng, đủ, sạch: đủ tệp, đúng chỗ, báo cáo đủ mười mục, không có tệp cấm | máy | 20% |
| L1 | Số liệu đúng: các tiêu chí công khai của bài, kiểm thử đạt, số khớp kết quả mong đợi | máy | 20% |
| L2 | Phân tích: mục 5 và mục 6 của báo cáo, giải thích theo cơ chế và có bằng chứng | giảng viên | 40% |
| L3 | Góc nhìn bảo mật (mục 7) và phần mở rộng của bài | giảng viên | 20% |

Hai tầng đầu em biết trước nhờ thẻ **Actions**: thẻ xanh gần như bảo đảm phần máy chấm. Điểm cao nằm ở hai tầng sau.

## 5. Nộp bài bằng đường dẫn commit

### 5.1. Lấy đường dẫn

1. Tải đủ các tệp của bài lên kho, và thẻ **Actions** đã xanh ở cả hai bước.
2. Bấm **Commits** (biểu tượng đồng hồ có mũi tên, phía trên danh sách tệp).
3. Bấm vào dòng chữ thông điệp ở dòng trên cùng, tức lần ghi nhận mới nhất. Không bấm nút sao chép bên phải dòng, vì nút ấy chỉ chép mã bốn mươi ký tự, không chép đường dẫn.
4. Chép đường dẫn trên thanh địa chỉ. Đường dẫn đúng có chữ `/commit/` theo sau là bốn mươi ký tự chữ và số, thí dụ:

   `https://github.com/nguyenvanan/sinhtrac-2305CT0001/commit/9f2c4e0b7a1d38c65e2f4b9a0c7d1e3f5a6b8c90`

5. Mở ô nộp của bài trên LMS, bấm **Add submission**, dán đường dẫn vào ô văn bản, bấm **Save changes**. Dòng trạng thái phải ghi **Submitted for grading**.

### 5.2. Vì sao nộp đường dẫn commit

Đường dẫn của kho luôn mở ra bản mới nhất, nên những gì sửa sau hạn sẽ lẫn vào bài. Đường dẫn commit thì không đổi: chuỗi bốn mươi ký tự là mã băm (hash) tính từ toàn bộ nội dung kho ở thời điểm ghi nhận cùng lịch sử trước nó. Đổi một ký tự trong bất kỳ tệp nào là mã đổi theo. Người chấm và sinh viên nhìn đúng một phiên bản. Đây là tính toàn vẹn (integrity), áp vào chính bài nộp.

### 5.3. Sửa bài và hạn nộp

Sửa bài trước hạn: ghi nhận thêm trên kho, rồi bấm **Edit submission** trên LMS và thay đường dẫn cũ bằng đường dẫn của lần ghi nhận mới nhất. Người chấm chỉ chấm phiên bản mà đường dẫn chỉ tới.

Hạn nộp là 12h00 thứ Tư tuần kế tiếp, trước ca lý thuyết. Mốc có giá trị là mốc LMS ghi khi em lưu bài nộp. Qua hạn rồi thì đừng sửa bài nộp trên LMS nữa. Sinh viên vắng buổi có phép làm theo quy chế chuyên cần.

Trong buổi, khi trợ giảng hay giảng viên tới máy, em mở kho trên GitHub và bảng kết quả, đồ thị của bài, và giải thích ngắn một bước của bài làm.

## 6. Dữ liệu sinh trắc và kho Git

Git giữ mọi phiên bản của mọi tệp đã từng ghi nhận. Xoá một tệp ở lần ghi nhận sau không xoá được bản cũ trong lịch sử. Vì vậy quy tắc A5 của bản cam kết đạo đức ("không đưa dữ liệu sinh trắc học hoặc dữ liệu dẫn xuất vào Git") được áp đúng nghĩa đen ở kho này.

Tệp `.gitignore` trong kho mẫu chặn các tệp ấy khi làm bằng dòng lệnh. Khi tải bằng trình duyệt, GitHub không đọc `.gitignore`, nên người tải tự tránh chọn chúng; phép tự kiểm sẽ báo nếu lỡ tay. Tuyệt đối không kéo cả thư mục làm bài (có `data/`, `venv/`, tệp `.db`) vào ô tải lên.

Nếu lỡ đưa lên ảnh hay mẫu của người thật: báo giảng viên ngay, rồi làm theo hướng dẫn giảng viên gửi, thường là xoá kho, lập lại kho mới và tải lại bài làm không kèm tệp ấy.

## 7. Lỗi thường gặp và cách sửa

| Dấu hiệu | Nguyên nhân | Cách sửa |
|---|---|---|
| LMS nhận một đường dẫn không có chữ `/commit/` | Chép đường dẫn trang kho hoặc trang thư mục | Làm lại Mục 5.1 từ bước 2 |
| Giảng viên báo không mở được kho | Chưa mời, hoặc lời mời quá bảy ngày đã hết hạn | **Settings**, **Collaborators**, mời lại |
| Tệp nằm sai thư mục | Bấm **Upload files** khi chưa mở thư mục | Tệp văn bản: mở tệp, bấm cây bút, gõ thêm `lab03/` vào đầu ô tên tệp, **Commit changes**. Tệp ảnh: tải lại vào đúng thư mục rồi xoá bản sai chỗ |
| Lỡ tải tệp cấm lên | Chọn cả thư mục khi tải | Mở tệp, bấm dấu ba chấm, **Delete file**, **Commit changes**; với dữ liệu người thật, xem Mục 6 |
| Kho không có nhãn Private | Lúc tạo đã chọn Public | **Settings**, **Danger Zone**, **Change visibility**, **Make private** |
| Thẻ Actions không có lần chạy nào | Kho không tạo từ kho mẫu, hoặc Actions bị tắt | **Settings**, **Actions**, **General**, ở mục **Actions permissions** chọn dòng **Allow all actions and reusable workflows**; nếu kho không tạo từ kho mẫu thì báo giảng viên |
| GitHub đòi bật xác thực hai lớp | Chính sách của GitHub | Làm theo hướng dẫn trên màn hình; mất quyền vào tài khoản thì báo giảng viên trước hạn nộp |

## 8. Tự kiểm trước khi bấm nộp

1. Thẻ **Actions**: lần chạy mới nhất xanh.
2. Mở chính đường dẫn vừa chép: trang hiện ra là một lần ghi nhận, đúng là lần mới nhất.
3. Bấm **Browse files** trên trang ấy: thấy đủ tệp của bài, đúng thư mục `labNN`.
4. `AI-SUDUNG.md` đã ghi nếu có dùng trợ lý lập trình.
5. Đường dẫn trên LMS trùng với đường dẫn vừa kiểm.
6. **Settings**, **Collaborators**: tên tài khoản giảng viên không còn kèm chữ **Pending invite**.

## 9. Nghĩa các nhãn tiếng Anh

| Nhãn trên màn hình | Nghĩa |
|---|---|
| Use this template, Create a new repository | Dùng kho mẫu này, tạo kho mới |
| Private | Riêng tư |
| Add file, Upload files | Thêm tệp, tải tệp lên |
| Commit changes | Ghi nhận thay đổi |
| Edit this file (biểu tượng cây bút) | Sửa tệp này |
| Delete file | Xoá tệp |
| Commits | Lịch sử các lần ghi nhận |
| Browse files | Xem các tệp ở lần ghi nhận này |
| Actions | Thẻ chạy quy trình tự động |
| Settings, Collaborators | Thiết lập, cộng tác viên |
| Add people, Pending invite | Thêm người, lời mời đang chờ |
| Danger Zone, Change visibility, Make private | Vùng thao tác nguy hiểm, đổi chế độ hiển thị, chuyển sang riêng tư |
| Add submission, Save changes, Edit submission (LMS) | Thêm bài nộp, lưu thay đổi, sửa bài nộp |
| Submitted for grading (LMS) | Đã nộp để chấm |
