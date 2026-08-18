# AeroLLM

**Aero How to LLMs** — khoá học thực hành bằng tiếng Việt về mô hình ngôn ngữ lớn (LLM): từ Python và toán nền tảng, token hoá, tự xây GPT, huấn luyện, tinh chỉnh, đánh giá đến RAG, an toàn và interpretability.

Repo này vừa là **kho học liệu** (nội dung khoá học) vừa là **trang học tập tĩnh** triển khai trên GitHub Pages. Trang có giao diện cyberpunk kiểu IDE: hero + marquee + lưới thẻ khoá + classroom + method + safety ở trang chủ, và trang khoá học có sidebar, mục lục (TOC), điều hướng tuần và code viewer.

## Truy cập trang học tập

**[Mở AeroLLM trên GitHub Pages →](https://aerovfx.github.io/AeroLLM/)**

- Trang chủ `index.html` là HTML tĩnh (không qua Jekyll layout).
- Trang khoá học render qua `_layouts/course.html`: mỗi file `.md` có front matter `layout: course` + `permalink`, Jekyll sinh `.html`; `course.js` dựa vào cấu trúc thư mục `*-10weeks` để vẽ sidebar/TOC/điều hướng tuần.

### Công cụ lớp học

- [Cổng lớp học](https://aerovfx.github.io/AeroLLM/tools/khao-sat/portal.html)
- [Khảo sát học viên](https://aerovfx.github.io/AeroLLM/tools/khao-sat/index.html)
- [Đánh giá đồng đẳng](https://aerovfx.github.io/AeroLLM/tools/khao-sat/danh-gia.html)
- [Dashboard kết quả](https://aerovfx.github.io/AeroLLM/tools/khao-sat/ket-qua.html)
- [Chấm điểm giáo viên](https://aerovfx.github.io/AeroLLM/tools/khao-sat/admin.html)

Các công cụ lưu dữ liệu trong trình duyệt theo mặc định. Giáo viên có thể cấu hình Google Apps Script của riêng mình để đồng bộ tuỳ chọn với Google Sheets.

## Bắt đầu ở đây

1. Đọc [Lộ trình khoá học](COURSE.md) để chọn điểm bắt đầu và thứ tự học.
2. Mở [Chỉ mục toàn bộ nội dung](CONTENT_INDEX.md) khi cần tìm một bài, notebook hoặc mã nguồn cụ thể.
3. Nếu muốn học theo chương trình ngắn, dùng [khoá nanoGPT 10 tuần](nanogpt_course/README.md).
4. Để học theo chuyên đề nghề nghiệp, chọn một trong [các khoá 10 tuần](courses/README.md).

> `COURSE.md` là nguồn chuẩn về thứ tự học. Các số trong tên thư mục `docs/` là mã lưu trữ cũ, không phải thứ tự bắt buộc.

## Mở nhanh các khoá học

| Khoá học | Mục lục | Tuần 1 | Lịch học |
|---|---|---|---|
| Python & Toán cho LLM | [Mở khoá](1_Foundations/python-math-foundations-10weeks/INDEX.md) | [Tuần 1](1_Foundations/python-math-foundations-10weeks/lessons/week01.md) | [Lịch](1_Foundations/python-math-foundations-10weeks/schedule.md) |
| Xây LLM từ đầu | [Mở khoá](2_LLM_Core/llm-from-scratch-10weeks/INDEX.md) | [Tuần 1](2_LLM_Core/llm-from-scratch-10weeks/lessons/week01.md) | [Lịch](2_LLM_Core/llm-from-scratch-10weeks/schedule.md) |
| Fine-tuning open-weight | [Mở khoá](3_FineTuning/openweight-finetuning-10weeks/INDEX.md) | [Tuần 1](3_FineTuning/openweight-finetuning-10weeks/lessons/week01.md) | [Lịch](3_FineTuning/openweight-finetuning-10weeks/schedule.md) |
| Pipeline huấn luyện open-weight | [Mở khoá](4_Training/openweight-training-pipeline-10weeks/INDEX.md) | [Tuần 1](4_Training/openweight-training-pipeline-10weeks/lessons/week01.md) | [Lịch](4_Training/openweight-training-pipeline-10weeks/schedule.md) |
| AI Thực Chiến | [Mở khoá](4_Training/ai-thuc-chien-10weeks/INDEX.md) | [Tuần 1](4_Training/ai-thuc-chien-10weeks/lessons/week01.md) | [Lịch](4_Training/ai-thuc-chien-10weeks/schedule.md) |
| Ứng dụng LLM | [Mở khoá](5_Applications/llm-applications-10weeks/INDEX.md) | [Tuần 1](5_Applications/llm-applications-10weeks/lessons/week01.md) | [Lịch](5_Applications/llm-applications-10weeks/schedule.md) |
| Interpretability | [Mở khoá](6_Interpretability/interpretability-10weeks/INDEX.md) | [Tuần 1](6_Interpretability/interpretability-10weeks/lessons/week01.md) | [Lịch](6_Interpretability/interpretability-10weeks/schedule.md) |
| Kimi K3 frontier systems | [Mở khoá](7_Frontier/kimi-k3-frontier-systems-10weeks/INDEX.md) | [Tuần 1](7_Frontier/kimi-k3-frontier-systems-10weeks/lessons/week01.md) | [Lịch](7_Frontier/kimi-k3-frontier-systems-10weeks/schedule.md) |

Ngoài ra còn khoá **nanoGPT 10 tuần** cho lớp học / học sinh THPT: [mở khoá](nanogpt_course/README.md).

[Xem chỉ mục 80 tuần](courses/WEEK_INDEX.md) · [Yêu cầu máy tính](courses/COMPUTER_REQUIREMENTS.md)

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
| [`1_Foundations/` … `7_Frontier/`](courses/README.md) | Tám gói khoá `*-10weeks`, code lab, bài tập và đồ án |
| [`tools/`](tools/) | Demo & công cụ: classroom (`khao-sat/`), web AI Thực Chiến (`ai-thuc-chien-web/`), script khoá (`course-scripts/`) |
| [`docs/project_logs/`](docs/project_logs/) | Nhật ký và thiết kế dự án; tài liệu tham khảo, không thuộc luồng học bắt buộc |

## Vỏ site (GitHub Pages)

Các file tạo nên giao diện trang học tập, đặt ở gốc repo:

| File | Vai trò |
|---|---|
| `index.html` | Trang chủ tĩnh: hero + marquee + lưới thẻ khoá + classroom + method + safety + footer |
| `styles.css` | Theme chính trang chủ (biến màu ở `:root`) |
| `classroom.css` | Style phần "Classroom operations" |
| `course.css` / `course-cards.css` / `course-sidebar.css` | Style trang khoá học kiểu IDE |
| `script.js` | Tìm kiếm/lọc thẻ khoá + set năm copyright |
| `course.js` | Sidebar/TOC/điều hướng tuần/code viewer (dựa vào `-10weeks` trong path) |
| `_layouts/course.html` | Layout Jekyll cho mọi trang khoá (`.md` → `.html`) |
| `_config.yml` | `title`, `url`, `baseurl: /AeroLLM`, plugin `jekyll-relative-links` |
| `Gemfile` / `Gemfile.lock` | Build Jekyll (gem `github-pages`) |
| `404.html` | Redirect `.md` → `.html` |
| `tools/khao-sat/` | Bộ công cụ classroom (portal, survey, rubric, dashboard) |

Thương hiệu và baseurl tập trung ở: `_config.yml` (`title`, `baseurl`), `index.html` + `_layouts/course.html` (brand `AEROLLM`, mark chữ `A`, link GitHub), `404.html`, `styles.css` (text trang trí `SYSTEM://AEROLLM_V2.077`, `content: "LLM_"`).

## Chạy local

### Trang học tập (tĩnh)

Không cần cài dependency. Mở `index.html` trực tiếp hoặc chạy static server:

```bash
python3 -m http.server 8080
```

Sau đó truy cập `http://localhost:8080`. (Trang khoá học cần Jekyll build; xem phần Triển khai bên dưới.)

### Công cụ trực quan

Yêu cầu Node.js và npm:

```bash
npm install
npm run dev
```

Mở <http://localhost:3002>. Công cụ minh hoạ token embedding, attention, MLP, residual connection và Mixture of Experts.

## Triển khai GitHub Pages

1. Đẩy code lên nhánh `main`.
2. Vào **Settings → Pages**, chọn **Deploy from a branch**, chọn nhánh `main` và thư mục `/ (root)`.
3. Trang hiện được phục vụ dạng **tĩnh** (file `.nojekyll` báo GitHub Pages bỏ qua bước build Jekyll) — shell `index.html` + CSS/JS hiển thị ngay tại `https://aerovfx.github.io/AeroLLM/`.

> Khi thêm trang khoá học (file `.md` có front matter `layout: course`), hãy xoá `.nojekyll` và bật lại Jekyll (hoặc dùng GitHub Actions với `actions/jekyll-build-pages`), đồng thời thêm `exclude` cho `skills/` và các thư mục nội dung LLM trong `_config.yml` để tránh lỗi Liquid (`{% %}`/`{{ }}`) từ code mẫu.

## Quy ước sử dụng

- Đi theo thứ tự trong `COURSE.md`; không suy ra thứ tự từ số thư mục.
- Mỗi giai đoạn nên hoàn thành ít nhất một bài thực hành hoặc sản phẩm đầu ra.
- Notebook và mã trong `src/` là phần thực hành đi kèm, không phải một khoá học độc lập.
- Các chuyên đề interpretability có thể học sau khi đã hoàn thành Build GPT và Evaluation.
- Khi thêm khoá mới, mỗi file `.md` phải có front matter `layout: course` + `permalink` đúng chuẩn Jekyll; tham khảo cấu trúc `lessons/code/exercises/projects` trong các thư mục `courses/*`.

## Đóng góp

Khi thêm nội dung, hãy cập nhật [chỉ mục nội dung](CONTENT_INDEX.md) và đặt bài vào đúng giai đoạn trong [lộ trình](COURSE.md). Không đưa nhật ký phát triển vào luồng bài học chính. Công việc liên quan đến tạo/sửa khoá học phải tuân theo hướng dẫn trong [skills/cyberlearn-course-creator/SKILL.md](skills/cyberlearn-course-creator/SKILL.md).

Giấy phép: [Apache License 2.0](LICENSE.txt).
