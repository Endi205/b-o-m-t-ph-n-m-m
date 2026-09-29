# TH01: Cài đặt môi trường và tự tính các chỉ số đánh giá hiệu năng

| Buổi | Bài giảng liên quan | CLO | Thời lượng | Dữ liệu |
|---|---|---|---|---|
| Buổi 1 | B01: Kiến trúc và bảo mật hệ thống sinh trắc | CLO1, CLO4 (theo đề cương, tuần 1) | 3 tiết: 135 phút học, 150 phút theo thời khoá biểu | tệp điểm tổng hợp `data/scores_th01.csv` (có sẵn) |

Theo đề cương, tuần 1 gắn với CLO1 và CLO4. Các phép tính FMR, FNMR, EER của hôm nay là công cụ đo mà các bạn dùng lại suốt học phần, kể cả khi rèn kỹ năng thiết kế hệ thống của CLO2 từ Buổi 2.

Bài làm cá nhân: mỗi sinh viên tự chạy và tự nộp, dù được khuyến khích ngồi theo cặp để gỡ lỗi (xem `00_moi-truong/quy-uoc-nop-bai.md`, mục 5).

## Mục tiêu

Sau buổi thực hành, sinh viên có thể:

1. Tự cài đặt hàm tính tỷ lệ so khớp sai (false match rate, FMR) và tỷ lệ không khớp sai (false non-match rate, FNMR) theo ngưỡng quyết định, cho cả điểm tương đồng lẫn điểm khoảng cách, rồi đối chiếu kết quả với pyeer (thư viện Python mã nguồn mở chuyên tính các chỉ số hiệu năng sinh trắc), bảo đảm tỷ lệ lỗi cân bằng (equal error rate, EER) tự tính lệch không quá 0,5 điểm phần trăm. (CLO1)
2. Vẽ và đọc đường cong DET (detection error trade-off), đường cong ROC (receiver operating characteristic), phân bố điểm cặp cùng người và cặp khác người; giải thích vì sao hai hệ thống có EER gần bằng nhau vẫn có thể khác nhau rất xa tại FMR = 0,1%. (CLO1)
3. Tính số lần so khớp sai kỳ vọng khi chuyển từ xác minh 1:1 sang định danh 1:N, từ đó giải thích vì sao ngưỡng tốt cho xác minh lại không đủ cho tìm kiếm trên cơ sở dữ liệu lớn. (CLO1)
4. Cùng bạn ngồi cạnh kiểm tra môi trường chuẩn của học phần, đọc báo cáo kiểm tra môi trường và tự phân loại lỗi nào cần xử lý ngay, lỗi nào xử lý trước bài sau. (CLO4)

## Liên hệ với bài giảng B01

Bài giảng B01 định nghĩa FMR, FNMR, EER, đường cong ROC và DET trên giấy. Buổi thực hành biến các định nghĩa đó thành mã, vì chỉ khi tự đếm từng cặp bị chấp nhận hay từ chối, ta mới thấy những chi tiết mà công thức giấu đi: điểm bằng ngưỡng thì xếp vào đâu, EER là một điểm hay một khoảng, vì sao với 10 cặp khác người ở Hoạt động 2 của B01 thì FMR chỉ nhận các giá trị là bội số của 10%. Tệp `bio_metrics.py` viết hôm nay được dùng lại ở TH03, TH04, TH05, TH06, TH07, TH09 và TH10, và phạm vi bài kiểm tra giữa kỳ thực hành bao gồm buổi này.

Ba hệ thống A, B, C của bài thực hành là dữ liệu tổng hợp riêng của TH01, không trùng với các hệ thống minh hoạ trong bài giảng; khi thấy EER khác với ví dụ trên slide, các bạn không cần lo tệp dữ liệu bị sai.

## Chuẩn bị

