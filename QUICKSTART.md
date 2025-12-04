# 🚀 Quick Start Guide - Vietnamese OCR

## Bắt đầu nhanh trong 3 bước

### Bước 1: Lấy Gemini API Key (FREE)

1. Truy cập: **https://makersuite.google.com/app/apikey**
2. Đăng nhập bằng Google
3. Click "Create API Key"
4. Copy API key

### Bước 2: Setup

**Cách 1: Tự động (khuyên dùng)**
```bash
bash setup_env.sh
```

**Cách 2: Thủ công**
```bash
# Cài đặt dependencies (có thể mất vài phút)
pip3 install -r requirements.txt

# Tạo file .env
echo "GEMINI_API_KEY=your-api-key-here" > .env
```

⚠️ **Lưu ý**: Lần đầu cài PaddleOCR có thể mất 5-10 phút vì cần tải các dependencies lớn (PaddlePaddle ~200MB)

### Bước 3: Chạy ứng dụng

```bash
# Cách 1: Dùng script
bash run.sh

# Cách 2: Chạy trực tiếp
python3 main.py
```

Mở trình duyệt: **http://localhost:5000**

---

## 📖 Sử dụng

### Upload ảnh
1. Click tab "📷 Upload Ảnh"
2. Kéo thả hoặc chọn ảnh chứa text không dấu
3. Click "🚀 Xử lý ảnh"
4. Xem kết quả và copy

### Nhập text
1. Click tab "✏️ Nhập Text"
2. Nhập text không dấu (VD: "Tung ck du lich")
3. Click "🚀 Phục hồi dấu"
4. Xem kết quả và copy

---

## ✅ Test API

Chạy server trước, sau đó:
```bash
python3 test_api.py
```

---

## 💡 Ví dụ

| Input (không dấu) | Output (có dấu) |
|-------------------|-----------------|
| `Tung ck du lich` | `Tùng chuyển khoản du lịch` |
| `Chuyen tien mua sam` | `Chuyển tiền mua sắm` |
| `Thanh toan hoa don` | `Thanh toán hóa đơn` |

---

## ⚠️ Troubleshooting

**Server không chạy?**
- Kiểm tra Python 3.8+ đã cài: `python3 --version`
- Kiểm tra dependencies: `pip3 install -r requirements.txt`

**Lỗi API key?**
- Kiểm tra file `.env` có tồn tại không
- Đảm bảo API key hợp lệ
- Export trực tiếp: `export GEMINI_API_KEY='your-key'`

**Kết quả không chính xác?**
- Gemini API đôi khi có thể sai, thử lại
- Ảnh cần rõ ràng, text dễ đọc
- Văn bản càng có ngữ cảnh càng chính xác

---

## 📚 Tài liệu đầy đủ

Xem file **README.md** để biết thêm chi tiết về:
- API endpoints
- Cấu hình nâng cao
- Xử lý lỗi
- Use cases

---

**Chúc bạn sử dụng vui vẻ! 🎉**

