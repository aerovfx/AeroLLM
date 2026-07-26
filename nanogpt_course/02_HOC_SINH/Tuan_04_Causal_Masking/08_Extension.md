# Tuần 4: Causal Masking — Extension Material
> **Chủ đề mở rộng:** Cách hoạt động của hàm `torch.tril` và phép biến đổi Softmax trên các giá trị cực biên.

---

Trong PyTorch, ma trận mặt nạ được tạo bằng hàm `torch.tril`:
```python
tril = torch.tril(torch.ones(block_size, block_size))
```
Phép toán điền mặt nạ được thực hiện trên ma trận điểm số chú ý `att` (tích vô hướng của Query và Key):
```python
att = att.masked_fill(tril[:T, :T] == 0, float('-inf'))
```
Khi tính Softmax cho một hàng $i$ bất kỳ:
$$S_j = rac{e^{att_{ij}}}{\sum_{k=1}^{T} e^{att_{ik}}}$$
Đối với mọi vị trí $j > i$ (tương lai), $att_{ij} = -\infty$. 
Vì $e^{-\infty} = 0$, tử số của các vị trí này bằng 0, dẫn đến xác suất chú ý $S_j = 0$. Điều này loại bỏ hoàn toàn ảnh hưởng của các token tương lai ra khỏi phép cộng thông tin Value ở bước tiếp theo:
$$y_i = \sum_{j=1}^{T} S_j v_j = \sum_{j=1}^{i} S_j v_j$$
