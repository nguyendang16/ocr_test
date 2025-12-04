# Vietnamese OCR - Phục hồi dấu tiếng Việt 🇻🇳

Ứng dụng nhận diện và phục hồi dấu tiếng Việt từ văn bản không dấu sử dụng Google Gemini API.

## ✨ Tính năng

- 📷 **OCR từ ảnh**: Upload ảnh chứa văn bản không dấu, tự động nhận diện và phục hồi dấu (dùng PaddleOCR)
- ✏️ **Nhập text trực tiếp**: Nhập văn bản không dấu để phục hồi dấu
- 🎯 **Hiểu ngữ cảnh**: Nhận diện ngữ cảnh chuyển tiền, chuyển khoản
- 🔤 **Xử lý từ viết tắt**: Hiểu các từ viết tắt phổ biến như "ck" → "chuyển khoản"
- 🇻🇳 **Hỗ trợ tiếng Việt tốt**: PaddleOCR được train cho tiếng Việt
- 🚀 **Giao diện thân thiện**: Web UI đẹp mắt, dễ sử dụng

## 📋 Yêu cầu

- Python 3.8+
- Google Gemini API Key

## 🚀 Cài đặt

### 1. Clone repository hoặc tải về

```bash
cd auto_ocr
```

### 2. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 3. Lấy Gemini API Key

1. Truy cập: https://makersuite.google.com/app/apikey
2. Đăng nhập với tài khoản Google
3. Tạo API key mới
4. Copy API key

### 4. Cấu hình API Key

**Cách 1: Sử dụng biến môi trường (Khuyến nghị)**

```bash
export GEMINI_API_KEY='your-gemini-api-key-here'
```

Hoặc trên Windows:
```cmd
set GEMINI_API_KEY=your-gemini-api-key-here
```

**Cách 2: Tạo file .env**

Tạo file `.env` trong thư mục `auto_ocr`:
```
GEMINI_API_KEY=your-gemini-api-key-here
```

Sau đó cập nhật `main.py` để load từ file .env:
```python
from dotenv import load_dotenv
load_dotenv()
```

## 🎮 Sử dụng

### Chạy ứng dụng

```bash
python main.py
```

Server sẽ chạy tại: http://localhost:5000

### Sử dụng qua Web UI

1. Mở trình duyệt và truy cập: http://localhost:5000
2. Chọn một trong hai tab:
   - **📷 Upload Ảnh**: Upload ảnh chứa văn bản không dấu
   - **✏️ Nhập Text**: Nhập trực tiếp văn bản không dấu
3. Nhấn nút "Xử lý" hoặc "Phục hồi dấu"
4. Xem kết quả và copy nếu cần

### Ví dụ

**Input (không dấu):**
```
Tung ck du lich
```

**Output (có dấu):**
```
Tùng chuyển khoản du lịch
```

**Input (không dấu):**
```
Chuyen tien mua sam cho Nguyen Van A
```

**Output (có dấu):**
```
Chuyển tiền mua sắm cho Nguyễn Văn A
```

## 📡 API Endpoints

### 1. Process Image (OCR + Restore Diacritics)

**Endpoint:** `POST /api/process`

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: 
  - `image`: Image file (JPG, PNG, JPEG)

**Response:**
```json
{
  "success": true,
  "original_text": "Tung ck du lich",
  "restored_text": "Tùng chuyển khoản du lịch"
}
```

**Example (curl):**
```bash
curl -X POST http://localhost:5000/api/process \
  -F "image=@image.jpg"
```

### 2. Restore Text Only

**Endpoint:** `POST /api/restore-text`

**Request:**
- Method: POST
- Content-Type: application/json
- Body:
```json
{
  "text": "Tung ck du lich"
}
```

**Response:**
```json
{
  "success": true,
  "original_text": "Tung ck du lich",
  "restored_text": "Tùng chuyển khoản du lịch"
}
```

