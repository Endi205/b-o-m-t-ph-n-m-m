# Quy ước nộp sản phẩm thực hành và cách kiểm tra hoàn thành

> **Cập nhật 23/09/2026.** Từ LAB_2 (giao ngày 23/09/2026), bài nộp là đường dẫn commit của kho cá nhân `sinhtrac-<MSSV>`, theo `00_Quy-uoc-kho-ca-nhan_04211 (bản mới nhất)` trong thư mục này. Tài liệu ấy thay mục 2 (tên tệp, tệp nén, nơi nộp) và mục 3 (loại sản phẩm) của tài liệu này. Mục 1, mục 4 (kiểm tra hoàn thành trong buổi) và mục 5 giữ nguyên.

Học phần 04211 Bảo mật sinh trắc. Áp dụng cho TH01 đến TH10.

## 1. Bài thực hành được ghi nhận như thế nào

Đề cương học phần chỉ có ba cột điểm: chuyên cần (25% điểm học phần), kiểm tra giữa kỳ (25%) và thi cuối kỳ (50%). Bài thực hành **không phải là một cột điểm riêng**. Mỗi bài được trợ giảng hoặc giảng viên kiểm tra hoàn thành (check-off) ngay trong buổi, với hai kết quả "Đạt" hoặc "Chưa đạt".

Kết quả kiểm tra hoàn thành phục vụ hai việc, và đó là lý do sinh viên nên làm nghiêm túc dù không có điểm số riêng:

1. **Minh chứng cho điểm chuyên cần.** Theo phụ lục 1 của đề cương, điểm chuyên cần gồm phần hiện diện (70%) và phần tích cực (30%). Phần tích cực xét mức độ tham gia, mức độ tương tác và chất lượng câu trả lời: không tham gia hoặc không trả lời được thì dưới 4; chỉ trả lời khi được chỉ định thì từ 4 đến 5,9; có đặt hoặc trả lời câu hỏi thì từ 6 đến 7,9; nhiệt tình trao đổi, trả lời nhiều câu hỏi thì từ 8 đến 10. Việc hoàn thành bài, trả lời được câu hỏi phân tích khi trợ giảng hỏi và giúp bạn khác gỡ lỗi là các minh chứng cụ thể mà giảng viên ghi vào sổ theo dõi cho phần tích cực này.
2. **Chuẩn bị cho bài kiểm tra giữa kỳ hình thức thực hành**, phạm vi Buổi 1 đến Buổi 5, tức TH01 đến TH05. Bài kiểm tra yêu cầu tự tay tính và giải thích những đại lượng đã làm trong các buổi thực hành đó; sinh viên đã tự viết `bio_metrics.py` ở TH01 và tự chạy lại được TH02 đến TH05 sẽ không bị bất ngờ.

## 2. Quy ước đặt tên tệp và thư mục

**Chỉ dùng ký tự ASCII: chữ thường không dấu, chữ số, dấu gạch ngang `-` và gạch dưới `_`; không khoảng trắng.** Lý do: thư mục học phần được đồng bộ qua Google Drive và mở trên cả Windows lẫn macOS; cùng một chữ tiếng Việt có dấu có thể được mã hoá theo hai dạng chuẩn hoá Unicode khác nhau (dạng tách rời và dạng dựng sẵn) tuỳ hệ điều hành và phần mềm, nên một tên như "báo cáo" có thể thành hai tệp khác nhau hoặc không mở được trên máy trợ giảng; hiện tượng này đã xảy ra trên thư mục Drive của học phần. Khoảng trắng trong tên tệp làm hỏng các lệnh dòng lệnh khi không có dấu ngoặc kép.

Cấu trúc nộp cho bài cá nhân (TH01 đến TH09):

```
<ma-sinh-vien>_bmst04211/
  TH01/
    TH01_<ma-sinh-vien>_bang-ket-qua.csv
    TH01_<ma-sinh-vien>_det.png
    TH01_<ma-sinh-vien>_tra-loi.md
    preflight-bao-cao.txt
    bio_metrics.py
    th01_main.py
  TH02/
    ...
```

Cấu trúc nộp cho bài nhóm (TH10):

```
nhom<NN>_bmst04211_TH10/
  ma-nguon/                      toàn bộ mã, không kèm dữ liệu
  TH10_nhom<NN>_bao-cao.md
  TH10_nhom<NN>_mo-hinh-de-doa.md
  TH10_nhom<NN>_bao-cao-danh-gia.json
  TH10_nhom<NN>_trinh-bay.pdf
```

