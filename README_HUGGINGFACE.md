---
title: Vietnamese OCR
emoji: 🇻🇳
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: mit
---

# Vietnamese OCR - Phục hồi dấu tiếng Việt

**⚠️ Chú ý:** File này dành cho Hugging Face Spaces

Ứng dụng nhận diện và phục hồi dấu tiếng Việt từ văn bản không dấu.

## Setup cho Hugging Face
1. Copy `app.py` và `requirements_hf.txt` 
2. Rename `requirements_hf.txt` → `requirements.txt`
3. Add secret: `GEMINI_API_KEY`

## Tính năng
- 📷 OCR từ ảnh (PaddleOCR)
- ✏️ Nhập text trực tiếp
- 🎯 Hiểu ngữ cảnh chuyển tiền, giao dịch
- 🤖 AI thông minh (Gemini 2.5 Flash)

