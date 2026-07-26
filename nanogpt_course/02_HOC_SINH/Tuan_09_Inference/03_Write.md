# Thanh gạt sáng tạo của Trí Tuệ Nhân Tạo

Sau khi AI học xong, làm thế nào để nó viết chữ? Quy trình này gọi là **Inference** (Suy luận). AI viết chữ từng từ một: nó đọc câu gợi ý của bạn, đoán từ tiếp theo, nối từ đó vào câu, rồi lại đọc toàn bộ câu mới để đoán tiếp từ tiếp sau nữa.

Tuy nhiên, nếu ở mỗi bước đoán, AI luôn luôn chọn từ có xác suất cao nhất (phương pháp **Greedy Sampling** — Chọn từ tham lam), kết quả sinh ra sẽ cực kỳ nhàm chán, lặp đi lặp lại và thiếu tính tự nhiên của con người. Con người khi nói chuyện đôi khi chọn những từ độc lạ, bất ngờ. 

Để điều khiển tính cách của AI, các nhà khoa học đưa vào một tham số cực kỳ thú vị: **Temperature** (Nhiệt độ sáng tạo).
*   **Nhiệt độ thấp (Temperature < 0.5):** AI trở nên rất nhút nhát và an toàn. Nó chia nhỏ điểm số của từ cao nhất so với các từ khác, khiến từ có xác suất cao nhất trở nên vượt trội hoàn toàn. Kết quả sinh ra rất logic, lặp từ, phù hợp để giải toán hoặc viết code.
*   **Nhiệt độ trung bình (Temperature = 0.7 - 1.0):** AI có sự cân bằng lý tưởng giữa tính logic và tính sáng tạo. Nó viết câu tự nhiên, trôi chảy.
*   **Nhiệt độ cao (Temperature > 1.2):** AI trở nên cực kỳ bay bổng, "nhiệt huyết" và liều lĩnh. Sự chênh lệch xác suất giữa các từ bị san phẳng, khiến AI có thể bốc thăm trúng các từ cực kỳ hiếm gặp. Kết quả sinh ra rất bất ngờ, đôi khi sáng tạo ra những câu thơ độc lạ, nhưng nếu quá cao (ví dụ `2.0`), nó sẽ nói sảng và gõ chữ vô nghĩa.

Để tránh việc AI bốc thăm trúng các từ hoàn toàn vô lý (ví dụ đang viết về món ăn tự nhiên bốc trúng từ `"vũ trụ"`), ta áp dụng **Top-K Sampling**. Chúng ta chỉ cho phép AI bốc thăm trong top $K$ (ví dụ 50) từ có điểm số cao nhất, loại bỏ hoàn toàn các từ vô nghĩa còn lại.
