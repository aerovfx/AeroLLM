# Tuần 6: Multi-Head Attention & Lớp MLP — Review Questions

1. Tại sao ta không dùng một đầu attention lớn có số chiều $768$ mà lại chia thành 12 đầu nhỏ có số chiều $64$? Lợi ích của việc chạy song song là gì?
2. Hàm kích hoạt phi tuyến tính (như GELU) có vai trò gì trong lớp MLP? Nếu bỏ hàm kích hoạt này đi và chỉ dùng các phép nhân tuyến tính (`nn.Linear`), bộ não AI sẽ gặp giới hạn gì?
3. Tại sao trong lớp MLP, số chiều dữ liệu thường được nở rộng lên gấp 4 lần (`4 * n_embd`) trước khi nén lại?
