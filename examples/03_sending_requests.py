#!/usr/bin/env python3
"""
Module 4: Sending Requests and Handling Responses
================================================

This file demonstrates how to actually send HTTP requests and handle
various response scenarios including errors and timeouts.

Learning Objectives:
- Learn best practices for sending requests
- Handle different types of errors and exceptions
- Implement timeout and retry strategies
- Work with sessions for multiple requests

Author: FSCJ - Software Defined Networking Course
"""

import requests
import time
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError


def basic_request_sending():
    """
    Demonstrate basic request sending patterns
    """
    print("=" * 60)
    print("BASIC REQUEST SENDING")
    print("=" * 60)
    
    print("1. Simple GET Request:")
    url = "https://httpbin.org/get"
    
    try:
        response = requests.get(url)
        print(f"   ✅ Success! Status: {response.status_code}")
        print(f"   ⏱️  Response time: {response.elapsed.total_seconds():.3f}s")
        print(f"   📦 Content length: {len(response.content)} bytes")
        
    except requests.RequestException as e:
        print(f"   ❌ Error occurred: {e}")
    
    print("\n2. Request with Parameters:")
    
    try:
        params = {'device': 'router', 'site': 'headquarters'}
        response = requests.get(url, params=params)
        print(f"   ✅ Success! Status: {response.status_code}")
        print(f"   🔗 Final URL: {response.url}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error occurred: {e}")


def timeout_handling():
    """
    Demonstrate proper timeout handling
    """
    print("\n" + "=" * 60)
    print("TIMEOUT HANDLING")
    print("=" * 60)
    
    print("1. Request with Timeout:")
    
    # Test with a delayed response
    url = "https://httpbin.org/delay/2"  # Server delays 2 seconds
    
    try:
        print("   Sending request with 3 second timeout...")
        response = requests.get(url, timeout=3)
        print(f"   ✅ Success! Took {response.elapsed.total_seconds():.2f}s")
        
    except Timeout:
        print("   ⏰ Request timed out!")
    except requests.RequestException as e:
        print(f"   ❌ Other error: {e}")
    
    print("\n2. Request that Times Out:")
    
    try:
        print("   Sending request with 1 second timeout (will timeout)...")
        response = requests.get(url, timeout=1)  # This will timeout
        print(f"   ✅ Unexpected success: {response.status_code}")
        
    except Timeout:
        print("   ⏰ Expected timeout occurred!")
    except requests.RequestException as e:
        print(f"   ❌ Other error: {e}")
    
    print("\n💡 Timeout Best Practices:")
    print("   • Always set timeouts for production code")
    print("   • Use reasonable timeouts (5-30 seconds for most APIs)")
    print("   • Consider separate connect and read timeouts")
    print("   • Example: requests.get(url, timeout=(3, 27))  # 3s connect, 27s read")


def error_handling_patterns():
    """
    Demonstrate comprehensive error handling
    """
    print("\n" + "=" * 60)
    print("ERROR HANDLING PATTERNS")
    print("=" * 60)
    
    # Different URLs that will cause different errors
    test_scenarios = [
        ("Valid Request", "https://httpbin.org/status/200"),
        ("Not Found Error", "https://httpbin.org/status/404"),
        ("Server Error", "https://httpbin.org/status/500"),
        ("Invalid URL", "https://this-domain-does-not-exist-12345.com"),
    ]
    
    for scenario_name, test_url in test_scenarios:
        print(f"\n{scenario_name}:")
        
        try:
            response = requests.get(test_url, timeout=5)
            
            # Check if request was successful
            response.raise_for_status()  # Raises HTTPError for bad status codes
            
            print(f"   ✅ Success! Status: {response.status_code}")
            
        except HTTPError as e:
            print(f"   🚫 HTTP Error: {e}")
            print(f"   📊 Status Code: {e.response.status_code}")
            
        except ConnectionError as e:
            print(f"   🔌 Connection Error: {e}")
            print("   💡 Check network connectivity or URL")
            
        except Timeout as e:
            print(f"   ⏰ Timeout Error: {e}")
            print("   💡 Server took too long to respond")
            
        except RequestException as e:
            print(f"   ❌ General Request Error: {e}")
            
        except Exception as e:
            print(f"   💥 Unexpected Error: {e}")


