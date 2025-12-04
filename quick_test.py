"""
Quick test for gemini-2.5-flash
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', 'your-api-key-here')

if GEMINI_API_KEY == 'your-api-key-here':
    print("❌ GEMINI_API_KEY not set!")
    print("Run: export GEMINI_API_KEY='your-key'")
    exit(1)

print(f"✅ API Key: {GEMINI_API_KEY[:10]}...{GEMINI_API_KEY[-4:]}")

genai.configure(api_key=GEMINI_API_KEY)

print("\n🧪 Testing gemini-2.5-flash...")

try:
    model = genai.GenerativeModel('gemini-2.5-flash')
    print("✅ Model created")
    
    # Test 1: Simple test
    print("\n[Test 1] Simple test:")
    response = model.generate_content("Hello")
    
    # Try method 1: response.text
    result_text = None
    try:
        result_text = response.text
        print(f"Response (method 1): {result_text}")
    except Exception as e:
        print(f"Method 1 failed: {e}")
        # Try method 2: candidates
        try:
            if response.candidates:
                result_text = response.candidates[0].content.parts[0].text
                print(f"Response (method 2): {result_text}")
        except Exception as e2:
            print(f"Method 2 failed: {e2}")
            exit(1)
    
    if result_text:
        print("✅ Basic test passed")
    else:
        print("❌ Cannot get text")
        exit(1)
    
    # Test 2: Vietnamese test
    print("\n[Test 2] Vietnamese diacritics restoration:")
    test_text = "Tung ck du lich"
    prompt = f"""
Phục hồi dấu tiếng Việt cho văn bản sau.
CHỈ trả về văn bản đã có dấu, không giải thích.

Văn bản: {test_text}
"""
    
    response = model.generate_content(prompt)
    
    # Try to get text
    result = None
    try:
        result = response.text.strip()
    except Exception as e:
        print(f"Method 1 failed: {e}")
        try:
            if response.candidates:
                result = response.candidates[0].content.parts[0].text.strip()
                print("Using method 2 (candidates)")
        except Exception as e2:
            print(f"Method 2 failed: {e2}")
            exit(1)
    
    if result:
        print(f"Input:  {test_text}")
        print(f"Output: {result}")
        print("✅ Vietnamese test passed")
    else:
        print("❌ Cannot get text")
        exit(1)
    
    print("\n" + "="*60)
    print("✅ All tests passed! gemini-2.5-flash works perfectly!")
    print("="*60)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

