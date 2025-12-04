# 📦 Hướng dẫn cài đặt chi tiết

## Cài đặt PaddleOCR và dependencies

### 🍎 macOS (Apple Silicon M1/M2/M3)

```bash
# Cài Python 3.8+ nếu chưa có
brew install python@3.10

# Cài đặt dependencies
pip3 install flask==3.0.0
pip3 install google-generativeai==0.3.2
pip3 install Pillow==10.1.0
pip3 install python-dotenv==1.0.0

# Cài PaddlePaddle CPU version (cho Apple Silicon)
pip3 install paddlepaddle

# Cài PaddleOCR
pip3 install paddleocr==2.7.0.3
```

### 🐧 Linux (Ubuntu/Debian)

**CPU version:**
```bash
pip3 install -r requirements.txt
```

**GPU version (nếu có NVIDIA GPU):**
```bash
# Cài CUDA và cuDNN trước
# Sau đó cài PaddlePaddle GPU version
pip3 install paddlepaddle-gpu

# Cài các dependencies còn lại
pip3 install flask==3.0.0
pip3 install google-generativeai==0.3.2
pip3 install Pillow==10.1.0
pip3 install python-dotenv==1.0.0
pip3 install paddleocr==2.7.0.3
```

### 🪟 Windows

**CPU version:**
```bash
pip install -r requirements.txt
```

**GPU version (nếu có NVIDIA GPU):**
```powershell
# Cài PaddlePaddle GPU
pip install paddlepaddle-gpu

# Cài các dependencies còn lại
pip install flask==3.0.0
pip install google-generativeai==0.3.2
pip install Pillow==10.1.0
pip install python-dotenv==1.0.0
pip install paddleocr==2.7.0.3
```

## ⚠️ Troubleshooting

### Lỗi khi cài PaddlePaddle

**Lỗi: "No matching distribution found"**

Thử cài phiên bản cụ thể:
```bash
pip3 install paddlepaddle==2.6.0
```

Hoặc cài từ wheel file cho platform cụ thể:
```bash
# Xem platform của bạn
python -c "import platform; print(platform.machine())"

# Tải wheel phù hợp từ:
# https://www.paddlepaddle.org.cn/install/quick
```

### Lỗi: "ImportError: libgomp.so.1"

Trên Linux, cài OpenMP:
```bash
sudo apt-get install libgomp1
```

### Lỗi: Memory/RAM không đủ

PaddleOCR cần ít nhất 2GB RAM. Nếu máy yếu, giảm batch size hoặc dùng model nhẹ hơn.

### Lỗi khi tải models lần đầu

PaddleOCR sẽ tự động tải models (~10-50MB) lần đầu chạy. Đảm bảo:
- Có kết nối internet
- Có quyền ghi vào thư mục `~/.paddleocr/`

Nếu timeout, thử tải thủ công:
```bash
python -c "from paddleocr import PaddleOCR; ocr = PaddleOCR(lang='vi')"
```

## ✅ Kiểm tra cài đặt

Chạy script test:

```python
# test_paddle.py
from paddleocr import PaddleOCR
import numpy as np
from PIL import Image, ImageDraw, ImageFont

print("🔍 Testing PaddleOCR...")

# Create test image with Vietnamese text
img = Image.new('RGB', (400, 100), color='white')
d = ImageDraw.Draw(img)
d.text((10, 30), "Chuyen tien mua sam", fill='black')
img.save('test.png')

# Initialize OCR
ocr = PaddleOCR(use_angle_cls=True, lang='vi', show_log=False)

# Test OCR
result = ocr.ocr('test.png', cls=True)
print(f"Result: {result}")

if result and result[0]:
    print("✅ PaddleOCR hoạt động tốt!")
else:
    print("❌ PaddleOCR có vấn đề")
```

Chạy:
```bash
python test_paddle.py
```

## 🚀 Tối ưu hiệu năng

### Dùng GPU (nếu có)

```python
# Trong main.py, thay đổi:
ocr = PaddleOCR(
    use_angle_cls=True, 
    lang='vi', 
    show_log=False,
    use_gpu=True,  # Bật GPU
    gpu_mem=500    # Giới hạn VRAM (MB)
)
```

### Giảm thời gian khởi động

```python
# Cache OCR instance để không phải load lại model
# OCR đã được khởi tạo 1 lần ở đầu file main.py
```

### Xử lý ảnh lớn

```python
# Resize ảnh lớn trước khi OCR để tăng tốc
if image.width > 2000 or image.height > 2000:
    image.thumbnail((2000, 2000), Image.Resampling.LANCZOS)
```

---

**Cần trợ giúp thêm?** Xem log trong terminal khi chạy app để debug.