def retry_strategies():
    """
    Demonstrate retry strategies for failed requests
    """
    print("\n" + "=" * 60)
    print("RETRY STRATEGIES")
    print("=" * 60)
    
    def make_request_with_retry(url, max_retries=3, delay=1):
        """
        Make a request with retry logic
        """
        for attempt in range(max_retries):
            try:
                print(f"   Attempt {attempt + 1}/{max_retries}...")
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                return response
                
            except (ConnectionError, Timeout) as e:
                print(f"   ⚠️  Attempt {attempt + 1} failed: {type(e).__name__}")
                if attempt < max_retries - 1:  # Not the last attempt
                    print(f"   ⏳ Waiting {delay} seconds before retry...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    print(f"   ❌ All {max_retries} attempts failed!")
                    raise
            
            except HTTPError as e:
                print(f"   🚫 HTTP Error {e.response.status_code}: Not retrying")
                raise
    
    print("1. Retry with Intermittent Connection Issues:")
    
    # Simulate a request that might fail intermittently
    url = "https://httpbin.org/get"
    
    try:
        response = make_request_with_retry(url)
        if response is not None:
            print(f"   ✅ Final success! Status: {response.status_code}")
        else:
            print("   ❌ No response received after retries.")
        
    except RequestException as e:
        print(f"   ❌ Final failure: {e}")
    
    print("\n💡 Retry Strategy Best Practices:")
    print("   • Only retry on network errors (not HTTP errors like 404)")
    print("   • Use exponential backoff (1s, 2s, 4s, 8s...)")
    print("   • Limit the number of retries (3-5 attempts)")
    print("   • Add jitter to avoid thundering herd problems")


def session_usage():
    """
    Demonstrate using sessions for multiple requests
    """
    print("\n" + "=" * 60)
    print("USING SESSIONS")
    print("=" * 60)
    
    print("Sessions are useful for:")
    print("• Making multiple requests to the same server")
    print("• Keeping cookies between requests")
    print("• Reusing TCP connections (more efficient)")
    print("• Setting default headers for all requests")
    
    # Create a session
    session = requests.Session()
    
    # Set default headers for all requests in this session
    session.headers.update({
        'User-Agent': 'FSCJ-NetworkAutomation/1.0',
        'Accept': 'application/json'
    })
    
    print("\n1. Multiple Requests with Session:")
    
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/user-agent", 
        "https://httpbin.org/headers"
    ]
    
    for i, url in enumerate(urls, 1):
        try:
            response = session.get(url, timeout=5)
            print(f"   Request {i}: ✅ Status {response.status_code}")
            
        except RequestException as e:
            print(f"   Request {i}: ❌ Error {e}")
    
    print("\n2. Session with Authentication:")
    
    # Set authentication for all requests
    session.auth = ('demo_user', 'demo_password')
    
    try:
        # This would use the authentication for the request
        response = session.get('https://httpbin.org/get', timeout=5)
        print(f"   ✅ Authenticated request: Status {response.status_code}")
        
    except RequestException as e:
        print(f"   ❌ Authentication error: {e}")
    
    # Always close the session when done
    session.close()
    
    print("\n💡 Session Benefits:")
    print("   • Reuses underlying TCP connection")
    print("   • Persists cookies across requests")
    print("   • Can set default headers and auth")
    print("   • More efficient for multiple requests to same host")


