# Giai Đoạn III: Hậu Huấn Luyện & Hiệu Chỉnh (Alignment)

Mô hình tiền huấn luyện của bạn là một "mô hình cơ sở" (base model)—nó là một công cụ dự đoán token tiếp theo mạnh mẽ, nhưng nó không phải là một trợ lý hữu ích. Hậu huấn luyện (Post-training) sẽ hiệu chỉnh nó để tuân theo các hướng dẫn.

Trước khi bạn bắt đầu, hãy xác định các chỉ số (metrics) và bộ dữ liệu đánh giá của bạn. Làm thế nào bạn sẽ biết liệu SFT hoặc RLHF của bạn có phải là một cải tiến hay không? Sử dụng kết hợp các đánh giá tự động (ví dụ: LLM-làm-giám-khảo) và đánh giá của con người.

## Tinh chỉnh có Giám sát (Supervised Fine-Tuning - SFT)​

**Mục đích:** Để dạy mô hình cách phản hồi. Bạn đang thay đổi hành vi của nó từ "tiếp tục văn bản này" thành "trả lời hướng dẫn này."

**Dữ liệu:** Điều này dựa trên một bộ dữ liệu nhỏ hơn, chất lượng cao gồm các cặp hướng dẫn-phản hồi.
Ví dụ:

`{  "instruction": "Thủ đô của Pháp là gì?",   "response": "Thủ đô của Pháp là Paris."}`

Chất lượng và sự đa dạng của dữ liệu quan trọng hơn nhiều so với kích thước.

## Tối ưu hóa Sở thích (Preference Optimization - RL)​

**Mục đích:** Để làm cho các phản hồi của mô hình tốt hơn (hữu ích hơn, trung thực hơn và vô hại hơn).

**Dữ liệu:** Điều này đòi hỏi một bộ dữ liệu sở thích, trong đó mỗi mục hiển thị hai hoặc nhiều phản hồi cho một câu lệnh (prompt), được xếp hạng từ tốt nhất đến tệ nhất.

**Phương pháp:** Điều này thường được thực hiện bằng Học Tăng cường (RL), chẳng hạn như RLHF (từ Phản hồi của Con người) hoặc RLAIF (từ Phản hồi của AI). Điều này liên quan đến việc huấn luyện một "Mô hình Phần thưởng" (Reward Model) trên dữ liệu sở thích của bạn, mô hình này sau đó sẽ "chấm điểm" các đầu ra của mô hình SFT và dạy nó tạo ra các phản hồi được điểm cao hơn.

> [Kiểm tra sự "Nhiễm bẩn" Dữ liệu (Contamination)!]
> Bạn phải đảm bảo rằng dữ liệu đánh giá của bạn (đặc biệt là từ các benchmark) không có mặt trong dữ liệu huấn luyện hoặc SFT của bạn. Nếu có, điểm số cao của bạn là không hợp lệ.
