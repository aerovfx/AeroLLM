# Tuần 7: Transformer Block & Architecture — Review Questions

1. Vẽ sơ đồ luồng dữ liệu đi qua một khối Transformer Block hoàn chỉnh. Đâu là vị trí đặt của LayerNorm và Residual Connection?
2. Tại sao kết nối dòng dư $x + f(x)$ lại giải quyết được vấn đề biến mất gradient khi huấn luyện mô hình sâu? (Gợi ý: Tính đạo hàm của biểu thức $x + f(x)$ theo $x$).
3. Một mô hình GPT có 6 layer, mỗi layer có 1 khối Multi-Head Attention và 1 khối MLP. Hãy ước lượng xem lớp nào chiếm nhiều tham số (weights) nhất trong mô hình.
