---
name: cyberlearn-course-creator
description: Tạo, mở rộng và kiểm tra khóa học AeroLLM 10 tuần bằng tiếng Việt/Anh, gồm bài học, code minh họa có chú thích, bài tập, rubric đánh giá, dự án cuối khóa, điều hướng tuần và khung code kiểu IDE. Dùng khi người dùng yêu cầu tạo khóa học mới, thêm tuần/bài, sinh code thực hành, tạo bài tập hoặc đánh giá, chuẩn hóa khóa hiện có, hay áp dụng cấu trúc của một khóa AeroLLM cho khóa khác.
---

# AeroLLM Course Creator

## Mục tiêu

Tạo khóa học có thể học và chạy được, không chỉ sinh bộ khung tài liệu. Mỗi khóa phải:

- có lộ trình 10 tuần tăng dần độ khó;
- hỗ trợ nội dung song ngữ Việt/Anh khi phù hợp;
- có code thực sự minh họa đúng tên bài;
- có chú thích tiếng Việt về luồng xử lý và điểm an toàn;
- có bài tập, rubric và dự án cuối khóa;
- dùng chung giao diện, điều hướng và code viewer của AeroLLM;
- build được bằng Jekyll/GitHub Pages;
- chỉ dùng môi trường lab thuộc sở hữu hoặc được ủy quyền.

## Nguồn chuẩn trong repository

Trước khi làm việc, đọc các file liên quan:

- `_layouts/course.html`: layout dùng chung;
- `course.js`: mục lục, điều hướng tuần, code viewer và copy;
- `course.css`, `course-cards.css`, `course-sidebar.css`: giao diện;
- `_config.yml`, `Gemfile`, `Gemfile.lock`: cấu hình build;
- khóa gần nhất về chủ đề để học cấu trúc, không sao chép nội dung mù quáng;
- `references/safety.md` của khóa gần nhất.

Đọc [course-blueprint.md](references/course-blueprint.md) khi tạo mới nhiều file hoặc chuẩn hóa toàn khóa.

## Quy trình bắt buộc

### 1. Khảo sát và xác định phạm vi

1. Kiểm tra cây thư mục và trạng thái Git.
2. Xác định khóa mới hay khóa đang có.
3. Xác định người học, prerequisite, công cụ và kết quả đầu ra.
4. Nếu người dùng không nêu rõ, mặc định:
   - 10 tuần, mức cơ bản đến trung cấp;
   - tiếng Việt là chính, thuật ngữ Anh trong ngoặc;
   - lab local/offline trên tài nguyên được phép;
   - 20 ví dụ code mỗi tuần nếu thiên về lập trình;
   - một final project có rubric.

Không đổi layout toàn site nếu yêu cầu chỉ liên quan một khóa, trừ khi tính năng cần dùng chung.

### 2. Thiết kế chương trình

Tạo `schedule.md` trước khi viết bài. Mỗi tuần phải có chủ đề, kết quả học tập đo được, lý thuyết, công cụ, lab, sản phẩm nộp, cách đánh giá và liên hệ với tuần kế tiếp.

Nhịp độ khuyến nghị:

1. nền tảng và môi trường;
2. kỹ thuật lõi;
3. cấu trúc dữ liệu hoặc luồng xử lý;
4. quan sát và phân tích;
5. phòng thủ và kiểm soát;
6. tích hợp công cụ;
7. kiểm thử và phát hiện lỗi;
8. xử lý tình huống;
9. xây mini project;
10. hoàn thiện, demo và đánh giá cuối khóa.

### 3. Tạo cấu trúc khóa

Tên thư mục dùng kebab-case và kết thúc bằng `-10weeks` để `course.js` nhận diện:

```text
<category>/<course-name>-10weeks/
├── INDEX.md
├── schedule.md
├── lessons/week01.md ... week10.md
├── code/
│   ├── README.md
│   ├── WEEKLY_EXAMPLES.md
│   └── week01/ ... week10/
├── projects/final_project.md
├── references/components.md
├── references/safety.md
├── references/software.md
└── notebooks/ (chỉ khi cần)
```

Markdown hiển thị như trang học phải có front matter:

```yaml
---
layout: course
title: "Week01"
permalink: /<category>/<course-name>-10weeks/lessons/week01.html
---
```

### 4. Viết bài học

Mỗi `lessons/weekNN.md` nên có:

1. tiêu đề tuần;
2. mục tiêu / objectives;
3. công cụ và dữ liệu;
4. lý thuyết, định nghĩa, ví dụ;
5. lab từng bước;
6. liên kết code mẫu;
7. câu hỏi thảo luận;
8. bài tập cơ bản, nâng cao, thử thách;
9. yêu cầu nộp bài;
10. rubric;
11. lưu ý an toàn và phạm vi được phép.

