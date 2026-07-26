# Cáp truyền tin đường tắt và Bộ ổn định âm lượng

Bạn đã bao giờ chơi trò truyền tin trong một vòng tròn lớn chưa? Người thứ nhất thì thầm vào tai người thứ hai, người thứ hai truyền cho người thứ ba... Khi đến người thứ 50, thông điệp ban đầu thường bị méo mó hoặc mất sạch thông tin. 

Trong các mạng nơ-ron học sâu (Deep Neural Networks), khi chúng ta xếp chồng 12 hay 96 lớp xử lý lên nhau, thông tin và tín hiệu đạo hàm (gradient) truyền ngược về cũng sẽ bị suy hao và biến mất y hệt như vậy. Hiện tượng này gọi là **Biến mất gradient** (Vanishing Gradient).

Để giải quyết, các nhà khoa học đã đưa ra giải pháp cực kỳ thông minh: **Residual Connection** (Kết nối dòng dư). Thay vì bắt tín hiệu đi tuần tự qua từng lớp, ta thiết kế một đường cáp truyền tin chạy song song đi tắt qua lớp đó. Công thức rất đơn giản:
$$	ext{Đầu ra} = x + f(x)$$
Trong đó $x$ là tín hiệu đầu vào ban đầu, còn $f(x)$ là kết quả sau khi đi qua lớp Attention hoặc MLP. Nếu lớp $f(x)$ hoạt động kém hoặc bị nhiễu, tín hiệu gốc $x$ vẫn đi qua đường tắt an toàn. Điều này cho phép xây dựng các mạng nơ-ron sâu hàng trăm tầng mà không sợ mất tín hiệu.

Bên cạnh đó, để tránh việc các con số cộng dồn qua nhiều lớp bị phình to quá mức (gây lỗi tràn số), ta sử dụng **Layer Normalization** (LayerNorm). LayerNorm hoạt động giống như một bộ điều chỉnh âm lượng tự động: nếu âm lượng quá to, nó sẽ vặn nhỏ lại; nếu quá nhỏ, nó sẽ khuếch đại lên, giữ cho tín hiệu luôn ở trong dải âm thanh ổn định và dễ nghe.

Ghép nối LayerNorm, Multi-Head Attention, và MLP lại với nhau theo cấu trúc đường tắt, ta thu được một **Transformer Block** hoàn chỉnh — viên gạch xây dựng nên các siêu AI.
