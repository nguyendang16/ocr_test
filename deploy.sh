#!/bin/bash

echo "🚀 Quick Deploy Script"
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing git..."
    git init
    git add .
    git commit -m "Initial commit - Vietnamese OCR"
    echo "✅ Git initialized"
else
    echo "✅ Git already initialized"
fi

echo ""
echo "📋 Next steps:"
echo ""
echo "1️⃣  Push to GitHub:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/vietnamese-ocr.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "2️⃣  Deploy to Render.com:"
echo "   - Go to: https://render.com/"
echo "   - New Web Service → Connect your repo"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn main:app"
echo "   - Add Environment Variable: GEMINI_API_KEY"
echo ""
echo "📖 Xem DEPLOY_RENDER.md để biết chi tiết!"
echo ""
echo "🎯 Alternative: Hugging Face Spaces (unlimited free)"
echo "   Xem DEPLOY_HUGGINGFACE.md"
echo ""

