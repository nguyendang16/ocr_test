# Vietnamese OCR - Render Deployment

## ⚠️ IMPORTANT: Chỉ dành cho Render.com

File này là Flask app, sử dụng cho Render.com deployment.

- **File này**: `main.py` - Flask app
- **Cho Hugging Face**: Dùng `app.py` - Gradio app
- **Requirements**: `requirements.txt` (không có Gradio)

## Start Command cho Render:
```
gunicorn main:app
```

**KHÔNG dùng:** `gunicorn app:app` (sẽ lỗi vì import Gradio)