Quy tắc chung cho tên tệp: `TH<số bài hai chữ số>_<mã sinh viên hoặc nhom<NN>>_<nội dung>.<đuôi>`. Tiền tố số bài đứng đầu để khi sắp xếp theo tên, các tệp của cùng một bài nằm liền nhau. Chương trình chính của TH01 nhận tham số mã sinh viên (`python th01_main.py --ma-sv <mã sinh viên>`) và tự đặt tên tệp kết quả theo quy tắc này. Ở các bài mà chương trình ghi tệp kết quả không có mã sinh viên (ví dụ `TH02_bang-minutiae.csv`), sinh viên đổi tên khi chép tệp vào thư mục nộp, theo đúng danh sách trong README của bài.

Hai loại tệp được giữ nguyên tên gốc: tệp mã nguồn (`bio_metrics.py`, `th01_main.py`, ...) và báo cáo `preflight-bao-cao.txt`. Lý do: bài sau nhập `bio_metrics.py` theo đúng tên đó, trợ giảng chạy lại mã bằng lệnh ghi trong README, và báo cáo kiểm tra môi trường do chương trình đặt tên; tên thư mục `<ma-sinh-vien>_bmst04211/THxx/` đã cho biết bài của ai.

### Nơi nộp và thời hạn

Mặc định dưới đây áp dụng khi giảng viên không thông báo cách khác; nếu thay đổi, giảng viên thông báo ở Buổi 1 và trên kênh học tập của lớp.

1. **Trong buổi:** sinh viên trình sản phẩm ngay trên máy đang dùng khi được kiểm tra hoàn thành (mục 4). Lý do: kiểm tra hoàn thành xác nhận chính sinh viên đã chạy được bài trong buổi học.
2. **Sau buổi:** sinh viên nén thư mục `<ma-sinh-vien>_bmst04211/THxx/` thành tệp `<ma-sinh-vien>_bmst04211_THxx.zip` (bài nhóm: `nhom<NN>_bmst04211_TH10.zip`) và tải lên kênh học tập của lớp mà giảng viên thông báo ở Buổi 1, **trước giờ bắt đầu buổi học kế tiếp**. Tệp nén gồm cả phần trả lời câu hỏi phân tích viết sau buổi. Lý do: phần trả lời viết cần thời gian lập luận hơn cuối giờ học cho phép, còn thời hạn trước buổi kế tiếp giúp trợ giảng đọc bài trước khi lớp chuyển sang nội dung mới, và trùng với thời hạn nộp bù trong quy chế chuyên cần.
3. Sinh viên giữ bản sao thư mục bài làm trên thiết bị cá nhân đến hết học kỳ, vì bài kiểm tra giữa kỳ thực hành cho phép dùng bài làm TH01 đến TH05 của chính sinh viên (xem `05_Danh-gia/giua-ky/dac-ta-kiem-tra-giua-ky.md`) và vì bản sao là minh chứng khi đề nghị điều chỉnh kết quả.

Bài nộp đi qua kênh học tập dưới dạng tệp nén, không qua Git. Mẫu `gitignore-mau.txt` cố ý bỏ qua mọi tệp ảnh, kể cả hình kết quả, để kho mã cá nhân không bao giờ chứa ảnh người thật; hình kết quả vì vậy chỉ nằm trong tệp nén.

## 3. Nội dung được nộp và nội dung không bao giờ nộp

Mỗi bài nộp gồm bốn loại sản phẩm; danh sách cụ thể nằm ở mục "Sản phẩm cần nộp" trong README của từng bài.

| Loại | Ví dụ | Vì sao cần |
|---|---|---|
| Bảng số liệu (CSV) | EER, FNMR tại FMR = 0,1%, APCER, BPCER | con số đo được là bằng chứng bài đã chạy thật |
| Đồ thị (PNG) | DET, ROC, CMC, phân bố điểm | đồ thị cho thấy sinh viên hiểu hình dạng của sai số chứ không chỉ một con số |
| Mã nguồn (PY) | tệp khởi đầu đã hoàn thành các TODO | trợ giảng chạy lại được khi kết quả bất thường |
| Trả lời câu hỏi phân tích (MD) | 3 đến 5 câu, mỗi câu 3 đến 8 dòng | phần này là căn cứ đánh giá "chất lượng câu trả lời" |

