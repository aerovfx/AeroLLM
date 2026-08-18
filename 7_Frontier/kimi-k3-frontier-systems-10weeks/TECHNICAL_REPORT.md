---
layout: course
title: "Technical Report"
permalink: /7_Frontier/kimi-k3-frontier-systems-10weeks/TECHNICAL_REPORT.html
---

# Phân tích Kimi K3 Technical Report cho đào tạo 10 tuần

[Trang khoá học](INDEX.md) · [Nguồn](references/README.md)

**Phiên bản phân tích:** 28/07/2026  
**Phạm vi:** technical report 47 trang, model card/config và repository chính thức của Moonshot AI.  
**Loại bằng chứng:** các mô tả kiến trúc/training là công bố của nhóm phát triển; benchmark nội bộ chưa phải xác nhận độc lập.

## Tóm tắt kỹ thuật

Đóng góp quan trọng nhất của Kimi K3 không phải riêng con số 2.8T tham số. Report trình bày một thiết kế đồng bộ trên ba tầng:

1. **Information flow:** KDA xử lý chuỗi dài hiệu quả, Gated MLA định kỳ giữ tương tác global, AttnRes cho phép truy xuất theo chiều sâu, Stable LatentMoE mở rộng chiều rộng bằng sparse experts.
2. **Training-to-serving continuity:** native multimodal từ đầu, progressive context extension, SFT/RL có reasoning-effort, QAT từ SFT tới rollout và draft model cho speculative decoding.
3. **Agent systems:** dữ liệu là trajectory trong sandbox có tool, budget, persistent state và verifier; hạ tầng giữ KV/sandbox state để rollout triệu token có thể tạm dừng và tiếp tục.

Vì vậy, khóa học nên dạy K3 như một **systems case study**, không như một recipe fine-tune model thông thường. Học viên laptop chỉ tái tạo cơ chế ở quy mô toy và học cách kiểm chứng claim. Full weights 2.8T ở 4-bit đã có lower bound khoảng **1.40 TB chỉ cho weights**; 104B activated parameters giảm compute mỗi token nhưng không đồng nghĩa toàn bộ model vừa một GPU 104B.

## 1. Kiến trúc: ba trục token, depth và channel

### Sequence mixing: 3 KDA + 1 Gated MLA

Mỗi block lặp ba KDA layers rồi một Gated MLA; layer cuối backbone cũng là global attention. KDA dùng recurrent state và channel-wise forget gate, có chi phí state không tăng theo chiều dài như KV cache của full attention. K3 thay log-decay không bị chặn bằng

\[
g_t=g_{min}\,\sigma(e^A z_t),\qquad \alpha_t=\exp(g_t),\qquad g_{min}=-5,
\]

giữ retention trong \((e^{-5},1)\). Report lập luận giới hạn này cho phép diagonal tiles dùng dense Tensor Core matmul thay vì position-pair path. Gated MLA được chèn định kỳ để model vẫn có global token-to-token interaction và giảm KV cache nhờ latent representation.

**Diễn giải:** KDA và MLA bổ sung nhau; không nên dạy “linear attention thay thế hoàn toàn attention”. Lab tuần 2 đo recurrence correctness và numerical range, không tuyên bố tái tạo throughput của kernel gốc.

### Depth mixing: Attention Residuals

Residual chuẩn cộng dồn mọi layer vào một state. AttnRes dùng pseudo-query học được để attention lên embedding và outputs trước đó. Full AttnRes có arithmetic \(O(L^2d)\), nhưng giữ state/communication \(O(Ld)\); Block AttnRes gộp layer theo block để giảm phần này xuống \(O(Nd)\). K3 chia 93 layers thành các block size 12, báo cáo 8 blocks đầy đủ, một partial block và embedding source.

**Diễn giải:** lợi ích cốt lõi là đường truy cập thông tin theo depth có chọn lọc. Lab tuần 3 phải so learned depth weights với residual sum và nêu memory trade-off.

### Channel mixing: Stable LatentMoE

K3 có 896 routed experts, chọn 16/token, cộng hai shared experts. Routed experts hoạt động trong latent width 3584 thay vì hidden width 7168. Để ổn định extreme sparsity, report thêm:

- RMSNorm trước up-projection;
- SiTU-GLU với hai nhánh tanh-scaled để output bị chặn (report dùng \(\beta_1=4,\beta_2=25\), bound 100);
- Quantile Balancing (QB), giải balanced assignment qua alternating quantile updates; bias cuối được freeze ở inference.

