---
layout: course
title: "Repository Guide"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/REPOSITORY_GUIDE.html
---

# Hướng dẫn dùng repository chính thức MoonshotAI/Kimi-K3

[Trang khoá học](INDEX.md) · [Nguồn](references/README.md) · [Code lab](code/README.md)

**Đối chiếu ngày:** 28/07/2026  
**Repository:** <https://github.com/MoonshotAI/Kimi-K3>

## 1. Repository cung cấp gì?

Tại thời điểm đối chiếu, repository GitHub chính thức có bốn nhóm tài sản chính:

| Tài sản | Dùng trong khoá học | Không nên suy diễn |
|---|---|---|
| `README.md` | model summary, benchmark protocol, deployment và usage | Không phải training recipe đầy đủ |
| `k3_tech_report.pdf` | kiến trúc, pre/post-training, infrastructure, evaluation | Không đủ artifact để reproduce 2.8T training |
| `LICENSE` | quyền, nghĩa vụ attribution/commercial conditions | Không thay thế tư vấn pháp lý |
| `assets/` | hình minh hoạ/model overview | Không phải code implementation |

Mã custom Transformers, config, tokenizer và weight shards nằm ở [Hugging Face model repository](https://huggingface.co/moonshotai/Kimi-K3), không nằm trong GitHub report repository. Vì vậy học viên phải ghi riêng hai nguồn trong manifest.

## 2. Model facts cần kiểm tra bằng cả report và config

| Trường | Giá trị công bố | Nguồn kiểm tra |
|---|---:|---|
| Total / activated parameters | 2.8T / 104B | README/report |
| Layers | 93 | README/config |
| Hybrid attention | 69 KDA + 24 Gated MLA | README/config `kda_layers`, `full_attn_layers` |
| Hidden size / heads / head dim | 7168 / 96 / 128 | config |
| AttnRes block size | 12 | config |
| Routed / selected / shared experts | 896 / 16 / 2 | README/config |
| Latent MoE / expert hidden width | 3584 / 3072 | README/config |
| Context | 1,048,576 | README/config `max_position_embeddings` |
| KDA gate lower bound | -5.0 | report/config |
| SiTU parameters | 4.0 và 25.0 | report/config |
| Vision encoder | MoonViT-V2, khoảng 401M | README/report |

Không lấy `dtype: bfloat16` trong config để phủ định MXFP4/MXFP8: config dtype mô tả model/runtime interface, còn report nói routed expert weights và expert activations dùng quantization-aware mixed formats trong deployment-aware post-training.

## 3. License checklist

Kimi K3 License cho phép sử dụng, sao chép, sửa đổi, phân phối, sublicense, bán, deploy và fine-tune, nhưng có điều kiện. Trước khi release bài tập hoặc sản phẩm:

- giữ copyright notice và permission notice trong bản sao/phần đáng kể;
- tuân thủ pháp luật hiện hành;
- nếu vận hành **Model as a Service** và tổng doanh thu nhóm công ty vượt 20 triệu USD trong 12 tháng liên tiếp, phải có thỏa thuận riêng với Moonshot AI trước khi dùng thương mại;
- sản phẩm/dịch vụ thương mại vượt 100 triệu MAU hoặc 20 triệu USD doanh thu tháng phải hiển thị nổi bật “Kimi K3”;
- đọc các ngoại lệ cho internal use và truy cập qua sản phẩm chính thức/certified partners;
- ghi nhận phần mềm/output được cung cấp “as is”, không có bảo hành.

Checklist trên là tóm tắt phục vụ học tập; khi triển khai thật phải đọc nguyên văn `LICENSE` và xin tư vấn phù hợp.

## 4. API và preserved thinking history

Model card ghi Kimi K3 luôn bật thinking, trả `reasoning_content` và hỗ trợ `reasoning_effort` ở `low`, `high`, `max` (mặc định `max`). Với multi-turn/tool calls, client phải đưa **toàn bộ assistant message** của lượt trước trở lại `messages`, gồm `reasoning_content`, `content` và `tool_calls`.

Quy tắc triển khai cho lab:

1. Không tự viết lại hoặc cắt bỏ assistant message trước khi nối history.
2. Không in `reasoning_content` vào console, telemetry hoặc bài nộp; coi nó là dữ liệu nhạy cảm.
3. Redact secrets/PII trước request và đặt retention policy cho conversation history.
4. Ghi `reasoning_effort`, sampling, tools, model identifier và timestamp trong evaluation manifest.
5. Dùng [payload builder](code/python/preserved_history_payload.py) để học cấu trúc offline; không cần API key.

## 5. Deployment paths

README chính thức nêu bốn đường:

- API `kimi-k3` trên Kimi platform với OpenAI/Anthropic-compatible interface;
- vLLM;
- SGLang;
- TokenSpeed.

Hugging Face còn trình bày Transformers/custom code và Docker integrations. Những snippet “serve model” chỉ mô tả interface; chúng **không đảm bảo** máy cá nhân đủ bộ nhớ hoặc engine/hardware hiện tại hỗ trợ mọi kernel/quantization path. Phải chạy capacity gate trước download và deployment.

## 6. Security gate khi dùng custom code

Model card sử dụng `trust_remote_code=True`. Điều đó cho phép chạy Python từ model repository trong môi trường local. Lab production phải:

- pin một commit revision thay vì phụ thuộc `main`;
- review `modeling_*.py`, `configuration_*.py` và dependency changes;
- chạy trong container/VM ít quyền, không mount secrets hoặc home directory;
- xác minh source/weight manifests và chỉ cho phép outbound network cần thiết;
- không chạy full-model load chỉ để đọc config—tải/đọc `config.json` riêng là đủ.

## 7. Repository audit assignment

Học viên nộp manifest gồm URL, commit/revision, ngày truy cập, file/sha256, license version, model config fields, engine/version và phần nào chưa được public. Mọi claim reproduction phải nêu rõ artifact cần thiết có thực sự tồn tại trong repository hay không.

