#!/usr/bin/env python3
"""
Module 4: Viewing and Understanding HTTP Responses
=================================================

This file demonstrates how to examine HTTP responses in detail,
understand status codes, headers, and different content types.

Learning Objectives:
- Understand response object properties
- Interpret HTTP status codes
- Examine response headers
- Handle different content types

Author: FSCJ - Software Defined Networking Course
"""

import requests
from datetime import datetime


def response_object_overview():
    """
    Explore the response object and its properties
    """
    print("=" * 60)
    print("RESPONSE OBJECT OVERVIEW")
    print("=" * 60)
    
    url = "https://httpbin.org/get"
    
    try:
        response = requests.get(url)
        
        print("📦 Response Object Properties:")
        print(f"   Type: {type(response)}")
        print(f"   Status Code: {response.status_code}")
        print(f"   Reason: {response.reason}")
        print(f"   URL: {response.url}")
        print(f"   Encoding: {response.encoding}")
        print(f"   Response Time: {response.elapsed.total_seconds():.3f}s")
        
        print(f"\n📊 Content Information:")
        print(f"   Content Length: {len(response.content)} bytes")
        print(f"   Text Length: {len(response.text)} characters")
        print(f"   Has JSON: {'Yes' if 'application/json' in response.headers.get('content-type', '') else 'No'}")
        
        print(f"\n🔗 Request Information:")
        print(f"   Method Used: {response.request.method}")
        print(f"   Final URL: {response.url}")
        
    except requests.RequestException as e:
        print(f"❌ Error: {e}")


def status_code_deep_dive():
    """
    Explore different HTTP status codes and their meanings
    """
    print("\n" + "=" * 60)
    print("HTTP STATUS CODES")
    print("=" * 60)
    
    # Status code categories and examples
    status_codes = {
        "2xx Success": {
            200: "OK - Request successful",
            201: "Created - Resource created successfully", 
            202: "Accepted - Request accepted for processing",
            204: "No Content - Successful but no content to return"
        },
        "3xx Redirection": {
            301: "Moved Permanently - Resource has new permanent URL",
            302: "Found - Resource temporarily at different URL",
            304: "Not Modified - Resource hasn't changed"
        },
        "4xx Client Error": {
            400: "Bad Request - Invalid request syntax",
            401: "Unauthorized - Authentication required",
            403: "Forbidden - Access denied",
            404: "Not Found - Resource doesn't exist",
            429: "Too Many Requests - Rate limit exceeded"
        },
        "5xx Server Error": {
            500: "Internal Server Error - Server encountered error",
            502: "Bad Gateway - Invalid response from upstream",
            503: "Service Unavailable - Server temporarily unavailable",
            504: "Gateway Timeout - Upstream server timeout"
        }
    }
    
    for category, codes in status_codes.items():
        print(f"\n🏷️  {category}:")
        for code, description in codes.items():
            print(f"   {code}: {description}")
    
    print("\n🧪 Testing Different Status Codes:")
    
    test_codes = [200, 404, 500]
    
    for code in test_codes:
        try:
            url = f"https://httpbin.org/status/{code}"
            response = requests.get(url, timeout=5)
            
            print(f"\n   Testing {code}:")
            print(f"   Status: {response.status_code} ({response.reason})")
            
            # Check if successful using different methods
            print(f"   response.ok: {response.ok}")
            print(f"   Is 2xx: {200 <= response.status_code < 300}")
            
            # Demonstrate raise_for_status()
            try:
                response.raise_for_status()
                print("   raise_for_status(): ✅ No exception")
            except requests.HTTPError as e:
                print(f"   raise_for_status(): ❌ {e}")
                
        except requests.RequestException as e:
            print(f"   ❌ Request failed: {e}")


def headers_examination():
    """
    Examine response headers in detail
    """
    print("\n" + "=" * 60)
    print("RESPONSE HEADERS ANALYSIS")
    print("=" * 60)
    
    url = "https://httpbin.org/response-headers"
    params = {
        'Server': 'FSCJ-Demo-Server',
        'X-Custom-Header': 'NetworkAutomation-Lab'
    }
    
    try:
        response = requests.get(url, params=params, timeout=5)
        
        print("📋 All Headers:")
        for name, value in response.headers.items():
            print(f"   {name}: {value}")
        
        print("\n🔍 Important Headers Analysis:")
        
        # Content-Type analysis
        content_type = response.headers.get('content-type', 'Not specified')
        print(f"   Content-Type: {content_type}")
        
        if 'application/json' in content_type:
            print("     → This is JSON data")
        elif 'text/html' in content_type:
            print("     → This is HTML content")
        elif 'text/plain' in content_type:
            print("     → This is plain text")
        
        # Server information
        server = response.headers.get('server', 'Not specified')
        print(f"   Server: {server}")
        
        # Content length
        content_length = response.headers.get('content-length', 'Not specified')
        print(f"   Content-Length: {content_length}")
        
        # Date information
        date = response.headers.get('date', 'Not specified')
        print(f"   Date: {date}")
        
        # Custom headers
        print(f"\n🎯 Custom Headers:")
        for name, value in response.headers.items():
            if name.lower().startswith('x-') or 'custom' in name.lower():
                print(f"   {name}: {value}")
        
    except requests.RequestException as e:
        print(f"❌ Error: {e}")


