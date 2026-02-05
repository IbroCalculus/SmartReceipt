import requests
import sys

BASE_URL = "http://localhost:8001"
EMAIL = "testuser@example.com"
PASSWORD = "password123"

def test_api():
    print(f"Testing API at {BASE_URL}...")
    
    # 1. Health Check
    try:
        resp = requests.get(f"{BASE_URL}/health")
        if resp.status_code == 200:
            print("✅ Health Check Passed")
        else:
            print(f"❌ Health Check Failed: {resp.status_code}")
            return
    except Exception as e:
        print(f"❌ Failed to connect: {e}")
        return

    # 2. Register
    print("Trying Registration...")
    reg_data = {"email": EMAIL, "password": PASSWORD}
    try:
        resp = requests.post(f"{BASE_URL}/users/", json=reg_data)
        if resp.status_code == 200:
            print("✅ Registration Successful")
        elif resp.status_code == 400 and "already registered" in resp.text:
             print("ℹ️ User already registered. Proceeding to Login...")
        else:
             print(f"❌ Registration Failed: {resp.text}")
             if resp.status_code != 400: # Proceed if just dup user
                 return
    except Exception as e:
        print(f"❌ Registration Request Failed: {e}")
        return

    # 3. Login
    login_data = {
        "username": EMAIL,
        "password": PASSWORD
    }
    
    resp = requests.post(f"{BASE_URL}/token", data=login_data)
    if resp.status_code == 200:
        print("✅ Login Successful")
        token = resp.json()["access_token"]
    else:
        print(f"❌ Login Failed: {resp.text}")
        return

    # 4. Upload Receipt
    headers = {"Authorization": f"Bearer {token}"}
    files = {'file': ('receipt.jpg', b'fake image data', 'image/jpeg')}
    
    resp = requests.post(f"{BASE_URL}/receipts/", headers=headers, files=files)
    if resp.status_code == 200:
        print("✅ Receipt Upload Successful")
        print(resp.json())
    else:
        print(f"❌ Receipt Upload Failed: {resp.text}")

if __name__ == "__main__":
    test_api()