**Không bao giờ nộp:** ảnh khuôn mặt, đoạn ghi âm, ảnh vân tay hay ảnh mống mắt của người thật; embedding; tệp `.pkl` của DeepFace; mẫu sinh trắc đã bảo vệ của người thật; trọng số mô hình; tập dữ liệu tải về. Lý do: đó là dữ liệu sinh trắc học hoặc dữ liệu dẫn xuất từ nó, và bài nộp đi qua nhiều máy và nhiều người. Hình minh hoạ lấy từ dữ liệu tổng hợp của bộ bài (vân tay, mống mắt tổng hợp) được phép nộp. Hình minh hoạ từ FVC hay CASIA chỉ đưa vào báo cáo khi README của bài yêu cầu, và không bao giờ dùng dữ liệu của sinh viên.

## 4. Quy trình kiểm tra hoàn thành trong buổi

Một buổi thực hành gồm 3 tiết: 135 phút học, 150 phút theo thời khoá biểu. Kiểm tra hoàn thành bắt đầu ngay khi có sinh viên làm xong và báo giảng viên hoặc trợ giảng; mỗi sinh viên mất khoảng 1 đến 2 phút. 30 phút cuối của buổi được dành cho những sinh viên chưa được kiểm tra. Lý do: nếu đợi đến cuối giờ mới kiểm tra cả lớp 40 đến 60 người, thời gian không đủ và sinh viên làm xong sớm phải ngồi chờ.

Mỗi lần kiểm tra:

1. Sinh viên mở bảng kết quả và đồ thị chính trên màn hình.
2. Người kiểm tra đối chiếu với danh sách "Tiêu chí hoàn thành" trong README của bài.
3. Người kiểm tra yêu cầu sinh viên giải thích ngắn một bước trong bài làm hoặc trả lời miệng một câu hỏi phân tích của bài, chọn ngẫu nhiên. Đây cũng là yêu cầu được mô tả ở mục 6.1 của quy chế chuyên cần. Câu trả lời bằng văn bản nộp sau, theo mục 2.
4. Người kiểm tra ghi "Đạt" hoặc "Chưa đạt" kèm một dòng nhận xét vào sổ theo dõi.

Sinh viên có mặt nhưng chưa đạt ở lần kiểm tra đầu được chỉ ra phần còn thiếu, làm tiếp và được kiểm tra lại **trong cùng buổi**, kể cả trong 30 phút cuối. Hết buổi mà vẫn chưa đạt thì kết quả của buổi đó là "Chưa đạt"; sinh viên vẫn nộp thư mục bài làm theo mục 2 để chuẩn bị cho bài sau và cho bài kiểm tra giữa kỳ. Lý do: kiểm tra hoàn thành là minh chứng về mức độ tham gia trong buổi học (mục 6.1 của `05_Danh-gia/chuyen-can/quy-che-chuyen-can.md`), nên chỉ bài làm trong buổi mới được ghi nhận.

Kiểm tra hoàn thành bù (ghi "B") chỉ dành cho sinh viên **vắng buổi thực hành có phép**, theo mục 5.1 của quy chế chuyên cần: sinh viên nộp sản phẩm của bài đó trước giờ bắt đầu của buổi học kế tiếp. Lý do: người vắng có lý do chính đáng không nên mất phần điểm Tích cực vì một việc ngoài khả năng của mình, còn người có mặt đã có trọn buổi học để hoàn thành.

## 5. Làm việc cặp đôi, làm việc nhóm và trích dẫn

TH01 đến TH09 là bài nộp cá nhân, nhưng sinh viên được khuyến khích ngồi theo cặp để gỡ lỗi cài đặt và thảo luận kết quả, vì kỹ năng giải quyết vấn đề cùng người khác là một phần của CLO4. Mỗi sinh viên tự chạy và tự nộp sản phẩm trên máy đang dùng. Riêng TH08, sinh viên thu dữ liệu tấn công trình diện theo nhóm 3 người (người trình diện, người thu nhận, người phân tích), vì một người không thể vừa cầm ảnh in trước camera vừa điều khiển chương trình; sau đó mỗi thành viên tự chạy đánh giá và nộp bài cá nhân. TH10 là bài duy nhất nộp theo nhóm, mỗi nhóm 3 đến 4 người; báo cáo ghi rõ phần việc của từng thành viên.

Khi dùng lại mã từ tài liệu, diễn đàn hay kho mã công khai, sinh viên ghi nguồn ngay tại chỗ trong chú thích mã (địa chỉ và ngày truy cập). Lý do: trợ giảng cần phân biệt phần sinh viên tự viết với phần sử dụng lại để đánh giá đúng mức hiểu bài.