Buổi 1 làm trên máy phòng thực hành, nơi môi trường của học phần đã được cài sẵn; mục 5.1 của `00_moi-truong/huong-dan-cai-dat.md` hướng dẫn cách mở môi trường đó. Lý do: sinh viên chưa nhận được thư mục bài thực hành trước Buổi 1, và cài đặt lần đầu mất 20 đến 60 phút, dài hơn thời gian của cả phần làm bài. Sau Buổi 1, sinh viên nào muốn dùng máy cá nhân thì tải thư mục bài thực hành từ kênh học tập của lớp (giảng viên thông báo ở Buổi 1) và cài theo hướng dẫn cài đặt trước Buổi 2.

| Việc | Thời điểm | Ghi chú |
|---|---|---|
| Đọc mục 1 và mục 5.1 của `00_moi-truong/huong-dan-cai-dat.md` | đầu buổi | biết vì sao cả lớp dùng chung một môi trường ghim phiên bản |
| Đọc Jain, Ross, Nandakumar, Swearingen (2024), Chương 1 "Introduction" (tr. 1-50) | theo phần tự học của Buổi 1 trong dàn ý B01 | đọc kỹ phần về các loại lỗi và đánh giá hiệu năng |
| Ký phần A của `00_moi-truong/cam-ket-dao-duc-va-dong-y.md` | 10 phút đầu buổi | bắt buộc cho mọi sinh viên, vì các bài sau có dùng kỹ thuật tấn công |

Tệp điểm `data/scores_th01.csv` gồm ba hệ thống giả định A, B, C; mỗi hệ thống có 1.000 cặp cùng người và 10.000 cặp khác người. A và B cho điểm tương đồng (cao là giống), C cho điểm khoảng cách (thấp là giống). Dữ liệu được sinh bằng `data/make_scores.py` với hạt giống (seed) cố định 4211 cho bộ sinh số ngẫu nhiên, hoàn toàn tổng hợp, nên mọi máy có cùng tệp và cùng kết quả.

Bài này không cần trọng số mô hình và không cần mạng. Vì vậy các dòng [CẢNH BÁO] về trọng số DeepFace hay mô hình SpeechBrain trong báo cáo kiểm tra môi trường không ảnh hưởng đến TH01.

## Các bước thực hiện

Bảng dưới đây chia 135 phút học của buổi. Thời lượng từng bước là ước lượng cho sinh viên đã biết Python cơ bản; các bước làm bài phải xong trước 30 phút cuối, vì 30 phút đó dành cho kiểm tra hoàn thành những bạn còn lại.

| Phút | Việc |
|---|---|
| 0 đến 10 | giảng viên nêu mục tiêu và điểm dễ sai; ký phần A của bản cam kết |
| 10 đến 20 | Bước 1: kiểm tra môi trường |
| 20 đến 30 | Bước 2: tính tay |
| 30 đến 60 | Bước 3: TODO 1 |
| 60 đến 85 | Bước 4: TODO 2 đến TODO 6 |
| 85 đến 90 | Bước 5: TODO 7 |
| 90 đến 95 | Bước 6: chạy chương trình chính |
| 95 đến 105 | Bước 7: đọc đồ thị, TODO quy tắc số 3 |
| 105 đến 135 | kiểm tra hoàn thành cho những bạn chưa được kiểm tra |

Kiểm tra hoàn thành (check-off) bắt đầu ngay khi có sinh viên làm xong, không đợi đến phút 105.

**Bước 1. Kiểm tra môi trường.** Trong thư mục `00_moi-truong`, chạy `python preflight_check.py --nhanh`. Chế độ nhanh bỏ qua bước nhập thử TensorFlow, PyTorch và DeepFace, vốn có thể mất vài phút ở lần chạy đầu mà TH01 không cần. Dòng cuối của báo cáo, "Sẵn sàng cho TH01", tổng hợp đúng những gì bài này cần. Chỉ một dòng `[LỖI]` ở Python, numpy, scipy, matplotlib, setuptools, pyeer, phép tính numpy hoặc phép vẽ hình mới chặn TH01; khi gặp, các bạn báo trợ giảng để được chuyển máy. Mọi dòng `[LỖI]` khác và mọi dòng `[CẢNH BÁO]` không chặn TH01: các bạn ghi lại và xử lý theo mục 9 của hướng dẫn cài đặt trước bài được nêu trong dòng đó, vì một thư viện hỏng chỉ phát hiện ra giữa buổi TH04 sẽ tốn cả buổi đó. Giữ lại tệp `preflight-bao-cao.txt`.

