#!/bin/bash

# Quick start script

echo "🇻🇳 Starting Vietnamese OCR..."
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  File .env không tồn tại"
    echo "   Vui lòng chạy: bash setup_env.sh"
    echo "   Hoặc tạo file .env với nội dung:"
    echo "   GEMINI_API_KEY=your-api-key-here"
    echo ""
    exit 1
fi

# Start the application
python3 main.py

