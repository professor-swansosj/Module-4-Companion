"""
Module 06: Network API Patterns - Real-World Network Automation Prep
TODO: Practice with network-device-style API patterns and authentication

Your mission:
1. Work with APIs that require authentication headers
2. Handle different response formats (like network devices use)
3. Practice patterns common in network automation
4. Build skills for real network device APIs

Hint: Network devices often require special headers and authentication!
"""

import requests
import json
import base64

def authenticated_api_call():
    """
    TODO: Practice making API calls with authentication headers
    
    Steps to complete:
    1. TODO: Create headers with authentication and content-type
    2. TODO: Make API call to httpbin.org/headers to see your headers
    3. TODO: Extract and display the headers the API received
    4. TODO: Practice with different header combinations
    
    Hint: httpbin.org is perfect for testing - it echoes back what you send!
    """
    print("🔐 Testing Authenticated API Calls...")
    
    # TODO: Create headers like network devices expect
    headers = {
        # TODO: Add authentication header
        # 'Authorization': 'Basic ' + base64.b64encode(b'admin:password').decode(),
        # TODO: Add content type
        # 'Content-Type': 'application/json',
        # TODO: Add user agent
        # 'User-Agent': 'NetworkAutomation-Python/1.0'
    }
    
    # Test endpoint that echoes headers back
    url = "https://httpbin.org/headers"
    
    try:
        # TODO: Make request with headers
        # response = requests.get(url, headers=headers)
        
        # TODO: Extract and display received headers
        # data = response.json()
        # received_headers = data['headers']
        
        print("📡 Headers sent to API:")
        # TODO: Display your headers nicely
        # for key, value in headers.items():
        #     print(f"   {key}: {value}")
        
        print("\n📨 Headers received by API:")
        # TODO: Display received headers
        # for key, value in received_headers.items():
        #     print(f"   {key}: {value}")
            
        print("TODO: Implement authenticated API call!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API call failed: {e}")

def network_device_simulation():
    """
    TODO: Simulate network device API interaction patterns
    
    Steps to complete:
    1. TODO: Get "device status" from httpbin.org/json
    2. TODO: Parse response like it's network device data
    3. TODO: Extract specific "configuration" fields
    4. TODO: Format output like network management tools
    
    🎮 Try This: Pretend the JSON response is from a router!
    """
    print("\n🌐 Simulating Network Device API...")
    
    # Simulate getting device status
    url = "https://httpbin.org/json"
    
    try:
        print("📡 Querying 'network device' status...")
        
        # TODO: Make API call
        # response = requests.get(url)
        
        # TODO: Parse JSON response
        # device_data = response.json()
        
        # TODO: Display as if it's network device info
        print("\n🔧 DEVICE STATUS REPORT")
        print("=" * 40)
        
        # TODO: Extract and format data like network info
        # print(f"Device Type: {device_data.get('slideshow', {}).get('author', 'Unknown')}")
        # print(f"Status: Online")
        # print(f"Response Time: {response.elapsed.total_seconds():.3f}s")
        
        # TODO: Show raw data structure
        print("\n📋 Raw Device Data:")
        # print(json.dumps(device_data, indent=2))
        
        print("TODO: Implement network device simulation!")
        
    except Exception as e:
        print(f"❌ Device communication failed: {e}")

def test_different_methods():
    """
    TODO: Practice different HTTP methods (GET, POST, PUT)
    
    This simulates how you'd interact with network device APIs
    that support configuration changes via different HTTP methods.
    """
    print("\n🛠️ Testing Different HTTP Methods...")
    
    base_url = "https://httpbin.org"
    
    # TODO: Test GET (like getting device config)
    print("\n1. GET Request (Read Configuration):")
    try:
        # TODO: Make GET request
        # response = requests.get(f"{base_url}/get")
        print("TODO: Implement GET request")
    except Exception as e:
        print(f"❌ GET failed: {e}")
    
    # TODO: Test POST (like adding configuration)
    print("\n2. POST Request (Add Configuration):")
    try:
        config_data = {"interface": "GigabitEthernet0/1", "ip": "192.168.1.1"}
        # TODO: Make POST request with JSON data
        # response = requests.post(f"{base_url}/post", json=config_data)
        print("TODO: Implement POST request with config data")
    except Exception as e:
        print(f"❌ POST failed: {e}")
    
    # TODO: Test PUT (like updating configuration)  
    print("\n3. PUT Request (Update Configuration):")
    try:
        update_data = {"interface": "GigabitEthernet0/1", "ip": "192.168.1.10"}
        # TODO: Make PUT request
        # response = requests.put(f"{base_url}/put", json=update_data)
        print("TODO: Implement PUT request")
    except Exception as e:
        print(f"❌ PUT failed: {e}")

def main():
    """
    TODO: Test all network-ready API patterns
    """
    print("🌐 Network API Readiness Test!")
    print("=" * 50)
    
    # TODO: Test authenticated calls
    authenticated_api_call()
    
    # TODO: Test network device simulation
    # network_device_simulation()
    
    # TODO: Test different HTTP methods
    # test_different_methods()
    
    print("\n🎉 CONGRATULATIONS!")
    print("You're ready for real network device APIs!")
    print("Your next step: Connect to actual network equipment!")

if __name__ == "__main__":
    main()