**Bước 2. Làm bằng tay trước khi làm bằng máy.** Mở `test_bio_metrics.py`, đọc ví dụ gồm 4 điểm cùng người (0,9; 0,8; 0,7; 0,4) và 5 điểm khác người (0,1; 0,2; 0,3; 0,6; 0,75). Trên giấy, tính FMR và FNMR tại ngưỡng 0,5, tại ngưỡng 0,7 và tại ngưỡng 0,75, rồi tìm EER. Hai ngưỡng sau trùng đúng một điểm, nên các bạn phải áp dụng quy ước "điểm bằng ngưỡng thì chấp nhận". Lý do: con số tính tay là đáp án để kiểm tra mã; nếu chưa tự tính được, ta sẽ không biết mã sai ở đâu.

**Bước 3. Hoàn thành `error_rates` (TODO 1).** Quy ước của cả học phần: với điểm tương đồng, chấp nhận khi điểm lớn hơn hoặc bằng ngưỡng. Phần đổi dấu điểm khoảng cách và phần dựng danh sách ngưỡng đã viết sẵn; việc của các bạn là sắp xếp điểm rồi dùng `np.searchsorted` để đếm. Lý do không dùng vòng lặp lồng nhau: với 11.000 điểm và khoảng 11.000 ngưỡng, vòng lặp cần khoảng 1,2 x 10^8 phép so sánh và chạy mất vài phút, còn cách sắp xếp rồi tìm kiếm nhị phân chạy dưới một giây. Chạy `python test_bio_metrics.py`; năm nhóm kiểm thử của `error_rates` phải ĐẠT, trong đó có hai nhóm "điểm bằng ngưỡng" sẽ báo ngay nếu mã chấp nhận theo `>` thay vì `>=`.

**Bước 4. Cài đặt `eer`, `fnmr_at_fmr`, `decidability`, `roc_auc`, `fpir_from_fmr` (TODO 2 đến TODO 6).** Docstring của từng hàm ghi đặc tả đầy đủ, gồm công thức nội suy của `eer_interp`, loại phương sai của chỉ số phân tách d' (decidability index) và cách sắp điểm trước khi tính diện tích dưới đường ROC (area under the curve, AUC). EER được lấy tại ngưỡng mà |FMR - FNMR| nhỏ nhất, bằng trung bình hai tỷ lệ tại đó; pyeer cũng làm như vậy, nên hai kết quả so sánh được. Hàm `fnmr_at_fmr` trả lời câu hỏi mà ngân hàng thực sự đặt ra: cố định FMR trước, rồi hỏi hệ thống từ chối nhầm bao nhiêu. Chạy lại kiểm thử sau mỗi hàm. Tổng số phép kiểm thử luôn là 21, kể cả khi còn hàm chưa viết, nên các bạn theo dõi được tiến độ qua tử số.

**Bước 5. Cài đặt `_probit` cho trục DET (TODO 7).** Trục DET dùng độ lệch chuẩn hoá (normal deviate, còn gọi là thang probit) thay cho thang tuyến tính, vì khi điểm gần phân phối chuẩn, đường DET gần như thẳng và các vùng lỗi nhỏ (0,1%, 0,01%) chiếm đủ chỗ để nhìn thấy. Sau bước này, `python test_bio_metrics.py` phải báo 21/21.

**Bước 6. Chạy chương trình chính.** Trong thư mục TH01, chạy `python th01_main.py --ma-sv <mã sinh viên>`. Chương trình tính các chỉ số cho A, B, C, gọi pyeer để đối chiếu, rồi ghi vào thư mục `ket-qua/` bảng `TH01_<mã sinh viên>_bang-ket-qua.csv` và ba hình `TH01_<mã sinh viên>_phan-bo-diem.png`, `TH01_<mã sinh viên>_det.png`, `TH01_<mã sinh viên>_roc.png`. Tên tệp đã đúng quy ước nộp bài, nên các bạn chép thẳng vào thư mục nộp. Nếu dòng nào báo CHƯA ĐẠT, chương trình dừng với mã lỗi 1: quay lại bước 3.

