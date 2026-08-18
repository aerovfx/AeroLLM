// AI Thực Chiến Documentation Web App Controller
const docsData = {
  "tuan-01-intro": {
    "title": "Tuần 1: Quy định & Thiết lập",
    "file": "docs/training/tuan-01-intro.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 1: Quy định & Thiết lập"],
    "content": "# Tuần 1: Quy định & Thiết lập Môi trường\n\nChào mừng bạn đến với tuần đầu tiên của chương trình huấn luyện AI thực chiến! Tuần này chúng ta tập trung vào việc hiểu rõ quy chế thi và cài đặt môi trường.\n\n## Quy định kỹ thuật phòng thi\n- Mỗi đội cần chuẩn bị **02 máy tính** (ghi hình màn hình) và **02 điện thoại** (giám sát trực tiếp và ghi hình phụ).\n- Sử dụng Google Colab hoặc card đồ họa cục bộ để thiết lập môi trường Python/PyTorch.\n\n## Hướng dẫn đăng nhập Suno & Lấy OTP\n- Đăng nhập qua Microsoft Account được cung cấp bởi Ban Tổ Chức.\n- Dùng công cụ OTP generator trên ứng dụng web để lấy mã 2FA xác thực nhanh chóng.\n"
  },
  "tuan-02-synthetic-data": {
    "title": "Tuần 2: Kỹ thuật Tạo Dữ liệu Tổng hợp",
    "file": "docs/training/tuan-02-synthetic-data.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 2: Kỹ thuật Tạo Dữ liệu Tổng hợp"],
    "content": "# Tuần 2: Kỹ thuật Tạo Dữ liệu Tổng hợp (Synthetic Data)\n\nDữ liệu chất lượng cao quyết định sự thông minh của mô hình. Trong tuần này, chúng ta sẽ học cách tự sinh tập dữ liệu hướng dẫn bằng LLM.\n\n## Các thuật toán sinh dữ liệu phổ biến\n1. **Self-Instruct (Alpaca):** Sử dụng mô hình lớn tự sinh câu lệnh (prompt) và câu trả lời tương ứng từ một tập hạt giống nhỏ.\n2. **Evol-Instruct (WizardLM):** Nâng cấp độ phức tạp của câu lệnh theo chiều sâu hoặc chiều rộng bằng cách ra lệnh cho LLM sửa câu lệnh cũ khó hơn.\n3. **Magpie:** Tận dụng trực tiếp khả năng sinh câu lệnh tự nhiên của các mô hình Instruct để trích xuất hội thoại chất lượng lớn.\n4. **Persona-driven:** Tạo ra 1 tỷ nhân vật giả lập để sinh các góc nhìn đa chiều của dữ liệu web.\n"
  },
  "tuan-03-data-filtering": {
    "title": "Tuần 3: Lọc dữ liệu & Pha trộn",
    "file": "docs/training/tuan-03-data-filtering.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 3: Lọc dữ liệu & Pha trộn"],
    "content": "# Tuần 3: Lọc dữ liệu & Pha trộn (Data Mix Optimization)\n\nCó được dữ liệu tổng hợp chưa đủ, ta cần lọc bỏ rác và tối ưu hóa tỷ lệ pha trộn giữa các miền dữ liệu khác nhau.\n\n## Các bước xử lý dữ liệu thô\n- **Lọc trùng lặp (Deduplication):** Sử dụng thuật toán MinHash LSH hoặc so khớp nhúng vector để loại bỏ các prompt giống nhau.\n- **Lọc an toàn (Toxicity Filtering):** Loại bỏ các mẫu phản hồi chứa từ ngữ thô tục, bạo lực bằng mô hình phân loại nhỏ.\n- **Pha trộn dữ liệu (Data Mix):** Tỷ lệ pha trộn tối ưu giữa code, toán học, đối thoại và tài liệu web chung (ví dụ: 30% code, 20% toán, 50% văn bản chung).\n"
  },
  "tuan-04-model-tokenizer": {
    "title": "Tuần 4: Lựa chọn Mô hình & Tokenizer",
    "file": "docs/training/tuan-04-model-tokenizer.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 4: Lựa chọn Mô hình & Tokenizer"],
    "content": "# Tuần 4: Lựa chọn Mô hình & Tokenizer\n\nViệc lựa chọn kiến trúc mô hình nền tảng (Base model) và cấu hình Tokenizer ảnh hưởng lớn đến chi phí huấn luyện.\n\n## Lựa chọn Base Model\n- **Dòng SmolLM2 (135M, 360M, 1.7B):** Lý tưởng cho các thử nghiệm ablation nhanh và các đội có ít GPU.\n- **Dòng Llama-3 / Qwen-2.5 (1B, 3B, 7B):** Cấu hình tiêu chuẩn cho kết quả chất lượng cao trên các bảng xếp hạng (benchmarks).\n\n## Cấu hình Tokenizer\n- Sử dụng bảng từ vựng (Vocabulary size) lớn (ví dụ 100k token) để mã hóa tiếng Việt tiết kiệm dung lượng ngữ cảnh.\n- Tránh tình trạng Tokenizer bị phân mảnh ký tự UTF-8.\n"
  },
  "tuan-05-sft-training": {
    "title": "Tuần 5: Tinh chỉnh Giám sát (SFT)",
    "file": "docs/training/tuan-05-sft-training.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 5: Tinh chỉnh Giám sát (SFT)"],
    "content": "# Tuần 5: Tinh chỉnh Giám sát (Supervised Fine-Tuning - SFT)\n\nBiến đổi mô hình cơ sở thành một trợ lý biết nghe lời thông qua SFT chất lượng cao.\n\n## Cấu hình Framework Axolotl / TRL\n- **Prompt Template:** Áp dụng mẫu trò chuyện chuẩn (ChatML, Llama-3 Instruct template).\n- **Siêu tham số SFT:**\n  - `learning_rate`: Đặt trong khoảng `2e-5` cho Full FT, hoặc `1e-4` cho LoRA.\n  - `warmup_ratio`: Thường chọn `0.03` (3% số bước đầu tiên tăng dần tốc độ học).\n  - `packing`: Gộp các câu thoại ngắn vào cùng một độ dài context tối đa (ví dụ 2048) để tối đa hóa hiệu năng GPU.\n"
  },
  "tuan-06-continued-pretraining": {
    "title": "Tuần 6: Tiền Huấn luyện Bổ sung",
    "file": "docs/training/tuan-06-continued-pretraining.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 6: Tiền Huấn luyện Bổ sung"],
    "content": "# Tuần 6: Tiền Huấn luyện Bổ sung (Continued Pre-training)\n\nKhi bạn muốn nhồi nhét một lượng lớn tri thức miền mới (ví dụ luật pháp Việt Nam, y học cổ truyền) vào mô hình cơ sở trước khi làm SFT.\n\n## Kỹ thuật thực hiện\n- Huấn luyện tự hồi quy (Next-token prediction) trên lượng lớn văn bản thô chưa gắn nhãn.\n- Cần đặt tốc độ học thấp hơn tiền huấn luyện gốc (khoảng `1e-5` đến `5e-5`).\n- Sử dụng hàm suy giảm tốc độ học dạng Cosine (Cosine learning rate scheduler).\n"
  },
  "tuan-07-distributed": {
    "title": "Tuần 7: Cấu hình Huấn luyện Phân tán",
    "file": "docs/training/tuan-07-distributed.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 7: Cấu hình Huấn luyện Phân tán"],
    "content": "# Tuần 7: Cấu hình Huấn luyện Phân tán (Distributed Training)\n\nĐể huấn luyện các mô hình lớn trên 2, 4 hoặc 8 GPU song song mà không bị tràn bộ nhớ VRAM.\n\n## Các công nghệ song song hóa\n1. **DeepSpeed ZeRO-3:** Phân tán trọng số mô hình, gradient và trạng thái bộ tối ưu hóa trên toàn bộ các GPU.\n2. **FSDP (Fully Sharded Data Parallel):** Kỹ thuật tích hợp sẵn trong PyTorch tương tự DeepSpeed, cấu hình mượt mà.\n3. **LoRA / QLoRA:** Đóng băng mô hình nền tảng, chỉ cập nhật adapter để tiết kiệm 70% bộ nhớ đồ họa.\n"
  },
  "tuan-08-preference-opt": {
    "title": "Tuần 8: Tối ưu Sở thích (DPO/ORPO)",
    "file": "docs/training/tuan-08-preference-opt.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 8: Tối ưu Sở thích (DPO/ORPO)"],
    "content": "# Tuần 8: Tối ưu Sở thích (DPO/ORPO)\n\nCăn chỉnh hành vi để mô hình trả lời lịch sự, hữu ích và tránh độc hại mà không cần huấn luyện mô hình phần thưởng phức tạp.\n\n## Kỹ thuật DPO (Direct Preference Optimization)\n- Sử dụng cặp dữ liệu phản hồi ưa thích (Chosen) và phản hồi bị từ chối (Rejected).\n- Trực tiếp tối ưu hóa xác suất của mô hình SFT để tăng xác suất chọn câu Chosen và giảm xác suất chọn câu Rejected.\n\n## Kỹ thuật ORPO (Odds Ratio Preference Optimization)\n- Gộp pha SFT và pha DPO thành một lượt huấn luyện duy nhất, giúp tối ưu hóa bộ nhớ và tăng tốc độ hội tụ mô hình.\n"
  },
  "tuan-09-evaluation": {
    "title": "Tuần 9: Đánh giá & Tránh Nhiễm dữ liệu",
    "file": "docs/training/tuan-09-evaluation.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 9: Đánh giá & Tránh Nhiễm dữ liệu"],
    "content": "# Tuần 9: Đánh giá & Tránh Nhiễm dữ liệu (Evaluation & Contamination)\n\nLàm sao biết mô hình của bạn đã cải tiến chất lượng và câu trả lời đáng tin cậy?\n\n## Các công cụ đánh giá tự động\n- **lm-evaluation-harness:** Bộ công cụ mã nguồn mở đánh giá mô hình trên hàng chục benchmark học thuật (MMLU, GSM8K, ARC).\n- **LLM-as-a-judge:** Sử dụng mô hình lớn mạnh (như GPT-4, Gemini Pro) để chấm điểm câu trả lời của mô hình bạn dựa trên Rubric quy định.\n\n## Phòng tránh nhiễm dữ liệu (Contamination)\n- Quét dữ liệu train của bạn để đảm bảo không chứa các câu hỏi thi hoặc đáp án của tập test.\n- Nếu bị phát hiện nhiễm dữ liệu, điểm số bài thi của bạn sẽ bị hủy bỏ.\n"
  },
  "tuan-10-model-submission": {
    "title": "Tuần 10: Đóng gói & Nộp Mô hình",
    "file": "docs/training/tuan-10-model-submission.md",
    "breadcrumbs": ["Luyện Tập 10 Tuần", "Tuần 10: Đóng gói & Nộp Mô hình"],
    "content": "# Tuần 10: Đóng gói & Nộp Mô hình\n\nTuần cuối cùng tập trung hoàn thiện gói sản phẩm để nộp lên Hugging Face Hub của Ban tổ chức.\n\n## Đóng gói kỹ thuật\n- Chuyển đổi trọng số sang định dạng chuẩn `.safetensors`.\n- Đảm bảo các tệp phụ trợ như `config.json`, `generation_config.json`, `tokenizer.json` được định cấu hình chính xác.\n\n## Viết Thẻ Mô hình (Model Card - README.md)\n- Trình bày rõ: Mô tả mô hình, cấu hình siêu tham số, dữ liệu huấn luyện, điểm số benchmark và các giới hạn được phát hiện.\n- Nộp liên kết bài viết và mã nguồn huấn luyện lên máy chủ chấm thi.\n"
  },

  "round-2": {
    "title": "Vòng Chung Khảo",
    "file": "docs/round-2.md",
    "breadcrumbs": [
      "Vòng Chung Khảo"
    ],
    "content": "## 🗃️   Hướng dẫn sử dụng API\n\n7 items\n\n## 🗃️   VibeCoding\n\n4 items\n\n## 🗃️   Tham chiếu API\n\n10 items\n\n## 🗃️   Tips và Tricks Thực Chiến\n\n3 items\n\n## 🗃️   Sử dụng với Google GenAI\n\n2 items\n\n## 📄️   Quy định & Hướng dẫn kỹ thuật\n\nBAN TỔ CHỨC CUỘC THI AI THỰC CHIẾN\n\n## 📄️   Hướng dẫn đăng nhập Suno\n\nTài liệu này hướng dẫn chi tiết cách đăng nhập vào Suno bằng tài khoản do Ban Tổ Chức (BTC) cung cấp.\n\n## 📄️   Công cụ OTP\n\nCông cụ này tạo Mật khẩu một lần dựa trên thời gian (TOTP) từ một secret key, tương thích với Google Authenticator, Microsoft Authenticator, và các ứng dụng 2FA tiêu chuẩn khác.\n"
  },
  "regulations-and-technical-guidelines": {
    "title": "Quy định & Hướng dẫn kỹ thuật",
    "file": "docs/round-2/regulations-and-technical-guidelines.md",
    "breadcrumbs": [
      "Vòng Chung Khảo",
      "Quy định & Hướng dẫn kỹ thuật"
    ],
    "content": "# Quy định & Hướng dẫn kỹ thuật — Vòng Chung khảo (Thi trực tuyến)\n\nBAN TỔ CHỨC CUỘC THI AI THỰC CHIẾN\n\n## Quy định và Hướng dẫn kỹ thuật cho các đội tham gia​\n\nSau khi Ban tổ chức/Hội đồng giám khảo duyệt hồ sơ tham dự và quyết định các đội qua vòng Sơ loại, các đội tham gia vòng thi Chung khảo (hình thức thi trực tuyến) phải tuân thủ các yêu cầu hình thức và kỹ thuật sau đây.\n\nLưu ý: mọi đội tham gia chịu trách nhiệm chuẩn bị đầy đủ thiết bị và môi trường theo hướng dẫn để đảm bảo tính công bằng, minh bạch và trung thực trong suốt thời gian thi.\n\n### 1. Không gian thi​\n\n- Mỗi đội tự chuẩn bị vị trí thi đảm bảo không gian cho 3 thí sinh.\n- Không gian thi phải yên tĩnh, không bị ảnh hưởng bởi tiếng ồn bên ngoài.\n- Tuyệt đối không xuất hiện người thứ tư trong khung hình/không gian thi trong suốt thời gian dự thi.\n- Ưu tiên sử dụng phòng làm việc có đủ ánh sáng và kết nối Internet băng thông rộng.\n\n### 2. Thiết bị kỹ thuật (bắt buộc)​\n\nMỗi đội chuẩn bị:\n\n- 02 máy tính (PC hoặc laptop) có kết nối Internet để thực hiện các yêu cầu của đề thi. Máy tính này sẽ được kết nối với hệ thống giám sát của Ban tổ chức — hệ thống sẽ ghi lại toàn bộ hoạt động trên màn hình trong suốt quá trình thi.\n- 02 điện thoại thông minh (kèm tripod và giá kẹp) để ghi hình phiên thi. Cụ thể:\n\n#### Điện thoại 1 — Ghi hình chính​\n\n- Chế độ: bật \"Flight/Airplane mode\" (không kết nối mạng).\n- Kết nối nguồn điện liên tục (sạc suốt phiên thi).\n- Tắt khóa màn hình (không để màn hình tắt tự động).\n- Đặt ghi hình theo phương ngang (landscape).\n- Góc máy: như ảnh mẫu 1.\n- Định dạng file: MP4 hoặc MOV, độ phân giải tối thiểu Full HD (1920x1080).\n\n#### Điện thoại 2 — Giám sát trực tiếp​\n\n- Chế độ: bật kết nối Internet (sẽ dùng để truyền hình ảnh trực tiếp cho Hội đồng giám thị).\n- Kết nối nguồn điện liên tục.\n- Tắt chế độ hiển thị thông báo với tất cả ứng dụng.\n- Tắt khóa màn hình (không để màn hình tắt tự động).\n- Tắt khoá màn hình dọc.\n- Đặt quay ngang (landscape) với góc máy như ảnh mẫu 2.\n- Thiết bị này sẽ kết nối với hệ thống giám sát của Hội đồng giám thị trong suốt quá trình thi.\n\n> [Lưu ý]\n> Mã kết nối sẽ được Ban tổ chức cung cấp trước giờ thi.\n\n### 3. Hướng dẫn ghi hình và lưu trữ​\n\n- Cả hai điện thoại cần được cố định chắc chắn trên tripod, không cầm tay trong suốt phiên thi.\n- Kiểm tra trước rằng hai camera không che khuất lẫn nhau và bao quát đủ khu vực làm việc (màn hình máy tính, bàn làm việc và thí sinh).\n- Đặt tên file video (Điện thoại 1) theo cấu trúc: MãĐội_TênĐội_NgàyThi (ví dụ: A12_TeamAlpha_2025-10-15.mp4).\n- Nên kiểm tra bản thu thử (~30 giây) và đảm bảo chất lượng âm thanh/ánh sáng/chế độ quay ngang.\n\n### 4. Quy định nộp kết quả​\n\n- Sau khi kết thúc thời gian làm bài chính thức, mỗi đội có 10 phút để nộp kết quả lên máy chủ của Ban Giám khảo theo hướng dẫn chi tiết sẽ được cung cấp kèm đề thi.\n- Một bộ kết quả hợp lệ bao gồm:\n  \n  \n  \n  - File kết quả bài làm theo yêu cầu đề thi (định dạng/đường dẫn nộp theo hướng dẫn đề tài).\n  - File video ghi hình quá trình làm bài (Video Điện thoại 1). Có thể upload lên Google Drive/OneDrive với quyền tải xuống (download) và gửi link tải về email chính thức của Ban Tổ chức.\n- Kết quả chấm thi sẽ dựa trên: nội dung bài làm và quá trình thực hiện trong video giám sát.\n\n### 5. Xử lý vi phạm​\n\n- Mọi hành vi can thiệp từ bên ngoài (nhận trợ giúp trái phép, sử dụng tư liệu/công cụ không được phép, thay người thi, v.v.) sẽ bị coi là phạm quy.\n- Mức xử lý: trừ điểm, loại bỏ phần thi hoặc hủy kết quả đội thi tùy theo mức độ vi phạm.\n\n### 6. Lời nhắn tới các đội​\n\nBan tổ chức đề nghị các đội nghiêm túc phối hợp, chuẩn bị kỹ lưỡng, tuân thủ quy định để đảm bảo tính công bằng, minh bạch và trung thực trong cuộc thi.\n\nTrân trọng cảm ơn.\n\n**BAN TỔ CHỨC**\n"
  },
  "suno-login-guidelines": {
    "title": "Hướng dẫn đăng nhập Suno",
    "file": "docs/round-2/suno-login-guidelines.md",
    "breadcrumbs": [
      "Vòng Chung Khảo",
      "Hướng dẫn đăng nhập Suno"
    ],
    "content": "# Hướng dẫn đăng nhập Suno\n\nTài liệu này hướng dẫn chi tiết cách đăng nhập vào Suno bằng tài khoản do Ban Tổ Chức (BTC) cung cấp.\n\n## Bước 1: Truy cập trang đăng nhập​\n\n1. Mở trình duyệt và truy cập: https://suno.com/home\n2. Nhấn vào nút **\"Sign In\"** ở góc trên bên phải\n\n## Bước 2: Chọn phương thức đăng nhập​\n\n> [Khuyến nghị]\n> Chọn đăng nhập bằng tài khoản Microsoft do BTC cung cấp.\n\n## Bước 3: Nhập thông tin đăng nhập​\n\n1. Nhập **email** do BTC cung cấp vào ô \"Email\"\n2. Nhấn nút \"Next\"\n\n## Bước 4: Nhập mật khẩu​\n\n1. Nhập **mật khẩu** do BTC cung cấp vào ô \"Password\"\n2. Nhấn nút **\"Sign in\"**\n\n## Lưu ý quan trọng​\n\nTrong trường hợp yêu cầu đăng nhập cần mã OTP, sử dụng công cụ OTP để lấy mã đăng nhập\n\n> [Bảo mật tài khoản]\n> - **Không chia sẻ** thông tin đăng nhập với người khác\n> - **Không thay đổi** mật khẩu tài khoản được cung cấp\n> - Nếu gặp vấn đề đăng nhập, vui lòng liên hệ BTC ngay lập tức\n\n## Xử lý sự cố​\n\n### Không thể đăng nhập​\n\nNếu bạn gặp lỗi khi đăng nhập:\n\n1. **Kiểm tra lại thông tin**: Đảm bảo email và mật khẩu được nhập chính xác\n2. **Xóa cache trình duyệt**: Thử xóa cache và cookie rồi đăng nhập lại\n3. **Thử trình duyệt khác**: Sử dụng Chrome, Firefox, hoặc Edge\n4. **Liên hệ BTC**: Nếu vẫn không được, báo ngay cho BTC để được hỗ trợ\n\n### Quên mật khẩu​\n\n> [Lưu ý]\n> **KHÔNG** sử dụng chức năng \"Forgot Password\" trên Suno vì đây là tài khoản do BTC quản lý.\n> Nếu quên mật khẩu, vui lòng liên hệ trực tiếp với BTC để được cấp lại thông tin đăng nhập.\n\n## Sau khi đăng nhập thành công​\n\nKhi đăng nhập thành công, bạn có thể:\n\n- Tạo nhạc bằng AI\n- Xem lịch sử các bài hát đã tạo\n- Quản lý thư viện cá nhân\n\n**Liên hệ hỗ trợ**: Nếu cần trợ giúp, vui lòng liên hệ Ban Tổ Chức qua kênh hỗ trợ chính thức.\n"
  },
  "otp-generator": {
    "title": "Công cụ OTP",
    "file": "docs/round-2/otp-generator.md",
    "breadcrumbs": [
      "Vòng Chung Khảo",
      "Công cụ OTP"
    ],
    "content": "# Công cụ Tạo mã OTP\n\nCông cụ này tạo Mật khẩu một lần dựa trên thời gian (TOTP) từ một secret key, tương thích với Google Authenticator, Microsoft Authenticator, và các ứng dụng 2FA tiêu chuẩn khác.\n\n## Hướng dẫn sử dụng​\n\n1. **Nhập Secret Key của bạn**: Dán secret key đã được mã hóa Base32 của bạn vào ô nhập liệu bên dưới.\n2. **Nhận mã OTP**: Công cụ sẽ tự động tạo mã OTP 6 chữ số hiện tại.\n3. **Tự động làm mới**: Mã sẽ tự động làm mới sau mỗi 30 giây, giống như ứng dụng xác thực của bạn.\n\nSecret Key (Base32):💡 Thử với secret key mẫu: JBSWY3DPEHPK3PXP------Copy\n\n## Lưu ý Bảo mật​\n\n- **Chỉ xử lý phía Client**: Mọi tính toán đều được thực hiện trực tiếp trong trình duyệt của bạn. Secret key của bạn không bao giờ được gửi đến bất kỳ máy chủ nào.\n- **Không chia sẻ Key**: Secret key là thông tin nhạy cảm. Không chia sẻ công khai. Công cụ này dành cho mục đích phát triển và kiểm thử.\n"
  },
  "vibe-coding": {
    "title": "Tích hợp với công cụ AI Coding",
    "file": "docs/round-2/using-google-genai/vibe-coding.md",
    "breadcrumbs": [
      "Vòng Chung Khảo",
      "Sử dụng với Google GenAI",
      "Tích hợp với công cụ AI Coding"
    ],
    "content": "# Tích hợp với công cụ AI Coding\n\nSử dụng `GEMINI_API_KEY` để tích hợp với Gemini CLI, Github Copilot, Cursor, Cline, KiloCode, Trae, v.v.\n"
  },
  "google-genai": {
    "title": "Sử dụng với Gemini/Vertex AI",
    "file": "docs/round-2/using-google-genai/google-genai.md",
    "breadcrumbs": [
      "Vòng Chung Khảo",
      "Sử dụng với Google GenAI",
      "Sử dụng với Gemini/Vertex AI"
    ],
    "content": "# Sử dụng với Gemini/Vertex AI\n\n \n\n- Vertex AI\n- Gemini\n\n## Xác thực (Authentication)​\n\nĐể xác thực với Vertex AI, bạn cần sử dụng service account key đã được ban tổ chức cung cấp và đặt đường dẫn của nó vào biến môi trường `GOOGLE_APPLICATION_CREDENTIALS`.\n\n**Đặt Biến Môi trường**:\nThêm biến môi trường sau vào môi trường local của bạn, trỏ đến file JSON đã được cung cấp.\n\n`export GOOGLE_APPLICATION_CREDENTIALS=\"/path/to/your/keyfile.json\"`\n\nChi tiết hơn có thể xem tại Google Cloud Documentation.\n\n## Hướng dẫn sử dụng cơ bản​\n\n### Tạo văn bản (Text Generation)​\n\nCài đặt thư viện cần thiết:\n\n`pip install --upgrade google-genai`\n\nSử dụng trong code:\n\n`from google import genaifrom dotenv import load_dotenvload_dotenv()   client = genai.Client(vertexai=True, location=\"us-central1\")response = client.models.generate_content(  model=\"gemini-2.5-flash\",  contents=\"Explain how AI works in a few words\")print(response.text)`\n\n### Tạo hình ảnh (Image Generation)​\n\nVới Vertex AI, bạn có thể sử dụng các mô hình tạo ảnh như Imagen.\n\n`from google import genaifrom google.genai.types import GenerateImagesConfig# Cần xác thực với GOOGLE_APPLICATION_CREDENTIALSclient = genai.Client()output_file = \"output-image.png\"image = client.models.generate_images(  model=\"imagen-4.0-generate-001\",  prompt=\"A dog reading a newspaper\",  config=GenerateImagesConfig(      image_size=\"2K\",  ),)image.generated_images[0].image.save(output_file)print(f\"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes\")`\n\n## Xác thực với Gemini API​\n\nĐể sử dụng API của Gemini, bạn cần sử dụng API key đã được ban tổ chức cung cấp.\n\n**Đặt Biến Môi trường**:\nThêm API key đã được cung cấp vào biến môi trường `GEMINI_API_KEY`.\n\n`export GEMINI_API_KEY=\"YOUR_API_KEY\"`\n\n## Hướng dẫn cơ bản cho Gemini​\n\n### Tạo văn bản với Gemini API​\n\nCài đặt thư viện cần thiết:\n\n`pip install -q -U google-genai`\n\nSử dụng trong code:\n\n`from google import genaifrom google.genai.types import HttpOptions# Cần đặt GEMINI_API_KEY trong môi trường của bạnclient = genai.Client(http_options=HttpOptions(api_version=\"v1\"))response = client.models.generate_content(  model=\"gemini-2.5-flash\",  contents=\"How does AI work?\",)print(response.text)`\n\nĐể biết thêm chi tiết về các tính năng nâng cao như tạo video và nhiều hơn nữa, vui lòng tham khảo tài liệu chính thức của Google Generative AI.\n"
  },
  "synthetic-data": {
    "title": "Kỹ Thuật Tạo Dữ Liệu Phổ Biến",
    "file": "docs/round-3/synthetic-data.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Kỹ Thuật Tạo Dữ Liệu"
    ],
    "content": "# Kỹ Thuật Tạo Dữ Liệu Phổ Biến\n\nTrong quá trình huấn luyện mô hình ngôn ngữ, việc sử dụng dữ liệu tổng hợp (synthetic data) có thể giúp cải thiện hiệu suất và khả năng tổng quát hóa của mô hình. Dưới đây là một số kỹ thuật phổ biến để tạo dữ liệu tổng hợp\n\n## Self-Instruct Alpaca​\n\nCác mô hình ngôn ngữ lớn được \"tinh chỉnh theo hướng dẫn\" (instruction-tuned) đã thể hiện khả năng đáng chú ý trong việc tổng quát hóa zero-shot sang các nhiệm vụ mới. Tuy nhiên, chúng phụ thuộc nhiều vào dữ liệu hướng dẫn do con người viết, vốn thường bị hạn chế về số lượng, tính đa dạng và tính sáng tạo, do đó cản trở tính tổng quát của mô hình đã được tinh chỉnh ......\n\nTham khảo Self-Instruct: Aligning Language Models with Self-Generated Instructions\n\n## Evolutionary Algorithm​\n\nViệc huấn luyện các mô hình ngôn ngữ lớn (LLMs) bằng dữ liệu tuân thủ chỉ dẫn miền mở mang lại thành công to lớn. Tuy nhiên, việc tạo thủ công các dữ liệu chỉ dẫn như vậy rất tốn thời gian và công sức. Hơn nữa, con người có thể gặp khó khăn trong việc tạo ra các chỉ dẫn có độ phức tạp cao. Trong bài báo này, chúng tôi trình bày một phương pháp tạo ra số lượng lớn dữ liệu chỉ dẫn với các mức độ phức tạp khác nhau bằng cách sử dụng LLM thay vì con người. Bắt đầu với một bộ chỉ dẫn ban đầu, chúng tôi sử dụng Evol-Instruct được đề xuất để viết lại chúng từng bước thành các chỉ dẫn phức tạp hơn. Sau đó, chúng tôi kết hợp tất cả dữ liệu chỉ dẫn đã tạo ra để tinh chỉnh LLaMA. Chúng tôi gọi mô hình thu được là WizardLM. Cả đánh giá tự động và đánh giá của con người đều cho thấy WizardLM vượt trội hơn các mô hình cơ sở như Alpaca (được huấn luyện từ Self-Instruct) và Vicuna (được huấn luyện từ các chỉ dẫn do con người tạo ra). Kết quả thực nghiệm chứng minh rằng chất lượng của bộ dữ liệu tuân thủ chỉ dẫn được tạo ra bởi Evol-Instruct có thể cải thiện đáng kể hiệu suất của LLMs\n\nTham khảo WizardLM: Empowering Large Pre-trained Language Models to Follow Complex Instructions\n\n## MAGPIE Algorithm​\n\nDữ liệu hướng dẫn chất lượng cao là rất quan trọng để điều chỉnh các mô hình ngôn ngữ lớn (LLM). Mặc dù một số mô hình, chẳng hạn như Llama-3-Instruct, có trọng số mở (open weights), nhưng dữ liệu điều chỉnh của chúng vẫn được giữ kín, điều này cản trở sự dân chủ hóa AI. Chi phí lao động nhân công cao và phạm vi nhắc lệnh (prompting) được xác định trước, giới hạn đã ngăn cản các phương pháp tạo dữ liệu mã nguồn mở hiện có mở rộng quy mô một cách hiệu quả, có khả năng giới hạn sự đa dạng và chất lượng của các tập dữ liệu điều chỉnh công khai. Liệu có thể tổng hợp dữ liệu hướng dẫn chất lượng cao trên quy mô lớn bằng cách trích xuất trực tiếp từ một LLM đã được điều chỉnh không?......\n\nTham khảo MAGPIE: Model-Aided Generation of Prompts for Instruction\nEngineering\n\n## Scaling Synthetic Data Creation with 1,000,000,000 Personas​\n\nChúng tôi đề xuất một phương pháp tổng hợp dữ liệu mới dựa trên nhân vật (persona-driven) khai thác các góc nhìn khác nhau trong một mô hình ngôn ngữ lớn (LLM) để tạo ra dữ liệu tổng hợp đa dạng. Để khai thác triệt để phương pháp này ở quy mô lớn, chúng tôi giới thiệu Persona Hub – một bộ sưu tập 1 tỷ nhân vật đa dạng được tự động tuyển chọn từ dữ liệu web. 1 tỷ nhân vật này (tương đương ≈13% tổng dân số thế giới), hoạt động như những vật mang tri thức thế giới được phân tán, có thể khai thác gần như mọi góc nhìn được gói gọn trong LLM, từ đó tạo điều kiện cho việc tạo ra dữ liệu tổng hợp đa dạng ở quy mô lớn cho nhiều kịch bản khác nhau......\n\nTham khảo Scaling Synthetic Data Creation with 1,000,000,000 Personas\n\n## Mixing Data Strategies​\n\nBộ dữ liệu tiền huấn luyện thường được thu thập từ nội dung web và thiếu sự phân chia miền (domain) vốn có. Ví dụ, các bộ dữ liệu được sử dụng rộng rãi như Common Crawl không bao gồm nhãn miền rõ ràng, trong khi việc quản lý thủ công các bộ dữ liệu được gắn nhãn như The Pile lại tốn nhiều công sức. Do đó, việc xác định hỗn hợp dữ liệu tiền huấn luyện tối ưu vẫn là một vấn đề khó khăn, mặc dù nó mang lại lợi ích đáng kể cho hiệu suất tiền huấn luyện. Để giải quyết những thách thức này, chúng tôi đề xuất CLustering-based Iterative Data Mixture Bootstrapping (CLIMB), một khuôn khổ tự động giúp khám phá, đánh giá và tinh chỉnh các hỗn hợp dữ liệu trong môi trường tiền huấn luyện.......\n\nTham khảo CLIMB: Automated Data Mixture Optimization for Language Model Pretraining\n\n## Knowledge Distillation with Synthetic Data​\n\nChưng cất tri thức (Knowledge distillation) là kỹ thuật nén một mạng thần kinh lớn hơn, được gọi là mô hình giáo viên (teacher model), thành một mạng thần kinh nhỏ hơn, được gọi là mô hình học sinh (student model), trong khi vẫn cố gắng duy trì hiệu suất của mạng thần kinh lớn hơn càng nhiều càng tốt. Các phương pháp chưng cất tri thức hiện có chủ yếu áp dụng cho các tác vụ phân loại (classification tasks). Nhiều phương pháp trong số đó cũng yêu cầu quyền truy cập vào dữ liệu gốc được sử dụng để đào tạo mô hình giáo viên. Để giải quyết vấn đề chưng cất tri thức cho các tác vụ hồi quy (regression tasks) trong điều kiện không có dữ liệu đào tạo gốc, phương pháp hiện có sử dụng một mô hình bộ tạo (generator model) được đào tạo đối nghịch (adversarially) với mô hình học sinh để tạo dữ liệu tổng hợp đào tạo mô hình học sinh. Trong nghiên cứu này, chúng tôi đề xuất một chiến lược tạo dữ liệu tổng hợp mới, trực tiếp tối ưu hóa cho sự khác biệt lớn nhưng bị giới hạn giữa mô hình học sinh và mô hình giáo viên. Kết quả của chúng tôi trên các thử nghiệm đối chiếu cho thấy rằng chiến lược được đề xuất cho phép mô hình học sinh học tốt hơn và mô phỏng hiệu suất của mô hình giáo viên một cách sát sao hơn\n\nTham khảo Synthetic data generation method for data-free knowledge\ndistillation in regression neural networks\n\nXem thêm về Knowledge Distillation\n"
  },
  "model-training-guideline": {
    "title": "Hướng Dẫn Huấn Luyện Mô Hình",
    "file": "docs/round-3/model-training-guideline.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình"
    ],
    "content": "## 📄️   Giới Thiệu\n\nChào mừng các đội! Tài liệu này là hướng dẫn để định hướng phát triển tập trung Post-Training mô hình cho cuộc thi. Hướng dẫn này dựa trên các thực tiễn tốt nhất từ:\n\n## 📄️   Chiến Lược & Thiết Lập Tiền Huấn Luyện\n\nTrước khi bạn viết một dòng mã huấn luyện nào, đội của bạn phải xác định chiến lược của mình. \"Thực tế lộn xộn\" của việc huấn luyện mô hình là thành công phụ thuộc rất nhiều vào kế hoạch tốt.\n\n## 📄️   Huấn Luyện Phân Tán\n\nĐể huấn luyện ở quy mô lớn, bạn phải song song hóa mô hình của mình trên nhiều GPU. Mục tiêu là tìm sự cân bằng phù hợp giữa tính toán, giao tiếp và bộ nhớ.\n\n## 📄️   Hậu Huấn Luyện & Hiệu Chỉnh\n\nMô hình tiền huấn luyện của bạn là một \"mô hình cơ sở\" (base model)—nó là một công cụ dự đoán token tiếp theo mạnh mẽ, nhưng nó không phải là một trợ lý hữu ích. Hậu huấn luyện (Post-training) sẽ hiệu chỉnh nó để tuân theo các hướng dẫn.\n\n## 📄️   Hoàn Thiện & Nộp Mô Hình\n\nMột \"mô hình\" không chỉ là các trọng số của nó. Bài nộp cuối cùng của bạn phải là một gói hoàn chỉnh.\n"
  },
  "model-training-introduction": {
    "title": "Giới Thiệu",
    "file": "docs/round-3/model-training-guideline/model-training-introduction.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình",
      "Giới Thiệu"
    ],
    "content": "# Giới Thiệu\n\nChào mừng các đội! Tài liệu này là hướng dẫn để định hướng phát triển tập trung Post-Training mô hình cho cuộc thi. Hướng dẫn này dựa trên các thực tiễn tốt nhất từ:\n\n- Smol Training Playbook\n- Nanotron Ultrascale Playbook\n- Post-training 101\n\nTrong khuôn khổ cuộc thi AI Thực Chiến, chúng tôi đề xuất quy trình huấn luyện mô hình gồm 4 giai đoạn chính:\n\n- Giai đoạn I: Chiến lược & Thiết lập Tiền huấn luyện\n- Giai đoạn II: Huấn luyện phân tán (Distributed Training)\n- Giai đoạn III: Hậu huấn luyện & Hiệu chỉnh (Alignment)\n- Giai đoạn IV: Hoàn thiện & Nộp Mô hình\n"
  },
  "pre-training-strategy-and-setup": {
    "title": "Chiến Lược & Thiết Lập Tiền Huấn Luyện",
    "file": "docs/round-3/model-training-guideline/pre-training-strategy-and-setup.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình",
      "Chiến Lược & Thiết Lập Tiền Huấn Luyện"
    ],
    "content": "# Giai Đoạn I: Chiến Lược & Thiết Lập Tiền Huấn Luyện\n\nTrước khi bạn viết một dòng mã huấn luyện nào, đội của bạn phải xác định chiến lược của mình. \"Thực tế lộn xộn\" của việc huấn luyện mô hình là thành công phụ thuộc rất nhiều vào kế hoạch tốt.\n\nXác định \"Kim chỉ nam Huấn luyện\" của bạn:\n\n- *Tại sao bạn lại huấn luyện mô hình này?*\n- *Mục tiêu của bạn là hiệu suất hàng đầu (state-of-the-art) trên một benchmark cụ thể, một đóng góp nghiên cứu mới, hay một mô hình hiệu quả nhất cho một tác vụ giống như sản xuất?*\n\nCâu trả lời cho \"tại sao\" sẽ định hướng mọi quyết định. Dưới đây là một số nguyên tắc hướng dẫn để giúp bạn thiết lập chiến lược tiền huấn luyện của mình:\n\n- **Bắt đầu với các Thí nghiệm Riêng lẻ (Ablations):** Tất cả các mô hình lớn đều bắt đầu từ những thí nghiệm nhỏ. Trước khi mở rộng quy mô, hãy chạy nhiều \"ablations\" (thí nghiệm quy mô nhỏ) để kiểm tra các giả thuyết của bạn.\n  \n  \n  \n  \n  > [Quy tắc Vàng]\n  > Chỉ sửa đổi một biến tại một thời điểm (ví dụ: một nguồn dữ liệu duy nhất, một siêu tham số). Nếu bạn thay đổi nhiều thứ và hiệu suất cải thiện, bạn sẽ không biết điều gì đã gây ra nó.\n- **Tuyển chọn Dữ liệu là Trên hết:** Mô hình của bạn chỉ tốt bằng dữ liệu của bạn. \"Sự pha trộn dữ liệu là quan trọng nhất.\"\n  \n  \n  \n  - **Pha trộn Dữ liệu (Data Mix):** Xác định \"chương trình giảng dạy\" (training curricula) của bạn. Đây là sự kết hợp các nguồn dữ liệu (ví dụ: văn bản web chung, mã nguồn, toán học, dữ liệu đa ngôn ngữ) mà bạn sẽ sử dụng.\n  - **Chất lượng > Số lượng:** Tập trung vào dữ liệu chất lượng cao, sạch và được lọc kỹ.\n  - **Các giai đoạn:** Cân nhắc phát triển hỗn hợp dữ liệu của bạn theo từng giai đoạn. Ví dụ, bắt đầu với dữ liệu web chung và giới thiệu dữ liệu chuyên biệt (như mã nguồn hoặc toán học) sau này trong quá trình huấn luyện.\n- **Kiến trúc & Siêu tham số (Hyperparameters):**\n  \n  \n  \n  - **Kiến trúc:** Đưa ra các lựa chọn có chủ đích về kiến trúc của mô hình (ví dụ: cơ chế chú ý (attention), mã hóa vị trí (positional encodings), Mixture of Experts (MoE)).\n  - **Siêu tham số:** Chốt các lựa chọn ban đầu của bạn cho trình tối ưu hóa (optimizer, ví dụ: AdamW), lịch trình tốc độ học (learning rate schedule), và kích thước lô toàn cục (global batch size) dựa trên các thử nghiệm quy mô nhỏ của bạn.\n"
  },
  "distributed-training": {
    "title": "Huấn Luyện Phân Tán",
    "file": "docs/round-3/model-training-guideline/distributed-training.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình",
      "Huấn Luyện Phân Tán"
    ],
    "content": "# Giai Đoạn II: Huấn Luyện Phân Tán (Distributed Training)\n\nĐể huấn luyện ở quy mô lớn, bạn phải song song hóa mô hình của mình trên nhiều GPU. Mục tiêu là tìm sự cân bằng phù hợp giữa tính toán, giao tiếp và bộ nhớ.\n\n## Một Số Kỹ Thuật Song Song Hữu Ích​\n\nKỹ ThuậtMô TảTrường Hợp Sử Dụng**Song song Dữ liệu (Data Parallelism - DP)**Sao chép toàn bộ mô hình trên mọi GPU và chia lô dữ liệu cho từng GPU.Luôn là điểm khởi đầu, làm nền tảng cho hầu hết các thiết lập huấn luyện.**Song song Tensor (Tensor Parallelism - TP)**Chia một lớp (layer) duy nhất (ma trận trọng số của nó) trên nhiều GPU. Ví dụ, trong TP 2 chiều, GPU-A giữ nửa đầu của trọng số và GPU-B giữ nửa còn lại.Khi một lớp duy nhất quá lớn để vừa với bộ nhớ của một GPU.**Song song Pipeline (Pipeline Parallelism - PP)**Chia toàn bộ mô hình theo chiều dọc, mỗi GPU xử lý một chuỗi các lớp. Ví dụ: GPU-A chạy các lớp 1-8, GPU-B chạy các lớp 9-16, v.v., giống như một dây chuyền lắp ráp. Điều này đòi hỏi \"phân lô vi mô\" (micro-batching) cẩn thận để giữ cho tất cả các GPU luôn bận rộn.Khi toàn bộ mô hình (không chỉ một lớp) quá lớn để vừa trên một GPU.**Song song Chuyên gia (Expert Parallelism - EP)**Kỹ thuật chuyên biệt, chia các \"chuyên gia\" (experts) trên các GPU khác nhau.Chỉ sử dụng cho các mô hình Mixture of Experts (MoE).\n\n## So sánh chiến lược: Full Fine-tuning vs. Tinh chỉnh Hiệu quả (LoRA)​\n\n> [Lưu ý Chiến lược]\n> Trước khi bắt đầu, đội của bạn phải đưa ra một quyết định quan trọng về phương pháp tinh chỉnh\n\n### Full Fine-tuning (Huấn luyện Toàn bộ):​\n\n**Mô tả:** Bạn cập nhật toàn bộ trọng số của mô hình.\n\n**Ưu điểm:** Có khả năng đạt được chất lượng cao nhất vì mô hình học hỏi sâu hơn.\n\n**Nhược điểm:** Yêu cầu VRAM cực kỳ cao. Để huấn luyện toàn bộ một mô hình 7B, bạn có thể cần 4-8 GPU A100/H100 80GB.\n\n### Tinh chỉnh Hiệu quả (ví dụ: LoRA/QLoRA):​\n\n**Mô tả:** Bạn \"đóng băng\" (freeze) mô hình chính và chỉ huấn luyện một số lượng nhỏ các trọng số \"adapter\" (thích ứng) được thêm vào.\n\n**Ưu điểm:** Yêu cầu VRAM thấp hơn rất nhiều (có thể huấn luyện mô hình 7B-9B trên 1-2 GPU cao cấp) và huấn luyện nhanh hơn đáng kể.\n\n**Nhược điểm:** Chất lượng có thể thấp hơn một chút so với Full FT trong một số tác vụ, nhưng thường là rất cạnh tranh.\n\n> [Khuyến nghị của BTC]\n> Các đội nên ưu tiên bắt đầu với LoRA hoặc QLoRA. Phương pháp này cho phép chu kỳ thử nghiệm nhanh hơn, tiết kiệm tài nguyên và thường mang lại kết quả xuất sắc. Chỉ nên xem xét Full Fine-tuning nếu bạn có đủ tài nguyên và đã thử nghiệm thành công với LoRA.\n\nĐể hiểu rõ hơn về sự khác biệt giữa các kỹ thuật này, bạn có thể tham khảo thêm tại đây.\n\n## Gợi ý Training Frameworks​\n\nFrameworkSFTPORLMulti-modalFullFTLoRADistributedTRL✅✅✅✅✅✅✅Axolotl✅✅✅✅✅✅✅OpenInstruct✅✅✅❌✅✅✅Unsloth✅✅✅✅✅✅✅vERL✅❌✅✅✅✅✅Prime RL✅❌✅❌✅✅✅PipelineRL❌❌✅❌✅✅✅ART❌❌✅❌❌✅❌TorchForge✅❌✅❌✅❌✅NemoRL✅✅✅❌✅❌✅OpenRLHF✅✅✅❌✅✅✅\n"
  },
  "post-training-alignment": {
    "title": "Hậu Huấn Luyện & Hiệu Chỉnh",
    "file": "docs/round-3/model-training-guideline/post-training-alignment.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình",
      "Hậu Huấn Luyện & Hiệu Chỉnh"
    ],
    "content": "# Giai Đoạn III: Hậu Huấn Luyện & Hiệu Chỉnh (Alignment)\n\nMô hình tiền huấn luyện của bạn là một \"mô hình cơ sở\" (base model)—nó là một công cụ dự đoán token tiếp theo mạnh mẽ, nhưng nó không phải là một trợ lý hữu ích. Hậu huấn luyện (Post-training) sẽ hiệu chỉnh nó để tuân theo các hướng dẫn.\n\nTrước khi bạn bắt đầu, hãy xác định các chỉ số (metrics) và bộ dữ liệu đánh giá của bạn. Làm thế nào bạn sẽ biết liệu SFT hoặc RLHF của bạn có phải là một cải tiến hay không? Sử dụng kết hợp các đánh giá tự động (ví dụ: LLM-làm-giám-khảo) và đánh giá của con người.\n\n## Tinh chỉnh có Giám sát (Supervised Fine-Tuning - SFT)​\n\n**Mục đích:** Để dạy mô hình cách phản hồi. Bạn đang thay đổi hành vi của nó từ \"tiếp tục văn bản này\" thành \"trả lời hướng dẫn này.\"\n\n**Dữ liệu:** Điều này dựa trên một bộ dữ liệu nhỏ hơn, chất lượng cao gồm các cặp hướng dẫn-phản hồi.\nVí dụ:\n\n`{  \"instruction\": \"Thủ đô của Pháp là gì?\",   \"response\": \"Thủ đô của Pháp là Paris.\"}`\n\nChất lượng và sự đa dạng của dữ liệu quan trọng hơn nhiều so với kích thước.\n\n## Tối ưu hóa Sở thích (Preference Optimization - RL)​\n\n**Mục đích:** Để làm cho các phản hồi của mô hình tốt hơn (hữu ích hơn, trung thực hơn và vô hại hơn).\n\n**Dữ liệu:** Điều này đòi hỏi một bộ dữ liệu sở thích, trong đó mỗi mục hiển thị hai hoặc nhiều phản hồi cho một câu lệnh (prompt), được xếp hạng từ tốt nhất đến tệ nhất.\n\n**Phương pháp:** Điều này thường được thực hiện bằng Học Tăng cường (RL), chẳng hạn như RLHF (từ Phản hồi của Con người) hoặc RLAIF (từ Phản hồi của AI). Điều này liên quan đến việc huấn luyện một \"Mô hình Phần thưởng\" (Reward Model) trên dữ liệu sở thích của bạn, mô hình này sau đó sẽ \"chấm điểm\" các đầu ra của mô hình SFT và dạy nó tạo ra các phản hồi được điểm cao hơn.\n\n> [Kiểm tra sự \"Nhiễm bẩn\" Dữ liệu (Contamination)!]\n> Bạn phải đảm bảo rằng dữ liệu đánh giá của bạn (đặc biệt là từ các benchmark) không có mặt trong dữ liệu huấn luyện hoặc SFT của bạn. Nếu có, điểm số cao của bạn là không hợp lệ.\n"
  },
  "model-finalization-and-submission": {
    "title": "Giai Đoạn IV: Hoàn Thiện & Nộp Mô Hình",
    "file": "docs/round-3/model-training-guideline/model-finalization-and-submission.md",
    "breadcrumbs": [
      "Vòng Bán Kết",
      "Huấn Luyện Mô Hình",
      "Hoàn Thiện & Nộp Mô Hình"
    ],
    "content": "# Giai Đoạn IV: Hoàn Thiện & Nộp Mô Hình\n\nMột \"mô hình\" không chỉ là các trọng số của nó. Bài nộp cuối cùng của bạn phải là một gói hoàn chỉnh.\n\n## Đóng gói Mô hình của bạn\n\nLưu tất cả các tệp cần thiết:\n\n- Trọng số mô hình (ví dụ: `model.safetensors`)\n- Các tệp Tokenizer (ví dụ: `tokenizer.json`)\n- Các tệp cấu hình (ví dụ: `config.json`)\n\n## Tạo một Thẻ Mô hình (Model Card)\n\nĐiều này là cần thiết. Tệp `README.md` của bạn phải là một thẻ mô hình chi tiết bao gồm:\n\n- **Mô tả Mô hình:** Nó là gì? Các tính năng chính của nó là gì?\n- **Dữ liệu Huấn luyện:** Bạn đã sử dụng hỗn hợp dữ liệu nào cho tiền huấn luyện và SFT?\n- **Quy trình Huấn luyện:** Chi tiết cấp cao về quá trình huấn luyện của bạn (siêu tham số, chiến lược song song hóa).\n- **Đánh giá:** Bạn đã đánh giá mô hình của mình như thế nào? Điểm số của nó là gì?\n- **Hạn chế & Thiên kiến (Bias):** Mô hình của bạn không thể làm gì? Nó thất bại ở đâu?\n\n## Nộp Mô hình của bạn\n\nTải lên kho lưu trữ mô hình hoàn chỉnh của bạn lên nền tảng cuộc thi (Hugging Face Hub).\n"
  },
  "round-4": {
    "title": "Vòng 4: Phát triển ứng dụng",
    "file": "docs/round-4.md",
    "breadcrumbs": [
      "Vòng Chung Kết",
      "Vòng 4: Phát triển ứng dụng"
    ],
    "content": "# Vòng 4: Phát triển ứng dụng\n\nTài liệu đang được cập nhật.\n"
  }
};

