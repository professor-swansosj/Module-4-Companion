#!/usr/bin/env python3
"""
Module 4: Introduction to the Python Requests Library
====================================================

This file introduces the Python Requests library and demonstrates basic concepts.

Learning Objectives:
- Understand what the Requests library is and why it's useful
- Learn basic terminology and concepts
- Make your first API call
- Understand the basic structure of HTTP requests and responses

Author: FSCJ - Software Defined Networking Course
"""

import requests
import json


def what_is_requests():
    """
    Introduction to the Requests library
    """
    print("=" * 60)
    print("WHAT IS THE PYTHON REQUESTS LIBRARY?")
    print("=" * 60)
    
    print("""
The Python Requests library is a simple, elegant HTTP library for Python.
It allows you to send HTTP requests easily and handle responses efficiently.

Key Features:
✓ Simple and intuitive API
✓ Automatic JSON decoding
✓ Built-in authentication support  
✓ Connection pooling and keep-alive
✓ Cookie persistence
✓ Automatic content decoding

Why use Requests for Network Automation?
• Interact with network device APIs
• Retrieve configuration data
• Send commands to network equipment
• Monitor network status and metrics
• Automate network provisioning tasks
    """)
    
    # Check if requests is installed
    print(f"Requests library version: {requests.__version__}")
    print("✓ Requests library is successfully imported!")


def basic_terminology():
    """
    Explain basic HTTP and API terminology
    """
    print("\n" + "=" * 60)
    print("BASIC TERMINOLOGY")
    print("=" * 60)
    
    terminology = {
        "HTTP": "HyperText Transfer Protocol - the protocol used for web communication",
        "API": "Application Programming Interface - allows programs to communicate",
        "Endpoint": "A specific URL where an API can be accessed",
        "Request": "A message sent to a server asking for data or action",
        "Response": "The server's reply to a request",
        "JSON": "JavaScript Object Notation - a lightweight data format",
        "Status Code": "A number indicating if the request was successful (200=OK, 404=Not Found)",
        "Headers": "Metadata about the request or response",
        "Payload": "The data being sent in a request (for POST, PUT requests)"
    }
    
    for term, definition in terminology.items():
        print(f"📘 {term:12}: {definition}")


def your_first_api_call():
    """
    Make your first API call using requests
    """
    print("\n" + "=" * 60)
    print("YOUR FIRST API CALL")
    print("=" * 60)
    
    # We'll use a simple, public API that doesn't require authentication
    url = "https://httpbin.org/get"
    
    print(f"Making a GET request to: {url}")
    print("This is a test API that simply returns information about your request.\n")
    
    try:
        # Make the request
        response = requests.get(url)
        
        # Basic information about the response
        print("📡 REQUEST SUCCESSFUL!")
        print(f"   Status Code: {response.status_code}")
        print(f"   Response Time: {response.elapsed.total_seconds():.2f} seconds")
        print(f"   Content Type: {response.headers.get('content-type', 'Unknown')}")
        
        # Show some of the response data
        data = response.json()
        print(f"\n📦 RESPONSE DATA (first few fields):")
        print(f"   Your IP Address: {data.get('origin', 'Unknown')}")
        print(f"   Request URL: {data.get('url', 'Unknown')}")
        
        print("\n✅ Congratulations! You've made your first API call!")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error making request: {e}")
        print("Check your internet connection and try again.")


def understanding_response_structure():
    """
    Demonstrate the basic structure of a response object
    """
    print("\n" + "=" * 60)
    print("UNDERSTANDING RESPONSE STRUCTURE")
    print("=" * 60)
    
    url = "https://httpbin.org/json"
    
    try:
        response = requests.get(url)
        
        print("When you make a request, you get back a Response object with:")
        print(f"📊 response.status_code: {response.status_code}")
        print(f"📝 response.text: (the raw response as text)")
        print(f"🗂️  response.json(): (converts JSON response to Python dict)")
        print(f"📋 response.headers: (metadata about the response)")
        print(f"⏱️  response.elapsed: {response.elapsed}")
        
        # Show headers (just a few important ones)
        print(f"\n📋 IMPORTANT HEADERS:")
        important_headers = ['content-type', 'server', 'content-length']
        for header in important_headers:
            value = response.headers.get(header, 'Not present')
            print(f"   {header}: {value}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")


def network_automation_example():
    """
    Show a simple example relevant to network automation
    """
    print("\n" + "=" * 60)
    print("NETWORK AUTOMATION EXAMPLE")
    print("=" * 60)
    
    print("""
🌐 Real-World Example: Getting Public IP Information

In network automation, you might want to:
- Check your public IP address
- Get geolocation information
- Verify network connectivity
- Monitor external network status

Let's try this with a real API:
    """)
    
    # Use a simple IP information API
    url = "https://httpbin.org/ip"
    
    try:
        print("Making request to get public IP information...")
        response = requests.get(url, timeout=5)  # 5 second timeout
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Your public IP: {data.get('origin', 'Unknown')}")
            print("\n💡 This type of API call could be used in network scripts to:")
            print("   • Verify external connectivity")
            print("   • Log public IP changes")  
            print("   • Integrate with network monitoring systems")
        else:
            print(f"⚠️  Unexpected status code: {response.status_code}")
            
    except requests.exceptions.Timeout:
        print("⏰ Request timed out - check network connectivity")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")


def practical_tips():
    """
    Share some practical tips for beginners
    """
    print("\n" + "=" * 60)
    print("PRACTICAL TIPS FOR BEGINNERS")
    print("=" * 60)
    
    tips = [
        "Always handle exceptions when making API calls",
        "Use timeouts to prevent hanging requests", 
        "Check status codes before processing responses",
        "Start with simple GET requests before trying POST/PUT/DELETE",
        "Read API documentation carefully",
        "Test API calls in small steps",
        "Keep your API keys secure (never commit them to code)",
        "Use proper error handling for production code"
    ]
    
    for i, tip in enumerate(tips, 1):
        print(f"{i:2d}. {tip}")


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - INTRODUCTION")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    what_is_requests()
    basic_terminology() 
    your_first_api_call()
    understanding_response_structure()
    network_automation_example()
    practical_tips()
    
    print("\n" + "=" * 60)
    print("🎓 NEXT STEPS")
    print("=" * 60)
    print("""
You've completed the introduction to the Requests library!

Next, you'll learn about:
• Creating different types of requests (GET, POST, PUT, DELETE)
• Adding headers and parameters
• Authentication methods
• Error handling strategies

Continue to: examples/02_creating_requests.py
    """)


if __name__ == "__main__":
    main()