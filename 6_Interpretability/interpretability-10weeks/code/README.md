---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/code/README.html
---

# Code lab — Interpretability (mech interp)

[Khoá học](../INDEX.md) · [Ánh xạ tài liệu](../references/README.md)

Tất cả code chạy độc lập bằng **Python 3 + NumPy** trên dữ liệu/mô hình giả (không tải model lớn thật, không cần token/secret). Mỗi tuần có 1–2 file `.py` có chú thích tiếng Việt ở đầu (mục tiêu, đầu vào, đầu ra, cách chạy, an toàn).

| Tuần | File | Nội dung |
|---:|---|---|
| 1 | [`week01/01_residual_stream.py`](week01/01_residual_stream.py) | Mô phỏng residual stream |
| 1 | [`week01/02_linear_probe_baseline.py`](week01/02_linear_probe_baseline.py) | Linear probe & baseline tuyến tính |
| 2 | [`week02/01_sparse_probe.py`](week02/01_sparse_probe.py) | Sparse probing (logistic + L1) |
| 2 | [`week02/02_sae_toy.py`](week02/02_sae_toy.py) | Sparse autoencoder tối giản |
| 3 | [`week03/01_cosine_similarity.py`](week03/01_cosine_similarity.py) | Cosine similarity + heatmap |
| 3 | [`week03/02_analogy_arithmetic.py`](week03/02_analogy_arithmetic.py) | Analogy + trục ngữ nghĩa |
| 4 | [`week04/01_activation_maximization.py`](week04/01_activation_maximization.py) | Activation maximization |
| 4 | [`week04/02_neuron_selectivity.py`](week04/02_neuron_selectivity.py) | Logistic regression vs t-test |
| 5 | [`week05/01_effective_dimensionality.py`](week05/01_effective_dimensionality.py) | Effective dimensionality (PCA) |
| 5 | [`week05/02_logit_lens.py`](week05/02_logit_lens.py) | Logit lens theo tầng |
| 6 | [`week06/01_activation_editing.py`](week06/01_activation_editing.py) | Zero/mean/median/noise edit |
| 6 | [`week06/02_counterfactual_patching.py`](week06/02_counterfactual_patching.py) | Counterfactual patching |
| 7 | [`week07/01_activation_patching_ioi.py`](week07/01_activation_patching_ioi.py) | Activation patching + IOI |
| 7 | [`week07/02_skip_layer.py`](week07/02_skip_layer.py) | Bỏ qua một tầng |
| 8 | [`week08/01_head_ablation.py`](week08/01_head_ablation.py) | Head ablation |
| 8 | [`week08/02_head_patching_ioi.py`](week08/02_head_patching_ioi.py) | Head patching trong IOI |
| 9 | [`week09/01_median_replacement.py`](week09/01_median_replacement.py) | Median replacement + ripple-rate |
| 9 | [`week09/02_subspace_removal.py`](week09/02_subspace_removal.py) | Subspace removal |
| 10 | [`week10/01_trajectory_pca.py`](week10/01_trajectory_pca.py) | PCA trajectories (common space) |
| 10 | [`week10/02_path_length.py`](week10/02_path_length.py) | Path length residual stream |

## Chạy nhanh

```bash
# Kiểm tra môi trường (chỉ cần NumPy)
python -c "import numpy; print(numpy.__version__)"

# Chạy một ví dụ
python 6_Interpretability/interpretability-10weeks/code/week01/01_residual_stream.py
```

Mỗi thư mục `weekNN/` có `README.md` kèm lệnh chạy và kết quả mong đợi chi tiết.
