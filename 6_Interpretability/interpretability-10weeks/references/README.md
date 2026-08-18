---
layout: course
title: "Readme"
permalink: /6_Interpretability/interpretability-10weeks/references/README.html
---

# Ánh xạ tuần → module docs nguồn

Khoá học diễn giải lại lý thuyết cốt lõi từ các module `docs/` của repo, không chép nguyên văn. Bảng dưới ánh xạ từng tuần tới tài liệu nguồn tương ứng để đọc sâu.

| Tuần | Chủ đề | Module nguồn |
|---:|---|---|
| 1 | Nhập môn interpretability & phương pháp | [`docs/15_interpretability/index.md`](../../../docs/15_interpretability/index.md) |
| 2 | Identifying circuits | [`docs/10_identifying_circuits/index.md`](../../../docs/10_identifying_circuits/index.md) |
| 3 | Token embeddings I: probing | [`docs/11_investigating_token_embeddings/index.md`](../../../docs/11_investigating_token_embeddings/index.md) |
| 4 | Neurons và dimensions | [`docs/12_investigating_neurons_dimensions/index.md`](../../../docs/12_investigating_neurons_dimensions/index.md) |
| 5 | Layers | [`docs/13_investigating_layers/index.md`](../../../docs/13_investigating_layers/index.md) |
| 6 | Modify activations | [`docs/14_modify_activations/index.md`](../../../docs/14_modify_activations/index.md) |
| 7 | Editing hidden states | [`docs/15_editing_hidden_states/index.md`](../../../docs/15_editing_hidden_states/index.md) |
| 8 | Interfering with attention | [`docs/16_interfering_with_attention/index.md`](../../../docs/16_interfering_with_attention/index.md) |
| 9 | Modifying MLP | [`docs/17_modifying_mlp/index.md`](../../../docs/17_modifying_mlp/index.md) |
| 10 | Token embeddings II: trajectories + capstone | [`docs/20_investigating_token_embeddings/index.md`](../../../docs/20_investigating_token_embeddings/index.md) |

## Đọc sâu gợi ý theo tuần

- **Tuần 1**: "Mechanistic Interpretability là gì", "Mech interp và AI safety", "General criticisms".
- **Tuần 2**: "Sparse probing theory and code", "SAE theory and code", "Generalized Eigendecomposition".
- **Tuần 3**: "Cosine similarity in word sequences", "RSA", "Linear semantic axes", "Embeddings arithmetic and analogies".
- **Tuần 4**: "Activation maximization", "Extracting activations via hooks", "Logistic regression vs t-test".
- **Tuần 5**: "Effective dimensionality with PCA", "Logit lens", "Mutual information".
- **Tuần 6**: "Introduction to causal mech interp", "Activation editing implementations".
- **Tuần 7**: "Activation patching with IOI", "Skip a layer", "Downstream impact of early layer scaling".
- **Tuần 8**: "Head ablation and token prediction", "Head patching in IOI".
- **Tuần 9**: "Successive median-replacement of MLP neurons", "Statistics-based lesioning", "Subspace removal".
- **Tuần 10**: "State-space trajectories", "Path length and logit token prediction", "Residual stream path length decomposition".

## Tài liệu tham khảo ngoài repo (đọc thêm, không bắt buộc)

- Olah, C., et al. (2020). *Zoom In: An Introduction to Circuits.* Distill.
- Elhage, N., et al. (2021). *A Mathematical Framework for Transformer Circuits.* Transformer Circuits Thread.
- Nanda, N., et al. (2023). *Progress measures for grokking via mechanistic interpretability.* ICLR.
- Alain, G., & Bengio, Y. (2016). *Understanding intermediate layers using linear classifier probes.* ICLR Workshop.
