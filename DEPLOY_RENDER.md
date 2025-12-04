# 🚀 Hướng dẫn Deploy lên Render.com (FREE)

## ✨ Ưu điểm Render.com
- ✅ **Free tier** tốt (750 giờ/tháng)
- ✅ Deploy đơn giản từ GitHub
- ✅ Hỗ trợ Python/Flask tốt
- ✅ SSL certificate tự động (HTTPS)
- ⚠️ Free tier sẽ sleep sau 15 phút không dùng (khởi động lại ~30s)

---

## 📋 Bước 1: Chuẩn bị code

### 1.1. Tạo Git repository (nếu chưa có)

```bash
cd /Users/nguyendang/demo_stuffs/auto_ocr

# Initialize git
git init

# Add files
git add .
git commit -m "Initial commit - Vietnamese OCR"
```

### 1.2. Push lên GitHub

```bash
# Tạo repo mới trên GitHub: https://github.com/new
# Sau đó:
git remote add origin https://github.com/YOUR_USERNAME/vietnamese-ocr.git
git branch -M main
git push -u origin main
```

---

## 🌐 Bước 2: Deploy trên Render

### 2.1. Đăng ký Render

1. Truy cập: **https://render.com/**
2. Sign up với GitHub account
3. Authorize Render truy cập GitHub repos

### 2.2. Tạo Web Service mới

1. Click **"New +"** → **"Web Service"**
2. Chọn repository: `vietnamese-ocr`
3. Cấu hình:

```
Name: vietnamese-ocr
Region: Singapore (gần VN nhất)
Branch: main
Runtime: Python 3

Build Command: pip install -r requirements.txt
Start Command: gunicorn main:app

Instance Type: Free
```

### 2.3. Thêm Environment Variables

Click **"Environment"** tab, thêm:

```
GEMINI_API_KEY=your-gemini-api-key-here
PYTHON_VERSION=3.11.0
```

### 2.4. Deploy

- Click **"Create Web Service"**
- Đợi ~3-5 phút để build
- URL sẽ có dạng: `https://vietnamese-ocr-xxxx.onrender.com`

---

## ⚙️ Bước 3: Cấu hình nâng cao (Optional)

### Tăng timeout (nếu OCR chậm)

Trong Render dashboard → Settings:

```
Health Check Path: /
```

### Auto-deploy khi push code mới

Render tự động deploy khi bạn push lên GitHub main branch.

---

## 🧪 Bước 4: Test

```bash
# Test API
curl -X POST https://vietnamese-ocr-xxxx.onrender.com/api/restore-text \
  -H "Content-Type: application/json" \
  -d '{"text": "Tung ck du lich"}'
```

Hoặc mở browser: `https://vietnamese-ocr-xxxx.onrender.com`

---

## 📝 Lưu ý với Free Tier

### 1. Sleep sau 15 phút
- Free service sẽ sleep nếu không có request
- Lần đầu access sau khi sleep mất ~30-60s để wake up

### 2. Giới hạn
- 750 giờ/tháng (đủ dùng)
- 512 MB RAM (có thể hơi ít với PaddleOCR)

### 3. Nếu vượt RAM:
- Xem logs để check memory usage
- Có thể cần optimize hoặc upgrade plan ($7/month)

---

## 🐛 Troubleshooting

### Lỗi: "Build failed"
```bash
# Check logs trong Render dashboard
# Thường do thiếu dependencies
```

### Lỗi: "Out of memory"
```bash
# PaddleOCR cần nhiều RAM
# Solutions:
# 1. Optimize code để load model khi cần
# 2. Giảm model size
# 3. Upgrade to paid plan
```

### App chậm/timeout
```bash
# Do free tier có giới hạn CPU
# PaddleOCR lần đầu chạy sẽ chậm do tải models
```

---

## 💡 Tips

### 1. Keep app awake
Dùng free service như **UptimeRobot** để ping app mỗi 5 phút:
- https://uptimerobot.com/
- Add monitor với URL của bạn

### 2. Custom domain (Optional)
Render free tier hỗ trợ custom domain miễn phí!

### 3. View logs
```bash
# Trong Render dashboard → Logs tab
# Xem real-time logs của app
```

---

## 🎯 Alternative: Nếu Render free tier không đủ RAM

Xem file **DEPLOY_HUGGINGFACE.md** để deploy lên Hugging Face Spaces (unlimited free cho ML apps).

---

**🎉 Done! App của bạn đã online!**