**Bước 7. Đọc đồ thị và hoàn thành TODO quy tắc số 3.** Mở hình DET, so sánh ba hệ thống ở vùng FMR nhỏ; mở hình phân bố điểm (trục tung thang log) để tìm nguyên nhân. Sau đó làm phần TODO cuối trong `th01_main.py` (câu hỏi phân tích 3). Phần trả lời viết cho năm câu hỏi được làm sau buổi học, vì cần thời gian lập luận cẩn thận hơn 10 phút cuối giờ.

**Bước 8. Kiểm tra hoàn thành.** Ngay khi xong bước 7, các bạn báo trợ giảng. Mỗi lần kiểm tra mất khoảng 1 đến 2 phút: trợ giảng đối chiếu tiêu chí hoàn thành ở cuối tệp này, rồi yêu cầu giải thích một bước trong bài làm hoặc trả lời miệng một câu hỏi phân tích.

Mẹo: các tệp `.py` của bộ bài có dấu `# %%` chia ô, nên có thể mở và chạy từng ô trong VS Code như notebook.

## Sản phẩm cần nộp

> **Nộp qua kho cá nhân.** Đặt các tệp dưới đây vào thư mục bài `labNN/` của kho `sinhtrac-<MSSV>`, giữ nguyên tên do chương trình ghi ra trong `ket-qua/`; phần trả lời câu hỏi phân tích viết trong `bao-cao.md` của thư mục bài, thay cho tệp `_tra-loi.md`. Danh mục chính xác nằm trong `README.md` của thư mục bài trong kho và trong đề bài trên LMS; cách nộp theo `00_moi-truong/00_Quy-uoc-kho-ca-nhan_04211 (bản mới nhất)`.

Theo quy ước trong `00_moi-truong/quy-uoc-nop-bai.md`: sản phẩm được trình ngay trên máy khi kiểm tra hoàn thành trong buổi; sau đó thư mục `<ma-sinh-vien>_bmst04211/TH01/` được nén và tải lên kênh học tập của lớp trước giờ bắt đầu buổi học kế tiếp. Thư mục gồm:

1. `preflight-bao-cao.txt`, có dòng "Sẵn sàng cho TH01: có" (lỗi còn lại, nếu có, kèm kế hoạch xử lý trong tệp trả lời).
2. `bio_metrics.py` đã hoàn thành, `python test_bio_metrics.py` đạt 21/21.
3. `th01_main.py` đã hoàn thành TODO quy tắc số 3, để trợ giảng xem được phần này.
4. `TH01_<ma-sinh-vien>_bang-ket-qua.csv` do `th01_main.py` sinh ra: EER tự tính, EER nội suy, EER của pyeer, chênh lệch (điểm phần trăm, phải không quá 0,5), FNMR tại FMR = 1% và 0,1%, d', AUC cho ba hệ thống.
5. `TH01_<ma-sinh-vien>_det.png` do `th01_main.py` sinh ra: đường DET của ba hệ thống trên cùng một hình, có đánh dấu điểm EER.
6. `TH01_<ma-sinh-vien>_tra-loi.md`: trả lời các câu hỏi phân tích dưới đây.

## Câu hỏi phân tích

