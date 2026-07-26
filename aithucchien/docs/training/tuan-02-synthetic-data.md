# Tuần 2: Kỹ thuật Tạo Dữ liệu Tổng hợp (Synthetic Data)

Dữ liệu chất lượng cao quyết định sự thông minh của mô hình. Trong tuần này, chúng ta sẽ học cách tự sinh tập dữ liệu hướng dẫn bằng LLM.

## Các thuật toán sinh dữ liệu phổ biến
1. **Self-Instruct (Alpaca):** Sử dụng mô hình lớn tự sinh câu lệnh (prompt) và câu trả lời tương ứng từ một tập hạt giống nhỏ.
2. **Evol-Instruct (WizardLM):** Nâng cấp độ phức tạp của câu lệnh theo chiều sâu hoặc chiều rộng bằng cách ra lệnh cho LLM sửa câu lệnh cũ khó hơn.
3. **Magpie:** Tận dụng trực tiếp khả năng sinh câu lệnh tự nhiên của các mô hình Instruct để trích xuất hội thoại chất lượng lớn.
4. **Persona-driven:** Tạo ra 1 tỷ nhân vật giả lập để sinh các góc nhìn đa chiều của dữ liệu web.
