"""
Quick test script to check if Gemini API is working
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your-api-key-here')

print("="*60)
print("🧪 Testing Gemini API")
print("="*60)
print()

# Check API key
if GEMINI_API_KEY == 'your-api-key-here':
    print("❌ GEMINI_API_KEY not set!")
    print("   Please run: export GEMINI_API_KEY='your-actual-api-key'")
    exit(1)

print(f"✅ API Key found: {GEMINI_API_KEY[:10]}...{GEMINI_API_KEY[-4:]}")
print()

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Test different models
models_to_test = [
    'gemini-2.5-flash',      # Newest model
    'gemini-2.0-flash-exp',
    'gemini-1.5-flash',
    'gemini-1.5-pro'
]

successful_model = None

for model_name in models_to_test:
    print(f"Testing model: {model_name}")
    try:
        model = genai.GenerativeModel(model_name)
        
        # Simple test
        response = model.generate_content("Say 'Hello' in Vietnamese")
        
        # Try to get text (don't use hasattr as it can cause NotImplementedError)
        try:
            text_result = response.text
            print(f"  ✅ {model_name} works!")
            print(f"  Response: {text_result}")
            successful_model = model_name
            break
        except Exception as text_error:
            print(f"  ⚠️  {model_name} cannot get text: {text_error}")
            try:
                if response.prompt_feedback:
                    print(f"  Feedback: {response.prompt_feedback}")
            except:
                pass
    except Exception as e:
        print(f"  ❌ {model_name} failed: {e}")
    
    print()

if successful_model:
    print("="*60)
    print(f"✅ Recommended model: {successful_model}")
    print("="*60)
    print()
    
    # Test Vietnamese diacritics restoration
    print("Testing Vietnamese diacritics restoration...")
    model = genai.GenerativeModel(successful_model)
    
    test_text = "Tung ck du lich"
    prompt = f"""
    Phục hồi dấu tiếng Việt cho văn bản sau.
    CHỈ trả về văn bản đã có dấu, không giải thích.
    
    Văn bản: {test_text}
    """
    
    try:
        response = model.generate_content(prompt)
        try:
            result_text = response.text.strip()
            print(f"  Input:  {test_text}")
            print(f"  Output: {result_text}")
            print("  ✅ Vietnamese restoration works!")
        except Exception as text_error:
            print(f"  ❌ Cannot get text: {text_error}")
            try:
                if response.prompt_feedback:
                    print(f"  Feedback: {response.prompt_feedback}")
            except:
                pass
    except Exception as e:
        print(f"  ❌ Error: {e}")
else:
    print("="*60)
    print("❌ No working Gemini model found!")
    print("   Please check your API key and internet connection")
    print("="*60)

print()

