# AeroLLM Course Blueprint

## Checklist trước khi tạo

- [ ] Tên khóa, slug và category đã xác định.
- [ ] Chân dung học viên và prerequisite rõ ràng.
- [ ] Mục tiêu cuối khóa đo được.
- [ ] Công cụ chạy trên nền tảng mục tiêu.
- [ ] Phạm vi pháp lý/an toàn rõ ràng.
- [ ] Lộ trình 10 tuần không trùng lặp.

## Ma trận thiết kế tuần

| Trường | Nội dung cần điền |
|---|---|
| Tuần | 01–10 |
| Chủ đề | Một năng lực chính |
| Mục tiêu | 3–6 động từ đo được |
| Lý thuyết | Khái niệm bắt buộc |
| Demo | Ví dụ nhỏ có kết quả |
| Lab | Hoạt động có giới hạn an toàn |
| Code | Danh sách file và chức năng riêng |
| Bài tập | Cơ bản / nâng cao / thử thách |
| Bằng chứng | Log, ảnh, report, source hoặc test |
| Rubric | Tiêu chí và trọng số |
| Liên kết | Tuần trước / tuần sau |

## Mẫu đầu file code

```text
// Tuần NN · Bài NN: Tên bài.
// Mục tiêu: Người học hiểu/làm được điều gì.
// Đầu vào: Dữ liệu hoặc tham số nào.
// Đầu ra: Kết quả mong đợi.
// An toàn: Chỉ chạy local/lab được ủy quyền; giới hạn quan trọng.
```

Chú thích theo khối logic. Tránh chú thích vô ích nếu không giải thích lý do hoặc rủi ro.

## Mẫu README code theo tuần

````markdown
---
layout: course
title: "Code WeekNN"
permalink: /<category>/<course>-10weeks/code/weekNN/README.html
---

# Tuần NN — Code minh họa

## 01_example.ext

**Chức năng:** Nhận ..., xử lý ..., và trả về ...

**Chạy:** `command 01_example.ext`

**Kết quả mong đợi:** Mô tả ngắn.

```language
{% include_relative 01_example.ext %}
```
````

## Mẫu rubric bốn mức

| Tiêu chí | Xuất sắc | Đạt | Cần cải thiện | Chưa đạt | Điểm |
|---|---|---|---|---|---:|
| Đúng chức năng | Đủ và đúng edge case | Đúng luồng chính | Thiếu một phần | Không chạy | 35 |
| An toàn | Validate, least privilege, cleanup | Có kiểm soát chính | Thiếu guardrail | Có hành vi nguy hiểm | 25 |
| Code và tài liệu | Rõ, test được, chú thích đúng | Dễ đọc | Khó bảo trì | Không giải thích | 20 |
| Phân tích và bằng chứng | Lập luận và log đầy đủ | Có bằng chứng | Bằng chứng yếu | Không có | 20 |

## Gate kiểm tra cấu trúc

```bash
find <course>/lessons -name 'week*.md' | wc -l
find <course>/code -path '*/week*/README.md' | wc -l
rg -n 'layout: course|permalink:' <course>
git diff --check
```

Chọn compiler/interpreter gate theo ngôn ngữ thực tế. Không dùng một lệnh chung rồi tuyên bố mọi code đều chạy được.