const navOrder = [
  'round-2',
  'regulations-and-technical-guidelines',
  'suno-login-guidelines',
  'otp-generator',
  'vibe-coding',
  'google-genai',
  'synthetic-data',
  'model-training-introduction',
  'pre-training-strategy-and-setup',
  'distributed-training',
  'post-training-alignment',
  'model-finalization-and-submission',
  'round-4',
  'tuan-01-intro',
  'tuan-02-synthetic-data',
  'tuan-03-data-filtering',
  'tuan-04-model-tokenizer',
  'tuan-05-sft-training',
  'tuan-06-continued-pretraining',
  'tuan-07-distributed',
  'tuan-08-preference-opt',
  'tuan-09-evaluation',
  'tuan-10-model-submission'];

// Simple Markdown to HTML Renderer
function renderMarkdown(md) {
  let html = md;
  
  // Admonitions / Callout blocks (> [Title])
  html = html.replace(/^> \[(.*?)\]\n((?:> .*\n?)+)/gm, (match, title, body) => {
    const cleanBody = body.replace(/^> /gm, '').trim();
    let type = 'tip';
    if (title.toLowerCase().includes('lưu ý') || title.toLowerCase().includes('chú ý')) type = 'warning';
    if (title.toLowerCase().includes('thông tin')) type = 'info';
    return `<div class="admonition ${type}">
      <div class="admonition-title">💡 ${title}</div>
      <div class="admonition-content"><p>${cleanBody}</p></div>
    </div>`;
  });

  // Regular blockquotes
  html = html.replace(/^> (.*$)/gim, '<blockquote>$1</blockquote>');

  // Headings
  html = html.replace(/^#### (.*$)/gim, '<h4 id="$1">$1</h4>');
  html = html.replace(/^### (.*$)/gim, '<h3 id="$1">$1</h3>');
  html = html.replace(/^## (.*$)/gim, '<h2 id="$1">$1</h2>');
  html = html.replace(/^# (.*$)/gim, '<h1 id="$1">$1</h1>');

  // Bold & Italic & Code
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');
  html = html.replace(/`(.*?)`/g, '<code>$1</code>');

  // Unordered list items
  html = html.replace(/^\- (.*$)/gim, '<li>$1</li>');
  html = html.replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>');

  // Paragraphs
  const paragraphs = html.split('\n\n');
  html = paragraphs.map(p => {
    p = p.trim();
    if (p.startsWith('<h') || p.startsWith('<div') || p.startsWith('<ul') || p.startsWith('<blockquote')) {
      return p;
    }
    return p ? `<p>${p}</p>` : '';
  }).join('\n');

  return html;
}

function loadDocument(docId) {
  const doc = docsData[docId] || docsData['round-2'];
  const articleEl = document.getElementById('docArticle');
  const breadcrumbsCurrent = document.getElementById('breadcrumbCurrent');

  // Update Breadcrumbs
  if (doc.breadcrumbs && doc.breadcrumbs.length > 0) {
    breadcrumbsCurrent.textContent = doc.breadcrumbs[doc.breadcrumbs.length - 1];
  }

  // Render content
  articleEl.innerHTML = renderMarkdown(doc.content);

  // Update Active Navigation Item
  document.querySelectorAll('.nav-item').forEach(item => {
    item.classList.remove('active');
    if (item.getAttribute('href') === `#${docId}`) {
      item.classList.add('active');
    }
  });

  // Build Right Table of Contents (TOC)
  buildTOC();

  // Update Pagination links
  updatePagination(docId);
  
  // Scroll to top
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

function buildTOC() {
  const tocNav = document.getElementById('tocNav');
  tocNav.innerHTML = '';
  
  const headings = document.querySelectorAll('.doc-article h2, .doc-article h3');
  if (headings.length === 0) {
    document.querySelector('.toc-sidebar').style.display = 'none';
    return;
  }
  document.querySelector('.toc-sidebar').style.display = 'block';

  headings.forEach(h => {
    const id = h.textContent.trim().toLowerCase().replace(/[^a-z0-9\u00C0-\u024F]/gi, '-');
    h.id = id;

    const link = document.createElement('a');
    link.href = `#${id}`;
    link.textContent = h.textContent;
    if (h.tagName === 'H3') link.style.paddingLeft = '0.75rem';
    
    link.addEventListener('click', (e) => {
      e.preventDefault();
      h.scrollIntoView({ behavior: 'smooth' });
    });

    tocNav.appendChild(link);
  });
}

function updatePagination(currentDocId) {
  const idx = navOrder.indexOf(currentDocId);
  const prevBtn = document.getElementById('prevDocBtn');
  const nextBtn = document.getElementById('nextDocBtn');

  if (idx > 0) {
    const prevId = navOrder[idx - 1];
    prevBtn.href = `#${prevId}`;
    document.getElementById('prevDocTitle').textContent = docsData[prevId].title;
    prevBtn.classList.remove('hidden');
  } else {
    prevBtn.classList.add('hidden');
  }

  if (idx >= 0 && idx < navOrder.length - 1) {
    const nextId = navOrder[idx + 1];
    nextBtn.href = `#${nextId}`;
    document.getElementById('nextDocTitle').textContent = docsData[nextId].title;
    nextBtn.classList.remove('hidden');
  } else {
    nextBtn.classList.add('hidden');
  }
}

// Theme Toggle Handler
const themeToggle = document.getElementById('themeToggle');
themeToggle.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
});

// Restore Theme Preference
const savedTheme = localStorage.getItem('theme') || 'dark';
document.documentElement.setAttribute('data-theme', savedTheme);

// Collapsible Navigation Sidebar
document.querySelectorAll('.nav-group-header').forEach(header => {
  header.addEventListener('click', () => {
    const group = header.parentElement;
    group.classList.toggle('collapsed');
    group.classList.toggle('expanded');
  });
});

// Mobile Sidebar Toggle
const mobileToggle = document.getElementById('mobileToggle');
const sidebar = document.getElementById('sidebar');
const sidebarBackdrop = document.getElementById('sidebarBackdrop');

function toggleMobileSidebar() {
  sidebar.classList.toggle('open');
  sidebarBackdrop.classList.toggle('active');
}

mobileToggle.addEventListener('click', toggleMobileSidebar);
sidebarBackdrop.addEventListener('click', toggleMobileSidebar);

// Search Feature
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

searchInput.addEventListener('input', (e) => {
  const query = e.target.value.toLowerCase().trim();
  if (!query) {
    searchResults.classList.add('hidden');
    return;
  }

  const matches = [];
  Object.keys(docsData).forEach(id => {
    const doc = docsData[id];
    if (doc.title.toLowerCase().includes(query) || doc.content.toLowerCase().includes(query)) {
      matches.push({ id, title: doc.title, snippet: doc.content.substring(0, 80) + '...' });
    }
  });

  if (matches.length > 0) {
    searchResults.innerHTML = matches.map(m => `
      <div class="search-item" data-id="${m.id}">
        <div class="search-item-title">${m.title}</div>
        <div class="search-item-snippet">${m.snippet}</div>
      </div>
    `).join('');
    searchResults.classList.remove('hidden');

    document.querySelectorAll('.search-item').forEach(item => {
      item.addEventListener('click', () => {
        const id = item.getAttribute('data-id');
        window.location.hash = id;
        searchResults.classList.add('hidden');
        searchInput.value = '';
      });
    });
  } else {
    searchResults.innerHTML = '<div class="search-item"><div class="search-item-snippet">Không tìm thấy kết quả.</div></div>';
    searchResults.classList.remove('hidden');
  }
});

// Handle hash navigation
window.addEventListener('hashchange', () => {
  const hash = window.location.hash.replace('#', '');
  if (hash && docsData[hash]) {
    loadDocument(hash);
  }
});

// Keyboard shortcut (Ctrl+K or Cmd+K for search)
document.addEventListener('keydown', (e) => {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
    e.preventDefault();
    searchInput.focus();
  }
});

// Initial Load
const initialHash = window.location.hash.replace('#', '') || 'regulations-and-technical-guidelines';
loadDocument(initialHash);
