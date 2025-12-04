import os
import io
import base64
import numpy as np
from flask import Flask, request, jsonify, render_template
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
from paddleocr import PaddleOCR

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your-api-key-here')

if GEMINI_API_KEY == 'your-api-key-here':
    print("⚠️  WARNING: GEMINI_API_KEY not set! Gemini features will not work.")
    print("   Please set: export GEMINI_API_KEY='your-actual-api-key'")
else:
    print(f"✅ Gemini API Key configured: {GEMINI_API_KEY[:10]}...")

genai.configure(api_key=GEMINI_API_KEY)

# Initialize Gemini model for text restoration
# Available models: 'gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-2.0-flash-exp'
# Note: 'gemini-2.5-flash' may not exist, use 'gemini-2.0-flash-exp' for latest
try:
    text_model = genai.GenerativeModel('gemini-2.5-flash')
    print("✅ Gemini model initialized: gemini-2.5-flash")
except Exception as e:
    print(f"⚠️  Error initializing gemini-2.5-flash: {e}")
    print("   Falling back to gemini-1.5-flash")
    text_model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize PaddleOCR
# use_angle_cls=True để detect góc xoay của text
# lang='vi' để hỗ trợ tiếng Việt tốt hơn
print("🔍 Initializing PaddleOCR (may take a moment first time)...")
ocr = PaddleOCR(use_angle_cls=True, lang='vi', show_log=False)
print("✅ PaddleOCR initialized")

def extract_text_from_image(image):
    """
    Extract text from image using PaddleOCR
    Args:
        image: PIL Image object
    Returns:
        str: Extracted text
    """
    try:
        # Convert PIL Image to numpy array
        img_array = np.array(image)
        
        # Perform OCR
        result = ocr.ocr(img_array, cls=True)
        
        if not result or not result[0]:
            return None
        
        # Extract text from result
        # PaddleOCR returns: [[[bbox], (text, confidence)], ...]
        extracted_lines = []
        for line in result[0]:
            if line and len(line) > 1:
                text = line[1][0]  # Get text from (text, confidence) tuple
                extracted_lines.append(text)
        
        # Join all lines with space
        extracted_text = ' '.join(extracted_lines)
        
        print(f"[PaddleOCR] Extracted text: {extracted_text}")
        
        return extracted_text if extracted_text else None
    except Exception as e:
        print(f"Error extracting text with PaddleOCR: {e}")
        return None

def restore_vietnamese_diacritics(text):
    """
    Restore Vietnamese diacritics using Gemini API
    """
    try:
        prompt = f"""
        Bạn là chuyên gia về tiếng Việt. Nhiệm vụ của bạn là phục hồi dấu tiếng Việt cho văn bản không dấu.

        Quy tắc:
        1. Phục hồi chính xác dấu thanh và dấu phụ cho tiếng Việt
        2. Hiểu ngữ cảnh về giao dịch chuyển tiền, chuyển khoản
        3. Các từ viết tắt phổ biến:
           - "ck" có thể là "chuyển khoản"
           - "chuyen khoan" → "chuyển khoản"
           - "du lich" → "du lịch"
           - "tien" → "tiền"
        4. Giữ nguyên số, ký hiệu đặc biệt
        5. Tên riêng cần viết hoa chữ cái đầu và có dấu chính xác
        6. CHỈ trả về văn bản đã được phục hồi dấu, KHÔNG thêm giải thích hay văn bản khác

        Văn bản cần phục hồi dấu:
        {text}

        Văn bản đã có dấu:
        """
        
        print(f"[Gemini] Sending request to restore diacritics for: {text[:50]}...")
        
        response = text_model.generate_content(prompt)
        
        # Try to get text from response
        # Method 1: Try response.text (preferred)
        try:
            restored_text = response.text.strip()
            print(f"[Gemini] Restored text: {restored_text}")
            return restored_text
        except Exception as text_error:
            print(f"[Gemini] Cannot get text directly: {text_error}")
            
            # Method 2: Try to get from candidates
            try:
                if response.candidates and len(response.candidates) > 0:
                    candidate = response.candidates[0]
                    if candidate.content and candidate.content.parts:
                        # Get text from first part
                        restored_text = candidate.content.parts[0].text.strip()
                        print(f"[Gemini] Restored text (from candidates): {restored_text}")
                        return restored_text
            except Exception as candidate_error:
                print(f"[Gemini] Cannot get text from candidates: {candidate_error}")
            
            # If all methods fail, show debug info
            try:
                if response.prompt_feedback:
                    print(f"[Gemini] Prompt feedback: {response.prompt_feedback}")
            except:
                pass
            
            return None
            
    except Exception as e:
        import traceback
        print(f"[ERROR] Error restoring diacritics: {e}")
        print(f"[ERROR] Traceback: {traceback.format_exc()}")
        return None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/process', methods=['POST'])
def process_image():
    """
    Process uploaded image:
    1. Extract text using OCR
    2. Restore Vietnamese diacritics
    """
    try:
        # Check if image is in request
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400
        
        image_file = request.files['image']
        
        # Read and validate image
        image_bytes = image_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Extract text from image
        extracted_text = extract_text_from_image(image)
        
        if not extracted_text:
            return jsonify({'error': 'Could not extract text from image'}), 400
        
        # Restore Vietnamese diacritics
        restored_text = restore_vietnamese_diacritics(extracted_text)
        
        if not restored_text:
            return jsonify({'error': 'Could not restore diacritics'}), 400
        
        return jsonify({
            'success': True,
            'original_text': extracted_text,
            'restored_text': restored_text
        })
    
    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/restore-text', methods=['POST'])
def restore_text_only():
    """
    Restore diacritics for text input (without image)
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        restored_text = restore_vietnamese_diacritics(text)
        
        if not restored_text:
            return jsonify({'error': 'Could not restore diacritics'}), 400
        
        return jsonify({
            'success': True,
            'original_text': text,
            'restored_text': restored_text
        })
    
    except Exception as e:
        print(f"Error restoring text: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🇻🇳 Vietnamese OCR - Starting Server")
    print("="*60)
    print(f"🌐 Server will run at: http://localhost:5001")
    print(f"📝 Press Ctrl+C to stop")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5001)

