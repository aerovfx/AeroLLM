# Tuần 07 · Bài 02: Tensor PyTorch căn bản.
# Mục tiêu: Tạo tensor, đọc shape/dtype, đổi hình reshape, sinh ngẫu nhiên có seed.
# Đầu vào: Các tensor giả khai báo trong code.
# Đầu ra: Shape, dtype, tensor đổi hình và tensor ngẫu nhiên.
# Cách chạy: python code/week07/02_tensor_basics.py
# Lưu ý an toàn: Chạy trên CPU; không cần GPU; seed chỉ để tái lập, không phải bảo mật.

# Import PyTorch với bí danh torch.
import torch


def main():
    # Tạo tensor 2x3 từ danh sách lồng nhau.
    t = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print("Tensor t:")
    print(t)

    # .shape cho kích thước; .dtype cho kiểu số của phần tử.
    print("shape:", t.shape)
    print("dtype:", t.dtype)

    # reshape đổi hình; -1 nghĩa là "tự suy ra chiều còn lại".
    print("\nreshape(3, 2):")
    print(t.reshape(3, 2))
    print("reshape(-1):", t.reshape(-1))  # Trải phẳng thành 1 chiều.

    # Tạo tensor kiểu float32 tường minh (thường cần cho học máy).
    f = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float32)
    print("\nTensor float32 dtype:", f.dtype)

    # Sinh tensor ngẫu nhiên tái lập được bằng Generator + manual_seed.
    g = torch.Generator().manual_seed(42)   # Seed cố định 42.
    r = torch.rand(3, generator=g)          # 3 số ngẫu nhiên trong [0, 1).
    print("\n3 số ngẫu nhiên (seed 42):", r)

    # Truy cập phần tử: t[0, 1] và hàng t[1] (liên hệ slicing tuần 6).
    print("t[0, 1] =", t[0, 1].item())
    print("t[1]    =", t[1])


if __name__ == "__main__":
    main()
