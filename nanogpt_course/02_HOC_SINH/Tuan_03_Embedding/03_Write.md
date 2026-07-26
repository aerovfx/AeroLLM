# Bản đồ ý nghĩa và Tọa độ của từ vựng

Con người hiểu nghĩa của từ `"mèo"` vì chúng ta đã nhìn thấy con mèo ngoài đời thực. Nhưng máy tính chỉ thấy con mèo là mã số `12` (Token ID). Làm thế nào máy tính hiểu được `"mèo"` và `"chó"` là các loài động vật bốn chân có lông, còn `"máy tính"` là đồ điện tử?

Để làm được điều này, các kỹ sư AI đã phát minh ra **Embedding** (Nhúng từ) — phương pháp biến mỗi từ thành một **tọa độ vector** nằm trên một **Bản đồ ý nghĩa nhiều chiều**.

Hãy tưởng tượng một bản đồ lớp học 3D. 
*   Trục X biểu thị mức độ *"thích thể thao"*.
*   Trục Y biểu thị mức độ *"thích nghệ thuật"*.
*   Trục Z biểu thị mức độ *"thích chơi game"*.

Mỗi học sinh trong lớp sẽ có một tọa độ (X, Y, Z) đại diện cho sở thích của mình. Những bạn thích đá bóng và chơi game sẽ ngồi rất gần nhau trên bản đồ này, còn những bạn thích vẽ tranh sẽ ngồi ở một góc khác. 

Lớp `nn.Embedding` trong PyTorch cũng hoạt động y hệt như vậy. Nó gán cho mỗi Token ID một danh sách các số thực (ví dụ 96 số đối với mô hình nhỏ, hoặc 768 số đối với GPT-2). Ban đầu các số này là ngẫu nhiên, nhưng qua quá trình học, các từ có nghĩa gần nhau (ví dụ `"vua"` và `"hoàng đế"`) sẽ tự động di chuyển lại gần nhau trên bản đồ, tạo ra một không gian biểu diễn ngữ nghĩa cực kỳ kỳ diệu.

Tuy nhiên, nếu chỉ nhúng nghĩa của từ, mô hình sẽ không phân biệt được `"tôi yêu em"` và `"em yêu tôi"`, vì cả hai câu đều chứa cùng các từ vựng. Do đó, ta cần **Position Embedding** (Nhúng vị trí). Đây là một bản đồ tọa độ phụ cho biết *"từ này đứng ở vị trí số 1, từ kia đứng ở vị trí số 2"*. Chúng ta cộng hai tọa độ này lại với nhau trước khi gửi vào bộ não AI.
