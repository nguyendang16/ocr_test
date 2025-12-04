#!/bin/bash

# Script setup môi trường cho Vietnamese OCR

echo "=========================================="
echo "🇻🇳 Vietnamese OCR - Setup"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 chưa được cài đặt"
    echo "   Vui lòng cài đặt Python 3.8+ từ: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python đã cài đặt: $(python3 --version)"
echo ""

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 chưa được cài đặt"
    exit 1
fi

echo "✅ pip đã cài đặt"
echo ""

# Install dependencies
echo "📦 Đang cài đặt dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Đã cài đặt thành công tất cả dependencies"
else
    echo "❌ Có lỗi khi cài đặt dependencies"
    exit 1
fi

echo ""
echo "=========================================="
echo "🔑 Cấu hình API Key"
echo "=========================================="
echo ""

# Check if .env exists
if [ -f .env ]; then
    echo "⚠️  File .env đã tồn tại"
    read -p "Bạn có muốn ghi đè? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Giữ nguyên file .env hiện tại"
        echo ""
    else
        read -p "Nhập Gemini API Key của bạn: " api_key
        echo "GEMINI_API_KEY=$api_key" > .env
        echo "✅ Đã lưu API key vào .env"
    fi
else
    read -p "Nhập Gemini API Key của bạn: " api_key
    echo "GEMINI_API_KEY=$api_key" > .env
    echo "✅ Đã tạo file .env với API key"
fi

echo ""
echo "=========================================="
echo "✅ Setup hoàn tất!"
echo "=========================================="
echo ""
echo "Để chạy ứng dụng:"
echo "  python3 main.py"
echo ""
echo "Sau đó mở trình duyệt tại:"
echo "  http://localhost:5000"
echo ""
echo "Để test API:"
echo "  python3 test_api.py"
echo ""