def real_world_network_scenarios():
    """
    Show real-world network automation request patterns
    """
    print("\n" + "=" * 60)
    print("REAL-WORLD NETWORK SCENARIOS")
    print("=" * 60)
    
    def network_device_health_check():
        """
        Simulate checking multiple network devices
        """
        print("\n📊 Network Device Health Check:")
        
        # Simulated device endpoints
        devices = [
            {"name": "Router-01", "url": "https://httpbin.org/status/200"},
            {"name": "Switch-01", "url": "https://httpbin.org/status/200"}, 
            {"name": "Router-02", "url": "https://httpbin.org/status/503"},  # Simulated failure
            {"name": "Firewall-01", "url": "https://httpbin.org/status/200"}
        ]
        
        session = requests.Session()
        # Use a 10 second timeout for all requests by passing it to each call
        
        healthy_devices = 0
        total_devices = len(devices)
        
        for device in devices:
            try:
                response = session.get(device["url"], timeout=10)
                if response.status_code == 200:
                    print(f"   ✅ {device['name']}: Healthy")
                    healthy_devices += 1
                else:
                    print(f"   ⚠️  {device['name']}: Status {response.status_code}")
                    
            except RequestException as e:
                print(f"   ❌ {device['name']}: Connection failed ({e})")
        
        session.close()
        
        health_percentage = (healthy_devices / total_devices) * 100
        print(f"\n   📈 Network Health: {healthy_devices}/{total_devices} devices ({health_percentage:.1f}%)")
    
    def configuration_backup_simulation():
        """
        Simulate backing up device configurations
        """
        print("\n💾 Configuration Backup Simulation:")
        
        devices_to_backup = ["Router-01", "Switch-01", "Switch-02"]
        
        for device in devices_to_backup:
            try:
                # Simulate getting device configuration
                url = "https://httpbin.org/json"  # Returns sample JSON
                headers = {"Accept": "application/json"}
                
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                
                config_data = response.json()
                config_size = len(str(config_data))
                
                print(f"   ✅ {device}: Config backed up ({config_size} bytes)")
                
                # In real scenario, you'd save this to a file
                # with open(f'{device}_config.json', 'w') as f:
                #     json.dump(config_data, f)
                
            except RequestException as e:
                print(f"   ❌ {device}: Backup failed - {e}")
    
    def network_monitoring_alerts():
        """
        Simulate checking for network alerts
        """
        print("\n🚨 Network Monitoring Alerts:")
        
        # Simulate checking different monitoring endpoints
        monitoring_endpoints = [
            {"name": "Bandwidth Usage", "url": "https://httpbin.org/get?usage=normal"},
            {"name": "Error Rates", "url": "https://httpbin.org/get?errors=low"},
            {"name": "Latency Check", "url": "https://httpbin.org/delay/0.5"}  # Simulate network delay
        ]
        
        for endpoint in monitoring_endpoints:
            try:
                start_time = time.time()
                response_time = time.time() - start_time
                
                print(f"   📊 {endpoint['name']}: OK ({response_time:.2f}s response)")
                
            except Timeout:
                print(f"   ⏰ {endpoint['name']}: SLOW RESPONSE (timeout)")
            except RequestException as e:
                print(f"   ❌ {endpoint['name']}: ERROR - {e}")
    
    # Run all scenarios
    network_device_health_check()
    configuration_backup_simulation()
    network_monitoring_alerts()


def best_practices_summary():
    """
    Summarize best practices for sending requests
    """
    print("\n" + "=" * 60)
    print("BEST PRACTICES SUMMARY")
    print("=" * 60)
    
    practices = [
        {
            "category": "Error Handling",
            "tips": [
                "Always use try-except blocks",
                "Handle specific exception types",
                "Use response.raise_for_status()",
                "Provide meaningful error messages"
            ]
        },
        {
            "category": "Timeouts",
            "tips": [
                "Always set timeouts in production",
                "Use reasonable timeout values (5-30s)",
                "Consider connect vs read timeouts",
                "Document timeout decisions"
            ]
        },
        {
            "category": "Retries",
            "tips": [
                "Only retry on network errors",
                "Use exponential backoff",
                "Limit retry attempts (3-5)",
                "Add jitter for multiple clients"
            ]
        },
        {
            "category": "Sessions",
            "tips": [
                "Use sessions for multiple requests",
                "Set common headers once",
                "Reuse connections for efficiency",
                "Always close sessions when done"
            ]
        },
        {
            "category": "Monitoring",
            "tips": [
                "Log request performance",
                "Monitor error rates",
                "Track response times",
                "Alert on failures"
            ]
        }
    ]
    
    for practice in practices:
        print(f"\n🎯 {practice['category']}:")
        for tip in practice['tips']:
            print(f"   • {tip}")


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - SENDING REQUESTS")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    basic_request_sending()
    timeout_handling()
    error_handling_patterns()
    retry_strategies()
    session_usage()
    real_world_network_scenarios()
    best_practices_summary()
    
    print("\n" + "=" * 60)
    print("🎓 NEXT STEPS")
    print("=" * 60)
    print("""
Excellent! You now know how to send requests properly and handle errors.

Key skills learned:
✓ Basic request sending
✓ Timeout handling
✓ Comprehensive error handling
✓ Retry strategies with exponential backoff
✓ Using sessions for multiple requests
✓ Real-world network automation patterns

Next, you'll learn about:
• Examining response objects in detail
• Understanding status codes and headers
• Working with different response formats

Continue to: examples/04_viewing_responses.py
    """)


if __name__ == "__main__":
    main()