**Example (curl):**
```bash
curl -X POST http://localhost:5000/api/restore-text \
  -H "Content-Type: application/json" \
  -d '{"text": "Tung ck du lich"}'
```

## 🏗️ Cấu trúc thư mục

```
auto_ocr/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Documentation
├── .gitignore          # Git ignore rules
├── templates/
│   └── index.html      # Web UI
```

## 🛠️ Công nghệ sử dụng

- **Flask**: Web framework
- **PaddleOCR**: OCR engine hỗ trợ tiếng Việt
- **Google Gemini API**: AI model để phục hồi dấu tiếng Việt
- **Pillow**: Xử lý ảnh
- **HTML/CSS/JavaScript**: Frontend

## ⚙️ Cấu hình nâng cao

### Thay đổi model Gemini

Trong `main.py`, bạn có thể thay đổi model cho việc phục hồi dấu:

```python
text_model = genai.GenerativeModel('gemini-1.5-flash')  # Nhanh, rẻ
# hoặc
text_model = genai.GenerativeModel('gemini-1.5-pro')    # Chính xác hơn
```

### Tùy chỉnh PaddleOCR

Trong `main.py`, bạn có thể cấu hình PaddleOCR:

```python
ocr = PaddleOCR(
    use_angle_cls=True,  # Detect góc xoay của text
    lang='vi',           # Ngôn ngữ tiếng Việt
    show_log=False,      # Ẩn log
    use_gpu=True         # Dùng GPU nếu có (nhanh hơn)
)
```

### Tùy chỉnh prompt

Bạn có thể tùy chỉnh prompt trong hàm `restore_vietnamese_diacritics()` để phù hợp với use case cụ thể.

## 🐛 Xử lý lỗi thường gặp

### Lỗi: "GEMINI_API_KEY not set"

**Nguyên nhân:** Chưa cấu hình API key

**Giải pháp:** 
```bash
export GEMINI_API_KEY='your-api-key'
python main.py
```

### Lỗi: "Could not extract text from image"

**Nguyên nhân:** Ảnh không rõ, không có text, hoặc PaddleOCR chưa cài đúng

**Giải pháp:** 
- Sử dụng ảnh có độ phân giải cao hơn
- Đảm bảo text trong ảnh rõ ràng, dễ đọc
- Kiểm tra PaddleOCR đã cài đúng: `pip install paddleocr paddlepaddle`
- Xem log trong terminal để debug

### Lỗi khi cài PaddleOCR

**Trên macOS với Apple Silicon (M1/M2/M3):**
```bash
# Dùng phiên bản CPU
pip install paddlepaddle
pip install paddleocr
```

**Trên Windows/Linux với GPU:**
```bash
# Dùng phiên bản GPU để nhanh hơn
pip install paddlepaddle-gpu
pip install paddleocr
```

### Lỗi: 429 (Too Many Requests)

**Nguyên nhân:** Vượt quá giới hạn API requests

**Giải pháp:**
- Đợi vài phút trước khi thử lại
- Kiểm tra quota tại Google Cloud Console

## 📝 Giới hạn

- Gemini API có giới hạn requests/phút (free tier)
- Độ chính xác OCR phụ thuộc vào chất lượng ảnh
- Hỗ trợ tốt nhất cho văn bản đánh máy (printed text)
- PaddleOCR lần đầu chạy sẽ tải model (~10-50MB), có thể mất vài phút

## 🎯 Use Cases

- Xử lý tin nhắn chuyển khoản không dấu
- OCR tài liệu văn bản không dấu
- Chuẩn hóa dữ liệu text không dấu
- Hỗ trợ nhập liệu tiếng Việt

## 📄 License

MIT License - Free to use

## 👨‍💻 Support

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra lại API key
2. Đảm bảo đã cài đặt đầy đủ dependencies
3. Kiểm tra logs trong terminal

---

**Made with ❤️ using Google Gemini AI**