1. Hệ thống A và hệ thống B có EER chênh nhau rất ít. Dựa vào đường DET và bảng kết quả, nếu một ngân hàng yêu cầu FMR không quá 0,1% thì nên chọn hệ thống nào, và vì sao EER không đủ để quyết định? Hình phân bố điểm cho biết nguyên nhân gì ở hệ thống có đuôi xấu?
2. Hệ thống C dùng điểm khoảng cách. Nếu quên đổi chiều (dùng `higher_is_better=True`), EER tính ra bằng bao nhiêu? Giải thích con số đó.
3. Giả sử một hệ thống không mắc lần so khớp sai nào trên 10.000 cặp khác người. "Quy tắc số 3" (rule of three) nói rằng khi quan sát 0 lỗi trên N phép thử độc lập, cận trên tin cậy 95% của tỷ lệ lỗi xấp xỉ 3/N, vì (1 - p)^N = 0,05 cho p xấp xỉ 3/N. Tính cận này, hoàn thành TODO cuối trong `th01_main.py`, và cho biết vì sao "0 lỗi" không có nghĩa là "FMR bằng 0".
4. Thông tư 50/2024/TT-NHNN, Điều 11 khoản 5, yêu cầu so khớp khuôn mặt có tỷ lệ từ chối sai dưới 5% khi tỷ lệ chấp nhận sai dưới 0,01% (https://vanban.chinhphu.vn/?pageid=27160&docid=211772&classid=1&orggroupid=4). Với 10.000 cặp khác người trong tệp, có kiểm chứng được một hệ thống đạt FMR 0,01% hay không? Dùng quy tắc số 3 ở câu 3, cần tối thiểu bao nhiêu cặp khác người?
5. Một lớp có 50 sinh viên. Có bao nhiêu cặp khác người khi so từng cặp sinh viên với nhau? Với FMR = 1%, kỳ vọng bao nhiêu cặp so khớp sai? Chuyển sang tìm kiếm 1:N trên cơ sở dữ liệu 100 triệu bản ghi với FMR = 0,01%: kỳ vọng bao nhiêu kết quả sai cho mỗi lần tìm (giả thiết các phép so khớp độc lập)?

## Tiêu chí hoàn thành

- [ ] Báo cáo kiểm tra môi trường có dòng "Sẵn sàng cho TH01: có"; các dòng `[LỖI]` và `[CẢNH BÁO]` còn lại đã được ghi kèm bài cần xử lý.
- [ ] `test_bio_metrics.py` đạt 21/21 trên máy sinh viên đang dùng.
- [ ] `th01_main.py --ma-sv <mã sinh viên>` chạy hết, cả ba hệ thống ĐẠT (chênh lệch EER với pyeer không quá 0,5 điểm phần trăm), tệp kết quả mang đúng mã sinh viên.
- [ ] Hình DET có trục chuẩn hoá, ba đường, nhãn trục đọc được.
- [ ] Sinh viên giải thích đúng một bước trong bài làm hoặc trả lời miệng đúng một câu hỏi phân tích do trợ giảng chọn.
- [ ] Đã ký phần A của bản cam kết đạo đức.

## Mở rộng cho sinh viên khá

- Viết hàm tính khoảng tin cậy 95% cho EER bằng bootstrap: lấy mẫu lại cặp cùng người và cặp khác người 1.000 lần, báo cáo phân vị 2,5% và 97,5%. So sánh độ rộng khoảng với chênh lệch EER giữa A và B, rồi kết luận chênh lệch đó có ý nghĩa hay không.
- Thêm vào DET đường "chi phí phát hiện" với chi phí so khớp sai gấp 100 lần chi phí từ chối sai, và tìm ngưỡng tối thiểu hoá chi phí kỳ vọng (NPTEL, đơn vị "Comparing systems, EER, cost functions, security vs convenience").
- Đọc tài liệu hướng dẫn về đường cong DET trong học liệu của C. Busch (https://christoph-busch.de/teaching-biometric-systems.html, truy cập 16/09/2026) và kiểm tra đồ thị vừa vẽ có theo đúng khuyến nghị về thang trục hay không.

## Tài liệu tham khảo

- Jain, A. K., Ross, A. A., Nandakumar, K., & Swearingen, T. (2024). Introduction to Biometrics (2nd ed.). Springer, Chương 1 "Introduction", tr. 1-50. https://doi.org/10.1007/978-3-031-61675-4
- ISO/IEC 19795-1:2021, Information technology: Biometric performance testing and reporting, Part 1. https://www.iso.org/standard/73515.html
- NPTEL "Biometrics" (P. Gupta, IIT Kanpur), các đơn vị "Identification vs verification, thresholds, FAR/FRR", "Hypothesis testing, ROC/DET", "Comparing systems, EER, cost functions". https://nptel.ac.in/courses/106104119
- Thư viện pyeer 0.5.6 trên PyPI: https://pypi.org/project/pyeer/0.5.6/