**Diễn giải:** “16/896” là routing multiplicity/sparsity, không phải model chỉ nạp 16 experts. Week 4 dùng toy batch để phân biệt load balance, expert specialization và total parameter residency.

## 2. Dữ liệu và pre-training: native multimodal, không ghép hậu kỳ

Report chia text thành Web, Code, Mathematics và Knowledge; vision gồm caption, interleaved image–text, OCR, perception, video và visual coding. MoonViT-V2 khoảng 401M tham số/27 layers mã hoá ảnh và video; projector đưa visual features vào shared embedding space. Model joint-optimizes text và visual tokens ngay từ đầu bằng next-token prediction.

Training context tăng theo curriculum 8K → 64K trong pre-training, rồi 256K → 1M trong cooldown. NoPE tránh phải retune RoPE khi kéo dài context, nhưng report nhấn mạnh chiều dài tự thân không tạo long-range ability: dữ liệu phải đặt evidence/subtasks rải trên toàn context. Pipeline long data gồm exact/fuzzy dedup, structural validation, classifier/heuristic filtering và perceptual hash cho video.

Scaling-law curve báo cáo khoảng 2.5× scaling efficiency so với Kimi K2, nhưng đây là **kết quả tổng hợp** của architecture + data + training recipe trên fitted held-out OOD loss; report không cung cấp decomposition để gán mức tăng cho từng thành phần. Vì vậy khóa học dùng claim này để dạy thiết kế ablation, không dùng như hệ số speedup triển khai.

## 3. Post-training: chuyên môn hoá rồi hợp nhất

Pipeline có ba giai đoạn:

1. **SFT:** cold-start agent policy, trajectories từ domain-specialized teachers, verification và human annotation, serialize bằng XTML. QAT bắt đầu tại đây.
2. **RL:** ba domain (general, general agents, coding agents) × ba effort levels (low/high/max) tạo chín expert policies. Partial rollout dừng iteration khi tỷ lệ \(\lambda\) trajectories hoàn tất; rollout còn lại được lưu và resume, nên cần regularization để chịu stale/off-policy data.
3. **MOPD:** Multi-Teacher On-Policy Distillation dùng teacher tương ứng domain/effort để hợp nhất vào một student; report dùng clipped per-token log-ratio reward.

Reasoning-effort RL áp budget theo từng problem: trajectory vượt \(\tau b_0(x)\) nhận reward -1. Với task agentic, budget tính cả reasoning và tool-call arguments. Agentic generative reward model tạo rubric, chấm candidate, ghi scorepad và có verbosity control để giảm reward hacking.

**Ứng dụng đào tạo:** học viên không chạy RL quy mô lớn. Week 7 xây simulator budget/reward, phân tích khi nào partial rollout tạo staleness, và thiết kế teacher matrix 3×3 ở mức experiment plan.

## 4. Agent environment: verifier quan trọng hơn lời tự khai

K3 report mô tả unified white-box environment như tập module: tools, system prompts, context management, skills, memories và subagents. Việc randomize/combine harness nhằm giảm overfit vào một tool schema hoặc scaffold cụ thể.

Autonomous Execution Tasks định nghĩa initial state, goal, tool action space, budget và verifier độc lập. Reward dựa trên final environment state; public verifier cung cấp feedback, hidden verifier kiểm tra held-out cases. Personal-assistant tasks dùng mock apps và persistent world state; một rollout có thể dài hàng nghìn tool calls.

Đây là phần áp dụng trực tiếp nhất cho lớp học: capstone phải có executable verifier, hard budget, hidden test và log state transition. “Agent nói đã xong” không được tính là bằng chứng hoàn thành.

## 5. Infrastructure và deployment: algorithm–system co-design

Report mô tả KDA fused kernels/context parallelism, MoonEP để cân bằng expert execution, activation/gradient-buffer reuse, multimodal encoder scheduling, cache hợp nhất cho KDA state và MLA KV, cùng sandbox/KV persistence cho RL. Những nội dung này giải thích vì sao architecture paper không đủ để vận hành model 3T-class.

Post-training giữ MoE expert weights ở MXFP4, expert input activations MXFP8, còn attention/latent projections/shared experts/router ở precision cao hơn. Rollout và training dùng cùng quantization scheme nhằm giảm train–inference mismatch. MTP layer pre-trained được fine-tune thành EAGLE-3-style draft model; report tối ưu trực tiếp negative log acceptance-rate objective thay vì chỉ KL surrogate.