def content_types_handling():
    """
    Demonstrate handling different content types
    """
    print("\n" + "=" * 60)
    print("HANDLING DIFFERENT CONTENT TYPES")
    print("=" * 60)
    
    content_examples = [
        {
            "name": "JSON Content",
            "url": "https://httpbin.org/json",
            "expected_type": "application/json"
        },
        {
            "name": "HTML Content", 
            "url": "https://httpbin.org/html",
            "expected_type": "text/html"
        },
        {
            "name": "Plain Text",
            "url": "https://httpbin.org/robots.txt", 
            "expected_type": "text/plain"
        },
        {
            "name": "XML Content",
            "url": "https://httpbin.org/xml",
            "expected_type": "application/xml"
        }
    ]
    
    for example in content_examples:
        print(f"\n📄 {example['name']}:")
        
        try:
            response = requests.get(example['url'], timeout=5)
            actual_type = response.headers.get('content-type', '').split(';')[0]
            
            print(f"   Status: {response.status_code}")
            print(f"   Content-Type: {actual_type}")
            print(f"   Size: {len(response.content)} bytes")
            
            # Show appropriate way to access content
            if 'json' in actual_type:
                try:
                    data = response.json()
                    print(f"   JSON Keys: {list(data.keys()) if isinstance(data, dict) else 'Array or other'}")
                except ValueError:
                    print("   ⚠️  Content claimed to be JSON but couldn't parse")
            
            elif 'html' in actual_type or 'xml' in actual_type:
                # Show first 100 characters of markup
                preview = response.text[:100].replace('\n', ' ')
                print(f"   Preview: {preview}...")
                
            else:
                # Plain text or other
                lines = response.text.split('\n')
                print(f"   Lines: {len(lines)}")
                if lines:
                    print(f"   First line: {lines[0][:50]}...")
            
        except requests.RequestException as e:
            print(f"   ❌ Error: {e}")


def response_content_access():
    """
    Show different ways to access response content
    """
    print("\n" + "=" * 60)
    print("ACCESSING RESPONSE CONTENT")
    print("=" * 60)
    
    url = "https://httpbin.org/json"
    
    try:
        response = requests.get(url, timeout=5)
        
        print("🎯 Different Ways to Access Content:")
        
        # 1. Raw bytes
        raw_content = response.content
        print(f"\n1. response.content (bytes):")
        print(f"   Type: {type(raw_content)}")
        print(f"   Length: {len(raw_content)} bytes")
        print(f"   First 50 bytes: {raw_content[:50]}...")
        
        # 2. Decoded text
        text_content = response.text
        print(f"\n2. response.text (string):")
        print(f"   Type: {type(text_content)}")
        print(f"   Length: {len(text_content)} characters")
        print(f"   Encoding: {response.encoding}")
        print(f"   First 100 chars: {text_content[:100]}...")
        
        # 3. JSON data
        if 'application/json' in response.headers.get('content-type', ''):
            json_content = response.json()
            print(f"\n3. response.json() (Python object):")
            print(f"   Type: {type(json_content)}")
            if isinstance(json_content, dict):
                print(f"   Keys: {list(json_content.keys())}")
                print(f"   Sample value: {list(json_content.values())[0] if json_content else 'None'}")
        
        print(f"\n💡 When to use each method:")
        print("   • response.content: Binary data, images, files")
        print("   • response.text: Human-readable text, HTML, XML")
        print("   • response.json(): JSON data that needs to be processed")
        
    except requests.RequestException as e:
        print(f"❌ Error: {e}")


