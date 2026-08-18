---
layout: course
title: "Readme"
permalink: /4_Training/openweight-training-pipeline-10weeks/code/colab/README.html
---

# Colab workflow — Pipeline training

Colab phù hợp cho reduced experiment, không phù hợp reproduction nhiều GPU hoặc target cache cực lớn.

1. Chạy notebook planning/audit bằng CPU trước.
2. Với CPT/SFT nhỏ, pin model/dataset revision và ghi GPU/VRAM/runtime limit.
3. Lưu checkpoint thường xuyên vào Drive hoặc artifact store; Colab runtime có thể bị thu hồi.
4. Không chạy DDP/FSDP/DeepSpec default trên Colab.
5. Nếu job không vừa một GPU, nộp capacity plan + smoke test thay vì tìm cách vượt quota.
