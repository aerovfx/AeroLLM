# Nguồn chính thức / Primary sources

[Trang khoá học](../INDEX.md)

## Nguồn bắt buộc

1. [Kimi K3 Technical Report (PDF)](https://github.com/MoonshotAI/Kimi-K3/blob/main/k3_tech_report.pdf) — nguồn chính cho kiến trúc, training, infrastructure và evaluation.
2. [MoonshotAI/Kimi-K3 repository](https://github.com/MoonshotAI/Kimi-K3) — model summary, usage, deployment và license.
3. [Kimi-K3 model card trên Hugging Face](https://huggingface.co/moonshotai/Kimi-K3) — files, config và integration hiện hành.
4. [Kimi K3 config.json](https://huggingface.co/moonshotai/Kimi-K3/blob/main/config.json) — kiểm tra cấu hình máy đọc được.
5. [Kimi Linear](https://github.com/MoonshotAI/Kimi-Linear) — nền tảng KDA được report K3 viện dẫn.
6. [Kimi K2 Technical Report](https://arxiv.org/abs/2507.20534) và [Kimi K2.5](https://arxiv.org/abs/2602.02276) — baseline lịch sử cho các claim “so với K2/K2.5”.

Xem [hướng dẫn repository](../REPOSITORY_GUIDE.md) để phân biệt tài sản trong GitHub/Hugging Face, audit license, preserved history và `trust_remote_code`.

## Quy tắc trích dẫn

- Ghi rõ “Kimi Team reports/nhóm Kimi báo cáo” với claim nội bộ, scaling curve và in-house benchmark.
- Không so điểm giữa các harness khác nhau như thể đó là thí nghiệm kiểm soát.
- Ghi ngày truy cập cho leaderboard động.
- Phân biệt open-weight với open-source; kiểm tra [Kimi K3 License](https://github.com/MoonshotAI/Kimi-K3/blob/main/LICENSE) trước mọi phân phối hoặc thương mại hoá. License có điều kiện riêng cho Model-as-a-Service/doanh thu lớn và attribution ở quy mô sản phẩm lớn.
