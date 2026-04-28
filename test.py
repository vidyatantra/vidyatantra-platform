import requests

# We'll use a free, public API for testing
BASE_URL = "https://jsonplaceholder.typicode.com"

def test_api():
    print("Starting API Test...\n")

    # 1. Test a GET request (Fetching data)
    print("--- Testing GET Request ---")
    response = requests.get(f"{BASE_URL}/posts/1")
    
    # Status code 200 means "OK"
    if response.status_code == 200:
        print("✅ GET Successful!")
        # Print the data we received (converted to a Python dictionary)
        print(response.json(), "\n")
    else:
        print(f"❌ GET Failed. Status Code: {response.status_code}\n")


    # 2. Test a POST request (Sending data)
    print("--- Testing POST Request ---")
    payload = {
        "title": "My Test Post",
        "body": "This is a test of the API.",
        "userId": 1
    }
    
    # We send the payload as JSON
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    
    # Status code 201 means "Created"
    if response.status_code == 201:
        print("✅ POST Successful!")
        print(response.json(), "\n")
    else:
        print(f"❌ POST Failed. Status Code: {response.status_code}\n")

if __name__ == "__main__":
    test_api()