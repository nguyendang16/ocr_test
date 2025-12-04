"""
Test script để demo API của Vietnamese OCR
Chạy server trước khi chạy script này: python main.py
"""

import requests
import json

# Base URL của API
BASE_URL = "http://localhost:5000"

def test_restore_text():
    """Test API phục hồi dấu cho text"""
    print("\n" + "="*60)
    print("TEST 1: Phục hồi dấu cho text")
    print("="*60)
    
    test_cases = [
        "Tung ck du lich",
        "Chuyen tien mua sam",
        "Nguyen Van A chuyen khoan tien dien",
        "Thanh toan hoa don internet thang 12",
        "Gui tien cho ba me o que nha"
    ]
    
    for i, text in enumerate(test_cases, 1):
        print(f"\n[Test case {i}]")
        print(f"Input:  {text}")
        
        response = requests.post(
            f"{BASE_URL}/api/restore-text",
            headers={"Content-Type": "application/json"},
            json={"text": text}
        )
        
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                print(f"Output: {data['restored_text']}")
                print("✅ Thành công")
            else:
                print(f"❌ Lỗi: {data.get('error')}")
        else:
            print(f"❌ HTTP Error: {response.status_code}")

def test_process_image():
    """Test API OCR từ ảnh"""
    print("\n" + "="*60)
    print("TEST 2: OCR từ ảnh")
    print("="*60)
    
    # Note: Cần có file ảnh test để chạy test này
    image_path = "test_image.jpg"  # Thay đổi path này
    
    try:
        with open(image_path, 'rb') as f:
            files = {'image': f}
            response = requests.post(
                f"{BASE_URL}/api/process",
                files=files
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    print(f"Text gốc (OCR):    {data['original_text']}")
                    print(f"Text đã có dấu:    {data['restored_text']}")
                    print("✅ Thành công")
                else:
                    print(f"❌ Lỗi: {data.get('error')}")
            else:
                print(f"❌ HTTP Error: {response.status_code}")
    except FileNotFoundError:
        print(f"⚠️  File ảnh không tồn tại: {image_path}")
        print("   Tạo file ảnh test hoặc thay đổi path trong script")

def check_server():
    """Kiểm tra server có đang chạy không"""
    try:
        response = requests.get(BASE_URL, timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False

if __name__ == "__main__":
    print("\n" + "="*60)
    print("🇻🇳 VIETNAMESE OCR - API TEST SCRIPT")
    print("="*60)
    
    # Check if server is running
    if not check_server():
        print("\n❌ Server chưa chạy!")
        print("   Vui lòng chạy: python main.py")
        print("   Sau đó chạy lại script này")
        exit(1)
    
    print("\n✅ Server đang chạy tại:", BASE_URL)
    
    # Run tests
    test_restore_text()
    # test_process_image()  # Uncomment nếu có ảnh test
    
    print("\n" + "="*60)
    print("✅ Hoàn thành test!")
    print("="*60 + "\n")