**Giới hạn phần cứng:** laptop làm được analytical labs. Tự host full model là bài toán cụm GPU, memory/storage/network và engine support; không thể suy ra cấu hình đủ chỉ từ “104B activated”. API là đường thực hành tùy chọn, phải có cost cap và không lưu reasoning/tool history nhạy cảm.

## 6. Evaluation: mạnh nhưng không phải mọi so sánh đều kiểm soát

Report đánh giá reasoning, coding, agents và multimodal. Cấu hình K3 chủ yếu dùng reasoning effort `max`, temperature 1.0; single-step/top-p và agentic/top-p khác nhau; một số benchmark báo cả không-tool/có-tool. Coding/agent scores còn phụ thuộc Kimi Code, Claude Code, Codex hoặc harness riêng.

Ba quy tắc audit:

- **Harness là một phần của treatment:** không gán toàn bộ chênh lệch score cho base model.
- **Tool augmentation đổi bài toán:** cặp điểm without/with tool không được trộn thành một metric.
- **In-house benchmark là bằng chứng sơ bộ:** cần task release, verifier và reproduction trước claim tổng quát.

Technical report tự kết luận K3 vẫn đứng sau hai proprietary systems mạnh nhất trong suite tổng thể, dù dẫn đầu nhiều benchmark cụ thể. Cách viết này nên được giữ trong bài giảng để tránh cherry-picking.

## 7. Những gì report chưa thiết lập

- Không công bố đầy đủ token count/data mixture weights, compute budget, hardware count hoặc mọi hyperparameter để tái tạo pre-training.
- Claim 2.5× không tách causal contribution của KDA, AttnRes, MoE, data và optimizer.
- Nhiều evaluation so khác harness, có fallback/cyberguard, hoặc dùng benchmark nội bộ.
- Model card ghi modality text/image trong summary trong khi narrative nói hiểu video qua shared vision pathway; cần diễn đạt video là input được encoder xử lý theo report, không suy rộng sang mọi capability video.
- Open weights không tự động đồng nghĩa OSI open source; mọi deployment phải đọc license cụ thể.

## 8. Chuyển thành khoá học 10 tuần

| Trụ cột report | Tuần | Sản phẩm học viên | Mức tái tạo |
|---|---:|---|---|
| Claim/evidence + scale | 1 | claim ledger, memory lower bound | audit |
| KDA–MLA | 2 | recurrence + numerical tests | toy implementation |
| AttnRes | 3 | depth mixer + ablation | toy implementation |
| Stable LatentMoE/QB | 4 | router balance experiment | toy implementation |
| Multimodal/data/scaling | 5 | dataset card + ablation plan | design |
| 1M context/infra | 6 | context curriculum + cache memo | systems design |
| SFT/RL/MOPD/QAT | 7 | effort-budget simulator + plan | simulation |
| Agent environments | 8 | sandbox task + verifier | executable mini-system |
| Serving/evaluation | 9 | benchmark audit + deployment decision | analysis |
| Integration | 10 | capstone + defense | reproduction-style |

## Khuyến nghị tiếp theo

1. Chạy toàn bộ toy labs trên CPU và ghi invariant, không chỉ screenshot output.
2. Với cohort có GPU, thêm optional benchmark trên model nhỏ dùng cùng experimental protocol; không gọi đó là K3 reproduction.
3. Với cohort có API, đánh giá preserved-history/tool calling trên dữ liệu không nhạy cảm, có token/cost budget.
4. Cập nhật claim ledger khi report/model card/license đổi; giữ ngày truy cập.

Chi tiết vận hành, license, config và preserved-thinking history được tách thành [hướng dẫn repository chính thức](REPOSITORY_GUIDE.md) để học viên không nhầm report repository với model/code repository trên Hugging Face.

## Câu hỏi nghiên cứu tiếp theo

- Bao nhiêu lợi ích đến từ hybrid attention so với long-context data curriculum?
- Block size của AttnRes thay đổi accuracy/memory/latency ra sao ở model nhỏ?
- QB ảnh hưởng specialization khi batch/domain mixture đổi như thế nào?
- Effort conditioning có tổng quát sang domain chưa thấy không?
- Hidden verifier nào đủ mạnh để phát hiện reward hacking mà không tạo false negatives quá cao?
