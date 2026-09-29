# Cam kết đạo đức và phiếu đồng ý sử dụng dữ liệu sinh trắc học trong thực hành

Học phần 04211 Bảo mật sinh trắc. Tài liệu gồm ba phần: bộ quy tắc ứng xử áp dụng cho mọi sinh viên (phần A), phiếu đồng ý tự nguyện cho sinh viên muốn dùng khuôn mặt hoặc giọng nói của chính bản thân (phần B), và biên bản xoá dữ liệu cuối buổi (phần C).

## Vì sao học phần cần văn bản này

Nhiều kỹ thuật trong học phần có tính lưỡng dụng (dual-use). Cùng một đoạn mã đưa tệp video quay sẵn vào chuỗi xử lý thay cho camera, ở TH08, vừa giúp ta hiểu và phòng chống tấn công chèn dữ liệu (injection attack), vừa có thể bị dùng để vượt qua bước xác thực khuôn mặt của ngân hàng. Điều này không còn là giả định: VnExpress ngày 26/06/2026 đưa tin một nhóm dùng mã độc chiếm quyền camera và thay hình ảnh trực tiếp bằng ảnh khuôn mặt lưu sẵn để mua bán hơn 1.000 tài khoản ngân hàng (https://vnexpress.net/can-thiep-camera-de-qua-mat-xac-thuc-sinh-trac-hoc-ban-1-000-tai-khoan-ngan-hang-5090374.html, truy cập 16/09/2026).

Dữ liệu sinh trắc học cũng khác mật khẩu ở một điểm căn bản: mật khẩu lộ thì đổi được, khuôn mặt lộ thì không. Luật Căn cước số 26/2023/QH15 định nghĩa "Sinh trắc học là những thuộc tính vật lý, đặc điểm sinh học cá biệt và ổn định của một người để nhận diện, phân biệt người này với người khác" (https://vanban.chinhphu.vn/?pageid=27160&docid=209628&classid=1&typegroupid=3). Chính tính "ổn định" đó làm cho một lần rò rỉ có hậu quả kéo dài suốt đời người bị lộ.

Căn cứ pháp lý chính cho việc xử lý dữ liệu trong phòng thực hành:

- Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15, ban hành 26/6/2025, có hiệu lực từ 01/01/2026, trong đó Điều 31 quy định về bảo vệ dữ liệu vị trí và dữ liệu sinh trắc học (https://vanban.chinhphu.vn/?pageid=27160&docid=214590&classid=1&typegroupid=3).
- Nghị định số 356/2025/NĐ-CP, ban hành 31/12/2025, có hiệu lực từ 01/01/2026, xếp dữ liệu sinh trắc học vào nhóm dữ liệu cá nhân nhạy cảm (https://vanban.chinhphu.vn/?pageid=27160&docid=216387).

Học phần áp dụng mức cẩn trọng cao hơn yêu cầu tối thiểu: không bắt buộc sinh viên nào cung cấp dữ liệu của bản thân, và mọi hoạt động đều có phương án dữ liệu công khai hoặc dữ liệu tổng hợp với giá trị học tập tương đương.

## Phần A. Bộ quy tắc ứng xử trong thực hành

Mỗi quy tắc đi kèm lý do, để sinh viên hiểu rõ nội dung cam kết chứ không chỉ tuân theo.

**A1. Chỉ thử nghiệm trên hệ thống do chính sinh viên dựng trong bài thực hành.** Sinh viên không thử kỹ thuật tấn công trình diện, chèn dữ liệu, trộn khuôn mặt hay giả mạo giọng nói lên ứng dụng ngân hàng, VNeID, hệ thống chấm công, điện thoại của người khác hay bất kỳ dịch vụ nào của bên thứ ba, kể cả khi "chỉ thử cho biết". Lý do: hành vi đó xâm phạm hệ thống không thuộc quyền của người thực hiện, có thể vi phạm pháp luật, và không cần thiết cho mục tiêu học tập vì chuỗi xử lý cục bộ đã cho thấy đủ cơ chế.

**A2. Bài tập chèn dữ liệu ở TH08 chỉ diễn ra trong phòng thực hành, có giảng viên giám sát.** Sinh viên không cài trình điều khiển camera ảo, không sửa ứng dụng di động và không mang mã của bài tập ra ngoài phạm vi buổi học. Lý do: ranh giới giữa bài tập có kiểm soát và công cụ tấn công chỉ nằm ở phạm vi sử dụng; giữ phạm vi hẹp là cách duy nhất để bài tập vẫn là bài tập.

**A3. Kỹ thuật trộn khuôn mặt và tạo khuôn mặt giả chỉ dùng ảnh từ tập dữ liệu công khai, và chỉ do giảng viên trình diễn minh hoạ.** Sinh viên không tạo ảnh hay video giả của bạn cùng lớp, giảng viên, người thân hay người nổi tiếng ngoài tập dữ liệu được giao. Lý do: ảnh giả của một người cụ thể gây tổn hại danh dự và có thể bị phát tán ngoài ý muốn ngay khi rời khỏi máy.

**A4. Xử lý dữ liệu sinh trắc học của người thật hoàn toàn cục bộ.** Không tải ảnh, giọng nói, embedding hay tệp `.pkl` của DeepFace lên Colab, Google Drive, dịch vụ nhận dạng trực tuyến, công cụ trò chuyện trực tuyến hay nhóm nhắn tin. Lý do: tải lên dịch vụ đám mây là chuyển dữ liệu nhạy cảm cho bên thứ ba, và người có dữ liệu không đồng ý với việc đó.

**A5. Không đưa dữ liệu sinh trắc học hoặc dữ liệu dẫn xuất vào Git.** Dùng tệp `gitignore-mau.txt` ngay từ lần tạo kho mã đầu tiên. Lý do: lịch sử Git giữ mọi phiên bản; xoá tệp ở lần cam kết sau không xoá được bản đã đẩy lên.

**A6. Tôn trọng quyền từ chối và quyền rút lại đồng ý của bạn cùng nhóm.** Không gây áp lực, không trêu chọc sinh viên chọn phương án dữ liệu công khai. Lý do: đồng ý chỉ có giá trị khi thật sự tự nguyện.

**A7. Tuân thủ điều kiện sử dụng của từng tập dữ liệu công khai.** SOCOFing chỉ dùng cho nghiên cứu phi thương mại, CASIA-IrisV4 cần đăng ký, LFW gồm ảnh người thật dù là người nổi tiếng. Sinh viên không phát tán lại các tập này. Lý do: người trong ảnh đồng ý với mục đích nghiên cứu, không đồng ý với việc bị lan truyền tiếp.

**A8. Báo ngay cho giảng viên khi phát hiện lỗ hổng thật** trong một hệ thống ngoài phòng thực hành (ví dụ nhận thấy một ứng dụng chấp nhận ảnh in). Không tự khai thác, không công bố. Lý do: công bố có trách nhiệm cho bên sở hữu thời gian khắc phục trước khi người xấu biết.

Vi phạm quy tắc A1 đến A4 được xử lý theo quy chế của Trường; giảng viên có quyền dừng quyền truy cập máy thực hành của sinh viên vi phạm trong buổi học để bảo vệ dữ liệu của người khác.

### Xác nhận cam kết (mọi sinh viên, ký ở buổi TH01)

Sinh viên ký tên dưới đây xác nhận đã đọc, hiểu bộ quy tắc A1 đến A8 và cam kết thực hiện trong suốt học phần.

Họ và tên: ........................................  Mã sinh viên: ....................  Lớp: ..........

Chữ ký: ........................  Ngày: ...../...../.........

## Phần B. Phiếu đồng ý tự nguyện sử dụng khuôn mặt hoặc giọng nói của bản thân sinh viên

**Không bắt buộc.** Sinh viên không ký phiếu này vẫn hoàn thành đầy đủ mọi bài thực hành bằng dữ liệu công khai hoặc dữ liệu tổng hợp do giảng viên chuẩn bị; lựa chọn đó không ảnh hưởng đến điểm chuyên cần, điểm kiểm tra giữa kỳ hay bất kỳ đánh giá nào khác của học phần.

### B1. Thông tin về việc xử lý dữ liệu

| Nội dung | Cam kết của học phần |
|---|---|
| Loại dữ liệu | ảnh hoặc đoạn video ngắn khuôn mặt; đoạn ghi âm giọng nói ngắn (tuỳ ô được đánh dấu ở B2) |
| Mục đích duy nhất | thực hiện bài thực hành được đánh dấu ở B2; không dùng cho mục đích khác, không dùng để nhận dạng sinh viên ngoài bài thực hành |
| Nơi xử lý | máy tính của phòng thực hành hoặc máy cá nhân của chính sinh viên, không kết nối dịch vụ nhận dạng trực tuyến, không tải lên đám mây |
| Tên tệp | mã giả danh do trợ giảng cấp (ví dụ P07), không chứa họ tên hay mã sinh viên |
| Người được tiếp cận | chính sinh viên, thành viên nhóm được sinh viên cho phép, giảng viên và trợ giảng trong buổi học |
| Thời hạn lưu | đến hết buổi thực hành tương ứng; xoá toàn bộ ảnh, âm thanh, embedding, tệp `.pkl` và mẫu sinh trắc đã bảo vệ trước khi rời phòng, có biên bản ở phần C |
| Kết quả được giữ lại | chỉ bảng số liệu và đồ thị tổng hợp (EER, APCER, BPCER), không chứa ảnh hay giọng nói |
| Quyền của sinh viên | rút lại đồng ý bất cứ lúc nào, kể cả giữa buổi, bằng lời nói với trợ giảng; dữ liệu được xoá ngay, sinh viên chuyển sang dữ liệu công khai mà không bị trừ điểm |
| Người chịu trách nhiệm | TS. Nguyễn An Khương, giảng viên học phần |

### B2. Lựa chọn của sinh viên

Sinh viên đánh dấu từng ô một cách độc lập; không đánh dấu nghĩa là không đồng ý.

| Hoạt động | Dữ liệu | Đồng ý |
|---|---|---|
| TH04, TH05: thêm ảnh khuôn mặt của bản thân vào tập thử xác minh và định danh | 3 đến 5 ảnh khuôn mặt | [ ] |
| TH06: ghi âm giọng nói của bản thân để thử xác minh người nói | 3 đến 5 câu, mỗi câu khoảng 5 giây | [ ] |
| TH08: làm mẫu trình diện thật và mẫu tấn công bằng ảnh in, màn hình phát lại khuôn mặt của bản thân | ảnh, video ngắn khuôn mặt | [ ] |
| TH08: tham gia bài thử cơ chế thách thức - phản hồi (challenge-response) trước camera của máy thực hành | video trực tiếp, không lưu | [ ] |
| TH10: đăng ký khuôn mặt của bản thân vào hệ thống của nhóm | 3 đến 5 ảnh khuôn mặt | [ ] |

### B3. Xác nhận

Sinh viên ký tên dưới đây xác nhận đã được giải thích về mục đích, phạm vi, thời hạn xử lý và quyền rút lại đồng ý; biết rằng có thể chọn dữ liệu công khai mà không bị ảnh hưởng đến kết quả học tập; và tự nguyện đồng ý với các ô đã đánh dấu ở mục B2.

Họ và tên: ........................................  Mã sinh viên: ....................  Lớp: ..........

Mã giả danh được cấp: ..........

Chữ ký sinh viên: ........................  Ngày: ...../...../.........

Giảng viên hoặc trợ giảng tiếp nhận: ........................  Chữ ký: ........................

Phiếu bản giấy do giảng viên lưu giữ riêng, không chụp, không số hoá lên hệ thống chung, vì phiếu chứa đồng thời họ tên và mã giả danh.

## Phần C. Biên bản xoá dữ liệu cuối buổi

Trợ giảng cùng sinh viên kiểm tra trực tiếp trên máy trước khi sinh viên rời phòng. Kiểm tra bằng mắt không đủ, vì embedding và tệp `.pkl` không phải là ảnh nên dễ bị bỏ sót.

| Mục kiểm tra | Cách kiểm tra | Đã xoá |
|---|---|---|
| Ảnh, video, âm thanh gốc | thư mục `du-lieu-rieng/`, thư mục Tải xuống, Thùng rác | [ ] |
| Tệp `.pkl` (kho embedding của `DeepFace.find`) và `.pkl.ldsa` (tệp chữ ký số LightDSA đi kèm kho đó) | tìm theo phần mở rộng trong thư mục tham chiếu | [ ] |
| Bộ đệm embedding | thư mục `cache-embedding/`, tệp `.npz`, `.npy` | [ ] |
| Mẫu đã bảo vệ, kho mẫu, nhật ký có mã giả danh | thư mục `ket-qua/` của TH09, TH10 | [ ] |
| Thùng rác của hệ điều hành đã được làm trống | mở Thùng rác | [ ] |

Buổi thực hành: TH.....  Mã giả danh: ..........

Sinh viên: ........................  Trợ giảng: ........................  Thời điểm: .....h..... ngày ...../...../.........
