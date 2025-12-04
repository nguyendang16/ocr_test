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

Ứng dụng nhận diện và phục hồi dấu tiếng Việt từ văn bản không dấu.

## Tính năng
- 📷 OCR từ ảnh (PaddleOCR)
- ✏️ Nhập text trực tiếp
- 🎯 Hiểu ngữ cảnh chuyển tiền, giao dịch
- 🤖 AI thông minh (Gemini 2.5 Flash)

## Ví dụ
**Input:** `Tung ck du lich`  
**Output:** `Tùng chuyển khoản du lịch`

## Cấu hình
Cần set environment variable:
```
GEMINI_API_KEY=your-gemini-api-key
```