Không lặp nội dung giữa các tuần. Mỗi mục tiêu phải có hoạt động hoặc tiêu chí đánh giá tương ứng.

### 5. Tạo code minh họa

Mỗi file code phải:

- minh họa đúng tên file và chức năng;
- chạy độc lập hoặc ghi rõ dependency;
- dùng dữ liệu giả/lab local an toàn;
- không chứa secret, token, IP mục tiêu thật hoặc hành vi phá hoại;
- có chú thích Việt ở đầu: mục tiêu, đầu vào, đầu ra, an toàn;
- chú thích import/include, cấu hình, hàm, vòng lặp, nhánh lỗi và cleanup;
- ưu tiên API an toàn và quản lý tài nguyên tự động;
- xử lý lỗi rõ ràng;
- có lệnh chạy và kết quả mong đợi trong README tuần.

Không tạo nhiều file cùng một thuật toán chỉ đổi số hoặc tên. Mỗi ví dụ phải thêm một khái niệm hoặc mức tích hợp mới.

Để code hiển thị như IDE và tự đồng bộ, dùng:

````markdown
## 01_ten_vi_du.ext

**Chức năng:** Mô tả cụ thể đầu vào, xử lý và kết quả.

```language
{% include_relative 01_ten_vi_du.ext %}
```
````

`course.js` tự bổ sung toolbar, chức năng, ngôn ngữ, số dòng và nút COPY CODE. Không chép code thủ công vào README nếu dùng được `include_relative`.

### 6. Bài tập và đánh giá

Mỗi tuần cần ba mức:

- Cơ bản: kiến thức và thao tác chính;
- Nâng cao: kết hợp ít nhất hai khái niệm;
- Thử thách: tình huống mở có nhiều phương án.

Rubric mặc định, tổng 100 điểm:

- Đúng chức năng: 35;
- An toàn và xử lý lỗi: 25;
- Chất lượng code/tài liệu: 20;
- Phân tích, giải thích và bằng chứng chạy: 20.

Mỗi tiêu chí mô tả mức đạt, không đạt và bằng chứng cần nộp. Không chấm dựa trên số dòng code.

Final project phải có bài toán, phạm vi, yêu cầu chức năng/phi chức năng, milestone, deliverables, demo script, threat model/risk assessment, rubric 100 điểm và tiêu chí thất bại bắt buộc.

### 7. Điều hướng và giao diện

- Giữ tên `week01` đến `week10`.
- Đường dẫn khóa chứa hậu tố `-10weeks`.
- Dùng layout `course` để nhận sidebar, mục lục, điều hướng tuần, bài trước/sau và IDE code viewer.
- Kiểm tra Lesson, Code, Exercise và Project giữ đúng tuần.
- Không nhúng JS/CSS riêng vào bài nếu tính năng dùng chung được.

### 8. Quality gates

Chỉ báo hoàn thành sau khi chạy các gate phù hợp:

1. `git diff --check`.
2. Build Jekyll:

```bash
JEKYLL_NO_BUNDLER_REQUIRE=true bundle exec jekyll build --destination /tmp/cyberlearn-site-check
```

3. Kiểm tra đủ 10 bài và README/code theo kế hoạch.
4. Biên dịch/chạy code với warning nghiêm ngặt khi có compiler.
5. Python: `python -m py_compile` và test phù hợp.
6. JavaScript: `node --check` và test phù hợp.
7. Kiểm tra HTML đầu ra có đúng số code block, mô tả và link.
8. Rà secret; không in secret ra log.
9. Rà an toàn: lab local, quyền sở hữu/ủy quyền, không có mục tiêu thật.
10. Báo rõ gate nào chưa chạy được và lý do.

## Nguyên tắc chỉnh sửa

- Dùng `apply_patch` để sửa file.
- Bảo toàn thay đổi không liên quan.
- Không tự commit, push hoặc deploy nếu người dùng chưa yêu cầu.
- Khi xuất bản, chỉ stage đúng file trong phạm vi.
- Nếu build cần network, xin quyền trước khi tải dependency.
- Không nói trang live đã cập nhật nếu chưa kiểm tra URL.

## Tiêu chuẩn bàn giao

Tóm tắt khóa/tuần/file đã cập nhật; số bài, code, bài tập và rubric; quyết định thiết kế; các kiểm tra đã chạy; trạng thái local/commit/deploy; phần còn thiếu hoặc rủi ro thực tế.

