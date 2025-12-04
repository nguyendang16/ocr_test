# 🚀 Hướng dẫn Deploy lên Hugging Face Spaces (FREE UNLIMITED)

## ✨ Ưu điểm Hugging Face Spaces
- ✅ **Hoàn toàn miễn phí**, không giới hạn
- ✅ RAM cao hơn (16GB free tier)
- ✅ Tối ưu cho ML/AI apps
- ✅ Không sleep
- ✅ Community lớn

---

## 📋 Bước 1: Tạo Space

### 1.1. Đăng ký Hugging Face
1. Truy cập: **https://huggingface.co/join**
2. Đăng ký tài khoản miễn phí

### 1.2. Tạo Space mới
1. Click **profile** → **"New Space"**
2. Điền thông tin:
   ```
   Space name: vietnamese-ocr
   License: MIT
   Space SDK: Gradio (hoặc Streamlit)
   ```
3. Click **"Create Space"**

---

## 📝 Bước 2: Tạo Gradio Interface

Hugging Face Spaces dùng Gradio để tạo UI. Tôi sẽ tạo file mới:

### 2.1. Cấu trúc files

```
vietnamese-ocr/
├── app.py              # Main Gradio app
├── requirements.txt    # Dependencies
├── .gitignore
└── README.md
```

### 2.2. Upload lên Space

**Cách 1: Qua Web UI**
1. Trong Space dashboard, click **"Files"**
2. Upload từng file

**Cách 2: Qua Git**
```bash
cd /Users/nguyendang/demo_stuffs/auto_ocr

# Clone space repo
git clone https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-ocr
cd vietnamese-ocr

# Copy files (sẽ tạo app.py ở bước sau)
# Push
git add .
git commit -m "Initial commit"
git push
```

---

## 🔑 Bước 3: Thêm API Key

1. Trong Space dashboard → **Settings** → **Variables and secrets**
2. Add secret:
   ```
   Name: GEMINI_API_KEY
   Value: your-gemini-api-key-here
   ```

---

## 🌐 Bước 4: Access App

URL: `https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-ocr`

---

## ⚡ So sánh Render vs Hugging Face

| Feature | Render.com | Hugging Face |
|---------|-----------|--------------|
| RAM | 512 MB | 16 GB |
| Sleep | Có (15 phút) | Không |
| Price | Free 750h/month | Unlimited free |
| Setup | Dễ hơn | Cần viết Gradio UI |
| Custom domain | Có | Không |
| Best for | Production apps | ML demos/experiments |

---

## 💡 Recommendation

- **Dùng Render** nếu: Muốn giữ nguyên Flask UI, cần custom domain
- **Dùng Hugging Face** nếu: Cần nhiều RAM hơn, không lo sleep, muốn share với ML community

---

**File app.py cho Gradio sẽ được tạo ở bước tiếp theo!**

