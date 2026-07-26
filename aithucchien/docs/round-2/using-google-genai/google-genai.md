# Sử dụng với Gemini/Vertex AI

 

- Vertex AI
- Gemini

## Xác thực (Authentication)​

Để xác thực với Vertex AI, bạn cần sử dụng service account key đã được ban tổ chức cung cấp và đặt đường dẫn của nó vào biến môi trường `GOOGLE_APPLICATION_CREDENTIALS`.

**Đặt Biến Môi trường**:
Thêm biến môi trường sau vào môi trường local của bạn, trỏ đến file JSON đã được cung cấp.

`export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/keyfile.json"`

Chi tiết hơn có thể xem tại Google Cloud Documentation.

## Hướng dẫn sử dụng cơ bản​

### Tạo văn bản (Text Generation)​

Cài đặt thư viện cần thiết:

`pip install --upgrade google-genai`

Sử dụng trong code:

`from google import genaifrom dotenv import load_dotenvload_dotenv()   client = genai.Client(vertexai=True, location="us-central1")response = client.models.generate_content(  model="gemini-2.5-flash",  contents="Explain how AI works in a few words")print(response.text)`

### Tạo hình ảnh (Image Generation)​

Với Vertex AI, bạn có thể sử dụng các mô hình tạo ảnh như Imagen.

`from google import genaifrom google.genai.types import GenerateImagesConfig# Cần xác thực với GOOGLE_APPLICATION_CREDENTIALSclient = genai.Client()output_file = "output-image.png"image = client.models.generate_images(  model="imagen-4.0-generate-001",  prompt="A dog reading a newspaper",  config=GenerateImagesConfig(      image_size="2K",  ),)image.generated_images[0].image.save(output_file)print(f"Created output image using {len(image.generated_images[0].image.image_bytes)} bytes")`

## Xác thực với Gemini API​

Để sử dụng API của Gemini, bạn cần sử dụng API key đã được ban tổ chức cung cấp.

**Đặt Biến Môi trường**:
Thêm API key đã được cung cấp vào biến môi trường `GEMINI_API_KEY`.

`export GEMINI_API_KEY="YOUR_API_KEY"`

## Hướng dẫn cơ bản cho Gemini​

### Tạo văn bản với Gemini API​

Cài đặt thư viện cần thiết:

`pip install -q -U google-genai`

Sử dụng trong code:

`from google import genaifrom google.genai.types import HttpOptions# Cần đặt GEMINI_API_KEY trong môi trường của bạnclient = genai.Client(http_options=HttpOptions(api_version="v1"))response = client.models.generate_content(  model="gemini-2.5-flash",  contents="How does AI work?",)print(response.text)`

Để biết thêm chi tiết về các tính năng nâng cao như tạo video và nhiều hơn nữa, vui lòng tham khảo tài liệu chính thức của Google Generative AI.
