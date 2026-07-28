# Aero How to LLMs

Khoá học thực hành bằng tiếng Việt về mô hình ngôn ngữ lớn: từ Python và toán nền tảng, token hoá, tự xây GPT, huấn luyện, tinh chỉnh, đánh giá đến RAG, an toàn và interpretability.

## Bắt đầu ở đây

1. Đọc [Lộ trình khoá học](COURSE.md) để chọn điểm bắt đầu và thứ tự học.
2. Mở [Chỉ mục toàn bộ nội dung](CONTENT_INDEX.md) khi cần tìm một bài, notebook hoặc mã nguồn cụ thể.
3. Nếu muốn học theo chương trình ngắn, dùng [khoá nanoGPT 10 tuần](nanogpt_course/README.md).

> `COURSE.md` là nguồn chuẩn về thứ tự học. Các số trong tên thư mục `docs/` là mã lưu trữ cũ, không phải thứ tự bắt buộc.

## Ba cách học

| Lộ trình | Phù hợp với | Điểm vào |
|---|---|---|
| Chuẩn | Người đã biết Python cơ bản, muốn hiểu và tự xây LLM | [Giai đoạn 1](COURSE.md#giai-đoạn-1-bức-tranh-toàn-cảnh) |
| Có bổ trợ | Người mới với Python, PyTorch hoặc toán cho deep learning | [Giai đoạn 0](COURSE.md#giai-đoạn-0-bổ-trợ-khi-cần) |
| 10 tuần | Học sinh THPT, lớp học hoặc câu lạc bộ | [nanoGPT Course](nanogpt_course/README.md) |

## Cấu trúc kho học liệu

| Khu vực | Vai trò |
|---|---|
| [`docs/`](docs/index.md) | Bài giảng lý thuyết, bài tập và chuyên đề |
| [`src/`](src/README.md) | Notebook, mã Python và ứng dụng trực quan |
| [`nanogpt_course/`](nanogpt_course/README.md) | Giáo án và học liệu 10 tuần |
| [`aithucchien/`](aithucchien/README.md) | Nhánh thực chiến: dữ liệu, training, alignment, submission |
| [`docs/project_logs/`](docs/project_logs/) | Nhật ký và thiết kế dự án; tài liệu tham khảo, không thuộc luồng học bắt buộc |

## Chạy công cụ trực quan

Yêu cầu Node.js và npm:

```bash
npm install
npm run dev
```

Mở <http://localhost:3002>. Công cụ minh hoạ token embedding, attention, MLP, residual connection và Mixture of Experts.

## Quy ước sử dụng

- Đi theo thứ tự trong `COURSE.md`; không suy ra thứ tự từ số thư mục.
- Mỗi giai đoạn nên hoàn thành ít nhất một bài thực hành hoặc sản phẩm đầu ra.
- Notebook và mã trong `src/` là phần thực hành đi kèm, không phải một khoá học độc lập.
- Các chuyên đề interpretability có thể học sau khi đã hoàn thành Build GPT và Evaluation.

## Đóng góp

Khi thêm nội dung, hãy cập nhật [chỉ mục nội dung](CONTENT_INDEX.md) và đặt bài vào đúng giai đoạn trong [lộ trình](COURSE.md). Không đưa nhật ký phát triển vào luồng bài học chính.

Giấy phép: [Apache License 2.0](LICENSE.txt).
