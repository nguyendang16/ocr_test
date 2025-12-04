# 🚀 Tóm tắt các options Deploy (FREE)

## 📊 So sánh nhanh

| Platform | RAM | Sleep? | Setup | Best for |
|----------|-----|--------|-------|----------|
| **Render.com** | 512MB | Có (15 phút) | ⭐⭐⭐ Dễ | Production simple |
| **Hugging Face** | 16GB | Không | ⭐⭐ Trung bình | ML/AI demos |
| **Railway** | 512MB | Có | ⭐⭐⭐ Dễ | Giống Render |
| **Fly.io** | 256MB | Không | ⭐ Khó | Advanced users |

---

## 🏆 RECOMMEND: Render.com (Dễ nhất)

### ⚡ Quick Start (5 phút)

```bash
cd /Users/nguyendang/demo_stuffs/auto_ocr

# 1. Init git (nếu chưa có)
git init
git add .
git commit -m "Initial commit"

# 2. Push lên GitHub
# Tạo repo tại: https://github.com/new
git remote add origin https://github.com/YOUR_USERNAME/vietnamese-ocr.git
git branch -M main
git push -u origin main

# 3. Deploy trên Render
# - Go to: https://render.com
# - Sign in with GitHub
# - New Web Service → Select repo
# - Build: pip install -r requirements.txt
# - Start: gunicorn main:app
# - Add env var: GEMINI_API_KEY
# - Deploy!
```

**URL:** `https://vietnamese-ocr-xxxx.onrender.com`

### ⚠️ Lưu ý
- Free tier sleep sau 15 phút không dùng
- Wake up mất ~30s
- Đủ cho demo/testing

---

## 🤗 ALTERNATIVE: Hugging Face Spaces (Nhiều RAM hơn)

### ⚡ Quick Start

```bash
# 1. Đăng ký: https://huggingface.co/join

# 2. Tạo Space mới
# - New Space → Gradio SDK
# - Name: vietnamese-ocr

# 3. Clone và upload
git clone https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-ocr
cd vietnamese-ocr

# Copy file app.py (đã tạo sẵn)
cp /Users/nguyendang/demo_stuffs/auto_ocr/app.py .
cp /Users/nguyendang/demo_stuffs/auto_ocr/requirements.txt .
cp /Users/nguyendang/demo_stuffs/auto_ocr/README_HF.md README.md

git add .
git commit -m "Add app"
git push
```

**URL:** `https://huggingface.co/spaces/YOUR_USERNAME/vietnamese-ocr`

### ✅ Ưu điểm
- 16GB RAM (đủ cho PaddleOCR)
- Không sleep
- Free unlimited
- Tối ưu cho ML apps

---

## 📦 Files đã chuẩn bị

```
auto_ocr/
├── main.py              # Flask app (cho Render)
├── app.py               # Gradio app (cho Hugging Face)
├── requirements.txt     # Dependencies
├── Procfile            # Render config
├── runtime.txt         # Python version
├── DEPLOY_RENDER.md    # Hướng dẫn chi tiết Render
├── DEPLOY_HUGGINGFACE.md  # Hướng dẫn chi tiết HF
└── deploy.sh           # Script hỗ trợ
```

---

## 🎯 Recommendation của tôi

### Chọn Render.com nếu:
- ✅ Muốn giữ nguyên Flask UI
- ✅ Setup nhanh, đơn giản
- ✅ Không cần nhiều RAM
- ⚠️ OK với app sleep khi không dùng

### Chọn Hugging Face nếu:
- ✅ Cần nhiều RAM (PaddleOCR ngốn RAM)
- ✅ Không muốn app sleep
- ✅ Share với ML community
- ⚠️ OK với Gradio UI (khác với Flask UI hiện tại)

---

## 💡 Tips

### 1. Keep Render app awake
Dùng **UptimeRobot** (free) để ping app mỗi 5 phút:
- https://uptimerobot.com/
- Add HTTP monitor với URL app của bạn

### 2. Test local trước khi deploy
```bash
# Test Flask app
python main.py

# Test Gradio app
python app.py
```

### 3. Check logs khi deploy
- Render: Dashboard → Logs tab
- Hugging Face: Space → App → Logs

---

## 🐛 Common Issues

### Out of Memory
```
→ Dùng Hugging Face (16GB RAM)
   hoặc optimize PaddleOCR
```

### Build timeout
```
→ PaddleOCR dependencies lớn (~200MB)
   Đợi 5-10 phút cho lần build đầu
```

### Gemini API error
```
→ Check GEMINI_API_KEY đã set đúng
   trong Environment Variables
```

---

## 🎉 Next Steps

1. **Chọn platform** (recommend: Render.com)
2. **Follow hướng dẫn** trong DEPLOY_RENDER.md hoặc DEPLOY_HUGGINGFACE.md
3. **Deploy!**
4. **Share URL** với mọi người

**Good luck! 🚀**

