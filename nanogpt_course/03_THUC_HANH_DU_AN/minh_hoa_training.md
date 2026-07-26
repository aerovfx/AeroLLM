# MINH HỌA QUY TRÌNH HUẤN LUYỆN (TRAINING PROCESS)
> **Tài liệu tham chiếu:** Mã nguồn Python [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py) và Sổ tay Jupyter [mini_gpt.ipynb](file:///file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.ipynb) trong thư mục `docs/`.

---

Quy trình huấn luyện (Training) là giai đoạn quan trọng nhất giúp bộ não AI chuyển từ trạng thái "đoán mò ngẫu nhiên" sang "viết chữ thông minh". Dưới đây là phân tích chi tiết từng khối mã nguồn PyTorch minh họa cho quá trình này.

---

## 📊 1. Chuẩn bị dữ liệu lô (Batching Data)

Máy tính không nạp toàn bộ tệp dữ liệu 1MB cùng một lúc vì sẽ gây quá tải bộ nhớ. Thay vào đó, nó chia dữ liệu thành các lô nhỏ (batches) nhờ hàm `get_batch` trong [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py#L37-L42):

```python
def get_batch(split):
    d = train_data if split == 'train' else val_data
    ix = torch.randint(len(d) - block_size, (batch_size,))
    x = torch.stack([d[i:i+block_size]     for i in ix])
    y = torch.stack([d[i+1:i+1+block_size] for i in ix])
    return x.to(device), y.to(device)
```

### 🔍 Giải thích cơ chế:
*   `ix`: Chọn ngẫu nhiên `batch_size` (32) vị trí bắt đầu trong văn bản.
*   `x` (Đầu vào): Đoạn văn gồm `block_size` (64) ký tự bắt đầu từ chỉ số ngẫu nhiên `i`.
*   `y` (Nhãn đáp án đúng): Đoạn văn tương ứng nhưng dịch chuyển sang phải 1 bước ký tự (`i+1` đến `i+1+block_size`).
*   `.to(device)`: Đẩy dữ liệu từ CPU lên card đồ họa (GPU) để tăng tốc độ tính toán song song.

---

## ⚙️ 2. Khởi tạo mô hình và Bộ tối ưu (Optimizer)

Đoạn code khởi tạo mô hình và thuật toán cập nhật trọng số trong [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py#L118-L121):

```python
model = MiniGPT().to(device)
print("So tham so / params: %.2fK" % (sum(p.numel() for p in model.parameters())/1e3))
opt = torch.optim.AdamW(model.parameters(), lr=lr)
```

### 🔍 Giải thích cơ chế:
*   `MiniGPT().to(device)`: Dựng khung bộ não AI và đưa toàn bộ trọng số lên thiết bị xử lý (GPU/CPU).
*   `AdamW`: Bộ tối ưu hóa (Optimizer) chịu trách nhiệm tính toán xem nên điều chỉnh trọng số như thế nào dựa trên độ dốc sai số (Gradient).
*   `lr=lr` (Learning Rate = `1e-3`): Tốc độ học tập. Mỗi bước chỉnh trọng số sẽ nhân với hệ số nhỏ này để tránh làm mô hình bị mất ổn định.

---

## 🔄 3. Vòng lặp huấn luyện cốt lõi (The Training Loop)

Mọi phép toán cập nhật tri thức diễn ra tuần tự trong vòng lặp chính của [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py#L133-L138):

```python
for it in range(max_iters):
    # 1. Lấy dữ liệu ngẫu nhiên
    xb, yb = get_batch('train')
    
    # 2. Dự đoán và Tính sai số (Forward Pass)
    _, loss = model(xb, yb)
    
    # 3. Xoá lịch sử gradient cũ
    opt.zero_grad(set_to_none=True)
    
    # 4. Tính toán độ dốc sai số (Backward Pass)
    loss.backward()
    
    # 5. Cập nhật tham số (Weight Update)
    opt.step()
```

### 🔍 Luồng đi chi tiết của 1 bước lặp (Iteration):
1.  **Forward Pass (`model(xb, yb)`):** Dữ liệu `xb` đi qua các lớp Embedding, Attention và MLP. Mô hình đưa ra điểm số dự đoán cho ký tự tiếp theo và so sánh với đáp án đúng `yb` để tính chỉ số `loss` (Cross-Entropy).
2.  **Zero Grad (`opt.zero_grad`):** PyTorch mặc định tích lũy cộng dồn gradient qua các lượt. Do đó, ta phải xóa sạch lịch sử gradient của bước trước để bắt đầu tính toán cho bước mới.
3.  **Backward Pass (`loss.backward()`):** Chạy lan truyền ngược sai số từ đầu ra ngược về các tầng nơ-ron trước đó, tính toán đạo hàm riêng của Loss đối với từng tham số.
4.  **Optimizer Step (`opt.step()`):** AdamW thực hiện điều chỉnh giá trị các tham số theo hướng ngược chiều với Gradient để kéo chỉ số Loss giảm xuống ở lần sau.

---

## 📊 4. Đánh giá định kỳ (Periodic Evaluation)

Để biết mô hình học thật hay học vẹt (overfitting), ta thỉnh thoảng đo Loss trên tập dữ liệu kiểm thử (Validation) bằng hàm `est_loss` trong [mini_gpt.py](file:///Users/dangvietchung/Aero-HowtoLLMs/docs/mini_gpt.py#L123-L131):

```python
@torch.no_grad()
def est_loss():
    model.eval()
    out = {}
    for split in ['train', 'val']:
        losses = torch.zeros(eval_iters)
        for k in range(eval_iters):
            _, l = model(*get_batch(split))
            losses[k] = l.item()
        out[split] = losses.mean().item()
    model.train()
    return out
```

### 🔍 Giải thích cơ chế:
*   `@torch.no_grad()`: Tắt tính năng tự động ghi nhớ đồ thị đạo hàm của PyTorch. Vì ở bước đánh giá ta chỉ cần tính toán xem Loss là bao nhiêu, không cần cập nhật trọng số, việc tắt này giúp tiết kiệm 70% bộ nhớ GPU.
*   `model.eval()`: Chuyển mô hình sang chế độ đánh giá (tắt các cơ chế ngẫu nhiên như Dropout).
*   `model.train()`: Sau khi đo xong, phải chuyển mô hình quay lại chế độ huấn luyện để tiếp tục vòng lặp học tập.
