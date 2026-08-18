---
layout: course
title: "Readme"
permalink: /1_Foundations/python-math-foundations-10weeks/code/README.html
---

# Code lab — Python & Toán nền tảng

[← Khoá học](../INDEX.md) · [Yêu cầu máy](../../../courses/COMPUTER_REQUIREMENTS.md)

## Cài đặt / Setup

```bash
python -m venv .venv && source .venv/bin/activate   # macOS/Linux
pip install numpy matplotlib torch
```

Hoặc cài theo `requirements.txt` ở gốc repo. Các tuần 1–4, 6 chỉ cần Python chuẩn; tuần 3, 5, 6, 8, 9 cần NumPy (và Matplotlib cho 5, 9); tuần 7, 10 cần PyTorch.

## Bản đồ code theo tuần / Code map

| Tuần | File | Chức năng |
|---:|---|---|
| 1 | [`week01/01_hello_python.py`](week01/01_hello_python.py) | Chào + in phiên bản Python |
| 1 | [`week01/02_environment_check.py`](week01/02_environment_check.py) | Kiểm tra môi trường Python |
| 2 | [`week02/01_data_types.py`](week02/01_data_types.py) | Kiểu dữ liệu và `type()` |
| 2 | [`week02/02_containers.py`](week02/02_containers.py) | list/dict và truy cập phần tử |
| 3 | [`week03/01_functions.py`](week03/01_functions.py) | Định nghĩa và gọi hàm |
| 3 | [`week03/02_numpy_random.py`](week03/02_numpy_random.py) | Số ngẫu nhiên có seed |
| 4 | [`week04/01_loops_and_conditions.py`](week04/01_loops_and_conditions.py) | for/if-else |
| 4 | [`week04/02_comprehension_enumerate_zip.py`](week04/02_comprehension_enumerate_zip.py) | comprehension/enumerate/zip |
| 5 | [`week05/01_strings_text.py`](week05/01_strings_text.py) | f-string và xử lý text |
| 5 | [`week05/02_plotting.py`](week05/02_plotting.py) | Vẽ biểu đồ + subplot |
| 6 | [`week06/01_indexing_slicing.py`](week06/01_indexing_slicing.py) | Indexing/slicing list, chuỗi |
| 6 | [`week06/02_numpy_slicing.py`](week06/02_numpy_slicing.py) | Slicing mảng NumPy |
| 7 | [`week07/01_classes_objects.py`](week07/01_classes_objects.py) | Class và đối tượng |
| 7 | [`week07/02_tensor_basics.py`](week07/02_tensor_basics.py) | Tensor, shape, reshape, random |
| 8 | [`week08/01_vector_matrix.py`](week08/01_vector_matrix.py) | Dot product, tổ hợp tuyến tính, ma trận |
| 8 | [`week08/02_softmax_entropy.py`](week08/02_softmax_entropy.py) | Softmax, entropy, cross-entropy |
| 9 | [`week09/01_gradient_descent_1d.py`](week09/01_gradient_descent_1d.py) | GD 1D + so sánh learning rate |
| 9 | [`week09/02_gradient_descent_2d.py`](week09/02_gradient_descent_2d.py) | GD 2D + dynamic LR |
| 10 | [`week10/01_perceptron.py`](week10/01_perceptron.py) | Perceptron thủ công |
| 10 | [`week10/02_linear_regression_pytorch.py`](week10/02_linear_regression_pytorch.py) | Forward/backward bằng autograd |

Mỗi file tự chạy độc lập, ví dụ:

```bash
python code/week01/01_hello_python.py
```

> Mọi script dùng dữ liệu giả/local, không chứa secret/token. Xem `weekNN/README.md` để biết đầu vào, đầu ra và kết quả mong đợi của từng tuần.
