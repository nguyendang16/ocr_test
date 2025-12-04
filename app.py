import os
import gradio as gr
import numpy as np
from PIL import Image
import google.generativeai as genai
from paddleocr import PaddleOCR

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)
    text_model = genai.GenerativeModel('gemini-2.5-flash')
else:
    print("⚠️ GEMINI_API_KEY not set!")

# Initialize PaddleOCR
print("🔍 Initializing PaddleOCR...")
ocr = PaddleOCR(use_angle_cls=True, lang='vi', show_log=False)
print("✅ PaddleOCR initialized")

def extract_text_from_image(image):
    """Extract text using PaddleOCR"""
    try:
        img_array = np.array(image)
        result = ocr.ocr(img_array, cls=True)
        
        if not result or not result[0]:
            return None
        
        extracted_lines = []
        for line in result[0]:
            if line and len(line) > 1:
                text = line[1][0]
                extracted_lines.append(text)
        
        return ' '.join(extracted_lines) if extracted_lines else None
    except Exception as e:
        print(f"OCR Error: {e}")
        return None

def restore_vietnamese_diacritics(text):
    """Restore Vietnamese diacritics using Gemini"""
    try:
        prompt = f"""
Bạn là chuyên gia về tiếng Việt. Nhiệm vụ của bạn là phục hồi dấu tiếng Việt cho văn bản không dấu.

Quy tắc:
1. Phục hồi chính xác dấu thanh và dấu phụ cho tiếng Việt
2. Hiểu ngữ cảnh về giao dịch chuyển tiền, chuyển khoản
3. Các từ viết tắt phổ biến:
   - "ck" có thể là "chuyển khoản"
4. Giữ nguyên số, ký hiệu đặc biệt
5. Tên riêng cần viết hoa chữ cái đầu và có dấu chính xác
6. CHỈ trả về văn bản đã được phục hồi dấu, KHÔNG thêm giải thích hay văn bản khác

Văn bản cần phục hồi dấu:
{text}

Văn bản đã có dấu:
"""
        
        response = text_model.generate_content(prompt)
        
        try:
            return response.text.strip()
        except:
            if response.candidates:
                return response.candidates[0].content.parts[0].text.strip()
            return None
    except Exception as e:
        print(f"Gemini Error: {e}")
        return None

def process_image(image):
    """Main processing function for image"""
    if image is None:
        return "⚠️ Vui lòng upload ảnh", ""
    
    # Extract text
    original_text = extract_text_from_image(image)
    if not original_text:
        return "❌ Không thể nhận diện text từ ảnh", ""
    
    # Restore diacritics
    restored_text = restore_vietnamese_diacritics(original_text)
    if not restored_text:
        return original_text, "❌ Không thể phục hồi dấu"
    
    return original_text, restored_text

def process_text(text):
    """Main processing function for text input"""
    if not text or not text.strip():
        return "⚠️ Vui lòng nhập văn bản"
    
    restored_text = restore_vietnamese_diacritics(text.strip())
    if not restored_text:
        return "❌ Không thể phục hồi dấu"
    
    return restored_text

# Create Gradio interface
with gr.Blocks(title="Vietnamese OCR - Phục hồi dấu tiếng Việt") as demo:
    gr.Markdown("""
    # 🇻🇳 Vietnamese OCR - Phục hồi dấu tiếng Việt
    
    Ứng dụng nhận diện và phục hồi dấu tiếng Việt từ văn bản không dấu sử dụng PaddleOCR và Gemini AI.
    """)
    
    with gr.Tabs():
        # Tab 1: Upload ảnh
        with gr.Tab("📷 Upload Ảnh"):
            with gr.Row():
                with gr.Column():
                    image_input = gr.Image(type="pil", label="Upload ảnh chứa text không dấu")
                    image_button = gr.Button("🚀 Xử lý ảnh", variant="primary")
                
                with gr.Column():
                    original_output = gr.Textbox(label="📄 Văn bản gốc (không dấu)", lines=5)
                    restored_output = gr.Textbox(label="✅ Văn bản đã có dấu", lines=5)
            
            gr.Examples(
                examples=[],
                inputs=image_input,
                label="Ví dụ"
            )
        
        # Tab 2: Nhập text
        with gr.Tab("✏️ Nhập Text"):
            with gr.Row():
                with gr.Column():
                    text_input = gr.Textbox(
                        label="Nhập văn bản không dấu",
                        placeholder="Ví dụ: Tung ck du lich",
                        lines=5
                    )
                    text_button = gr.Button("🚀 Phục hồi dấu", variant="primary")
                
                with gr.Column():
                    text_output = gr.Textbox(label="✅ Văn bản đã có dấu", lines=5)
            
            gr.Examples(
                examples=[
                    ["Tung ck du lich"],
                    ["Chuyen tien mua sam"],
                    ["Nguyen Van A chuyen khoan tien dien"],
                    ["Thanh toan hoa don internet"],
                ],
                inputs=text_input,
                label="Ví dụ"
            )
    
    # Event handlers
    image_button.click(
        fn=process_image,
        inputs=[image_input],
        outputs=[original_output, restored_output]
    )
    
    text_button.click(
        fn=process_text,
        inputs=[text_input],
        outputs=[text_output]
    )
    
    gr.Markdown("""
    ---
    ### 📝 Lưu ý:
    - Ảnh cần rõ ràng, text dễ đọc để OCR chính xác
    - Hỗ trợ tốt nhất cho văn bản đánh máy (printed text)
    - Hiểu ngữ cảnh chuyển tiền, giao dịch
    
    ### 🛠️ Công nghệ:
    - **PaddleOCR**: Nhận diện text tiếng Việt
    - **Google Gemini 2.5 Flash**: Phục hồi dấu thông minh
    
    **Made with ❤️ using Gradio + PaddleOCR + Gemini AI**
    """)

# Launch
if __name__ == "__main__":
    demo.launch()