def response_timing_analysis():
    """
    Analyze response timing and performance
    """
    print("\n" + "=" * 60)
    print("RESPONSE TIMING ANALYSIS")
    print("=" * 60)
    
    urls_to_test = [
        ("Fast Response", "https://httpbin.org/get"),
        ("Delayed Response", "https://httpbin.org/delay/1"),
        ("Large Response", "https://httpbin.org/json")
    ]
    
    print("⏱️  Performance Analysis:")
    
    for name, url in urls_to_test:
        try:
            start_time = datetime.now()
            response = requests.get(url, timeout=10)
            end_time = datetime.now()
            
            total_time = (end_time - start_time).total_seconds()
            elapsed_time = response.elapsed.total_seconds()
            
            print(f"\n📊 {name}:")
            print(f"   Status: {response.status_code}")
            print(f"   Total Time: {total_time:.3f}s (including Python overhead)")
            print(f"   Network Time: {elapsed_time:.3f}s (requests library measurement)")
            print(f"   Content Size: {len(response.content):,} bytes")
            
            # Calculate throughput
            if elapsed_time > 0:
                throughput = len(response.content) / elapsed_time / 1024  # KB/s
                print(f"   Throughput: {throughput:.1f} KB/s")
            
        except requests.RequestException as e:
            print(f"\n📊 {name}: ❌ {e}")
    
    print(f"\n💡 Performance Tips:")
    print("   • Monitor response times in production")
    print("   • Set appropriate timeouts based on expected response times")
    print("   • Consider caching for frequently requested data")
    print("   • Use compression (gzip) for large responses")


def network_troubleshooting_with_responses():
    """
    Show how response analysis helps with network troubleshooting
    """
    print("\n" + "=" * 60)
    print("NETWORK TROUBLESHOOTING WITH RESPONSES")
    print("=" * 60)
    
    def diagnose_response(url, expected_status=200):
        """
        Perform comprehensive response diagnosis
        """
        print(f"\n🔍 Diagnosing: {url}")
        
        try:
            response = requests.get(url, timeout=10)
            
            # Basic status check
            if response.status_code == expected_status:
                print("   ✅ Status: Expected result")
            else:
                print(f"   ⚠️  Status: {response.status_code} (expected {expected_status})")
            
            # Performance check
            response_time = response.elapsed.total_seconds()
            if response_time < 1.0:
                print(f"   ✅ Performance: Fast ({response_time:.3f}s)")
            elif response_time < 5.0:
                print(f"   ⚠️  Performance: Acceptable ({response_time:.3f}s)")
            else:
                print(f"   ❌ Performance: Slow ({response_time:.3f}s)")
            
            # Content validation
            content_type = response.headers.get('content-type', '')
            if 'json' in content_type:
                try:
                    data = response.json()
                    print("   ✅ Content: Valid JSON")
                except ValueError:
                    print("   ❌ Content: Invalid JSON")
            
            # Server information
            server = response.headers.get('server', 'Unknown')
            print(f"   📋 Server: {server}")
            
            # Connection info
            print(f"   🔗 Final URL: {response.url}")
            
        except requests.exceptions.Timeout:
            print("   ⏰ ERROR: Request timeout")
            print("   💡 Possible causes: Server overload, network congestion")
            
        except requests.exceptions.ConnectionError:
            print("   🔌 ERROR: Connection failed")
            print("   💡 Possible causes: Server down, DNS issues, firewall")
            
        except requests.RequestException as e:
            print(f"   ❌ ERROR: {e}")
    
    # Test different scenarios
    test_scenarios = [
        ("Working API", "https://httpbin.org/get", 200),
        ("Not Found", "https://httpbin.org/status/404", 404),
        ("Server Error", "https://httpbin.org/status/500", 500)
    ]
    
    for name, url, expected in test_scenarios:
        print(f"\n🧪 Test Scenario: {name}")
        diagnose_response(url, expected)


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - VIEWING RESPONSES")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    response_object_overview()
    status_code_deep_dive()
    headers_examination()
    content_types_handling()
    response_content_access()
    response_timing_analysis()
    network_troubleshooting_with_responses()
    
    print("\n" + "=" * 60)
    print("🎓 NEXT STEPS")
    print("=" * 60)
    print("""
Great work! You now understand HTTP responses in detail.

Key concepts mastered:
✓ Response object properties and methods
✓ HTTP status codes and their meanings
✓ Response headers analysis
✓ Different content types (JSON, HTML, XML, text)
✓ Performance timing analysis
✓ Using responses for network troubleshooting

Next, you'll learn about:
• Converting JSON responses to Python dictionaries
• Working with nested JSON data structures
• Handling malformed JSON

Continue to: examples/05_json_conversion.py
    """)


if __name__ == "__main__":
    main()