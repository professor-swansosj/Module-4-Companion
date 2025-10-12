#!/usr/bin/env python3
"""
Module 4: Creating Different Types of Requests
==============================================

This file demonstrates how to create different types of HTTP requests
using the Python Requests library.

Learning Objectives:
- Understand different HTTP methods (GET, POST, PUT, DELETE)
- Learn how to add headers and parameters
- Explore authentication methods
- Practice request customization

Author: FSCJ - Software Defined Networking Course
"""

import requests
import json
from datetime import datetime


def http_methods_overview():
    """
    Explain the different HTTP methods
    """
    print("=" * 60)
    print("HTTP METHODS OVERVIEW")
    print("=" * 60)
    
    methods = {
        "GET": {
            "purpose": "Retrieve data from server",
            "use_case": "Fetch device configurations, status, logs",
            "has_body": False
        },
        "POST": {
            "purpose": "Send data to create new resources",
            "use_case": "Create new network configurations, add devices",
            "has_body": True
        },
        "PUT": {
            "purpose": "Update or replace existing resources",
            "use_case": "Update device settings, replace configurations",
            "has_body": True
        },
        "DELETE": {
            "purpose": "Remove resources from server",
            "use_case": "Delete configurations, remove network policies",
            "has_body": False
        },
        "PATCH": {
            "purpose": "Partially update existing resources",
            "use_case": "Modify specific configuration parameters",
            "has_body": True
        }
    }
    
    for method, details in methods.items():
        print(f"🔧 {method:6}: {details['purpose']}")
        print(f"   📋 Use Case: {details['use_case']}")
        print(f"   📦 Has Body: {'Yes' if details['has_body'] else 'No'}")
        print()


def get_request_examples():
    """
    Demonstrate various GET request patterns
    """
    print("=" * 60)
    print("GET REQUEST EXAMPLES")
    print("=" * 60)
    
    # Basic GET request
    print("1. Basic GET Request:")
    print("   Purpose: Retrieve basic information")
    
    try:
        url = "https://httpbin.org/get"
        response = requests.get(url)
        print(f"   ✅ Status: {response.status_code}")
        print(f"   📊 Response size: {len(response.text)} characters")
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    print("\n2. GET with Query Parameters:")
    print("   Purpose: Filter or customize the response")
    
    try:
        url = "https://httpbin.org/get"
        params = {
            'device_type': 'router',
            'location': 'datacenter_1',
            'status': 'active'
        }
        response = requests.get(url, params=params)
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🔗 Final URL: {response.url}")
        
        # Show how parameters are added to URL
        data = response.json()
        print(f"   📝 Parameters sent: {data.get('args', {})}")
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    print("\n3. GET with Custom Headers:")
    print("   Purpose: Send metadata with your request")
    
    try:
        url = "https://httpbin.org/get"
        headers = {
            'User-Agent': 'NetworkAutomation-Tool/1.0',
            'Accept': 'application/json',
            'X-Network-Admin': 'student@fscj.edu'
        }
        response = requests.get(url, headers=headers)
        print(f"   ✅ Status: {response.status_code}")
        
        data = response.json()
        print(f"   📋 Headers sent: {list(data.get('headers', {}).keys())}")
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def post_request_examples():
    """
    Demonstrate POST request patterns
    """
    print("\n" + "=" * 60)
    print("POST REQUEST EXAMPLES")
    print("=" * 60)
    
    # POST with JSON data
    print("1. POST with JSON Data:")
    print("   Purpose: Send structured data to create resources")
    
    try:
        url = "https://httpbin.org/post"
        
        # Example: Creating a new network device configuration
        device_config = {
            'device_name': 'Router-Lab-01',
            'device_type': 'Cisco_ISR',
            'ip_address': '192.168.1.1',
            'location': 'Computer_Lab',
            'interfaces': [
                {'name': 'GigE0/0', 'ip': '10.1.1.1/24'},
                {'name': 'GigE0/1', 'ip': '10.1.2.1/24'}
            ],
            'created_by': 'FSCJ_Student',
            'timestamp': datetime.now().isoformat()
        }
        
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, json=device_config, headers=headers)
        
        print(f"   ✅ Status: {response.status_code}")
        print(f"   📦 Data sent: Device configuration for {device_config['device_name']}")
        
        # Show server received the data
        response_data = response.json()
        received_data = response_data.get('json', {})
        print(f"   📨 Server received device: {received_data.get('device_name', 'Unknown')}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    # POST with form data
    print("\n2. POST with Form Data:")
    print("   Purpose: Send form-like data (like HTML form submission)")
    
    try:
        url = "https://httpbin.org/post"
        
        # Example: Submitting network troubleshooting report
        form_data = {
            'ticket_id': 'NET-2024-001',
            'issue_type': 'connectivity',
            'severity': 'medium',
            'description': 'Intermittent packet loss on VLAN 100',
            'reporter': 'student@fscj.edu'
        }
        
        response = requests.post(url, data=form_data)
        
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🎫 Ticket ID: {form_data['ticket_id']}")
        
        response_data = response.json()
        received_form = response_data.get('form', {})
        print(f"   📝 Server received: {list(received_form.keys())}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def put_request_examples():
    """
    Demonstrate PUT request patterns
    """
    print("\n" + "=" * 60)
    print("PUT REQUEST EXAMPLES")
    print("=" * 60)
    
    print("1. PUT to Update Resource:")
    print("   Purpose: Replace/update an entire resource")
    
    try:
        url = "https://httpbin.org/put"
        
        # Example: Updating complete device configuration
        updated_config = {
            'device_id': 'RTR-001',
            'hostname': 'Router-Lab-01-Updated',
            'interfaces': {
                'GigE0/0': {
                    'ip': '10.1.1.1',
                    'mask': '255.255.255.0',
                    'status': 'up'
                },
                'GigE0/1': {
                    'ip': '10.1.2.1', 
                    'mask': '255.255.255.0',
                    'status': 'down'  # Status changed
                }
            },
            'routing_protocol': 'OSPF',
            'last_updated': datetime.now().isoformat(),
            'updated_by': 'network_admin'
        }
        
        response = requests.put(url, json=updated_config)
        
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🔄 Updated device: {updated_config['hostname']}")
        print(f"   ⏰ Last updated: {updated_config['last_updated'][:19]}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def delete_request_examples():
    """
    Demonstrate DELETE request patterns
    """
    print("\n" + "=" * 60)
    print("DELETE REQUEST EXAMPLES")
    print("=" * 60)
    
    print("1. DELETE Resource:")
    print("   Purpose: Remove a resource from the system")
    
    try:
        url = "https://httpbin.org/delete"
        
        # Example: Delete a network policy
        headers = {
            'Authorization': 'Bearer fake-token-for-demo',
            'X-Admin-User': 'network_admin@fscj.edu'
        }
        
        # Parameters to specify what to delete
        params = {
            'policy_id': 'POL-VLAN-100',
            'confirm': 'true'
        }
        
        response = requests.delete(url, headers=headers, params=params)
        
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🗑️  Requested deletion of policy: {params['policy_id']}")
        
        # Show what was sent
        response_data = response.json()
        print(f"   📝 Deletion parameters: {response_data.get('args', {})}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def authentication_examples():
    """
    Demonstrate different authentication methods
    """
    print("\n" + "=" * 60)
    print("AUTHENTICATION EXAMPLES")
    print("=" * 60)
    
    print("1. Basic Authentication:")
    print("   Purpose: Username/password authentication")
    
    try:
        url = "https://httpbin.org/basic-auth/testuser/testpass"
        
        # Method 1: Using auth parameter (recommended)
        response = requests.get(url, auth=('testuser', 'testpass'))
        print(f"   ✅ Status: {response.status_code} (Method 1: auth parameter)")
        
        # Method 2: Using headers manually  
        import base64
        credentials = base64.b64encode(b'testuser:testpass').decode('ascii')
        headers = {'Authorization': f'Basic {credentials}'}
        response = requests.get(url, headers=headers)
        print(f"   ✅ Status: {response.status_code} (Method 2: manual headers)")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    print("\n2. Bearer Token Authentication:")
    print("   Purpose: API token-based authentication")
    
    try:
        url = "https://httpbin.org/bearer"
        
        # Simulate API token authentication
        token = "example-api-token-12345"
        headers = {'Authorization': f'Bearer {token}'}
        
        response = requests.get(url, headers=headers)
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🔑 Token used: {token[:15]}...")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    print("\n3. API Key Authentication:")
    print("   Purpose: Simple API key in headers")
    
    try:
        url = "https://httpbin.org/get"
        
        headers = {
            'X-API-Key': 'your-api-key-here',
            'X-Client-ID': 'fscj-network-automation'
        }
        
        response = requests.get(url, headers=headers)
        print(f"   ✅ Status: {response.status_code}")
        
        data = response.json()
        api_key_sent = data.get('headers', {}).get('X-Api-Key', 'Not found')
        print(f"   🔐 API Key sent: {api_key_sent}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def request_customization():
    """
    Show advanced request customization options
    """
    print("\n" + "=" * 60)
    print("ADVANCED REQUEST CUSTOMIZATION")
    print("=" * 60)
    
    print("1. Timeout and Connection Settings:")
    
    try:
        url = "https://httpbin.org/delay/1"  # API that delays 1 second
        
        # Request with timeout
        response = requests.get(url, timeout=2.0)  # 2 second timeout
        print(f"   ✅ Request completed in: {response.elapsed.total_seconds():.2f}s")
        print(f"   ⏰ Timeout setting: 2.0 seconds")
        
    except requests.exceptions.Timeout:
        print("   ⏰ Request timed out!")
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")
    
    print("\n2. Custom User Agent and Headers:")
    
    try:
        url = "https://httpbin.org/user-agent"
        
        headers = {
            'User-Agent': 'FSCJ-NetworkAutomation-Bot/1.0 (Educational)',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'X-Student-ID': 'student123',
            'X-Course': 'Software-Defined-Networking'
        }
        
        response = requests.get(url, headers=headers)
        data = response.json()
        
        print(f"   ✅ Status: {response.status_code}")
        print(f"   🤖 User-Agent sent: {data.get('user-agent', 'Unknown')}")
        
    except requests.RequestException as e:
        print(f"   ❌ Error: {e}")


def network_automation_scenarios():
    """
    Show realistic network automation scenarios
    """
    print("\n" + "=" * 60)
    print("NETWORK AUTOMATION SCENARIOS")
    print("=" * 60)
    
    scenarios = [
        {
            "title": "Device Configuration Backup",
            "method": "GET",
            "description": "Retrieve current configuration from network device",
            "example_url": "https://router.company.com/api/v1/config",
            "headers": {"Accept": "application/json", "X-Auth-Token": "device-token"}
        },
        {
            "title": "VLAN Creation", 
            "method": "POST",
            "description": "Create a new VLAN on a switch",
            "example_url": "https://switch.company.com/api/v1/vlans",
            "data": {"vlan_id": 100, "name": "Finance_VLAN", "description": "Finance Department"}
        },
        {
            "title": "Interface Status Update",
            "method": "PUT", 
            "description": "Enable/disable a network interface",
            "example_url": "https://switch.company.com/api/v1/interfaces/GigE0/1",
            "data": {"admin_status": "up", "description": "Connected to Server"}
        },
        {
            "title": "Security Policy Removal",
            "method": "DELETE",
            "description": "Remove an outdated firewall rule",
            "example_url": "https://firewall.company.com/api/v1/rules/RULE-123",
            "params": {"force": "true"}
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"{i}. {scenario['title']} ({scenario['method']})")
        print(f"   📝 {scenario['description']}")
        print(f"   🔗 URL Pattern: {scenario['example_url']}")
        if 'headers' in scenario:
            print(f"   📋 Headers: {scenario['headers']}")
        if 'data' in scenario:
            print(f"   📦 Data: {scenario['data']}")
        if 'params' in scenario:
            print(f"   ❓ Params: {scenario['params']}")
        print()


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - CREATING REQUESTS")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    http_methods_overview()
    get_request_examples()
    post_request_examples()
    put_request_examples()
    delete_request_examples()
    authentication_examples()
    request_customization()
    network_automation_scenarios()
    
    print("\n" + "=" * 60)
    print("🎓 NEXT STEPS")
    print("=" * 60)
    print("""
Great! You've learned how to create different types of requests.

Key takeaways:
✓ GET for retrieving data
✓ POST for creating new resources
✓ PUT for updating existing resources
✓ DELETE for removing resources
✓ Authentication methods (Basic, Bearer, API Key)
✓ Request customization (headers, timeouts, parameters)

Next, you'll learn about:
• Actually sending requests and handling responses
• Error handling and retry strategies  
• Working with sessions and cookies

Continue to: examples/03_sending_requests.py
    """)


if __name__ == "__main__":
    main()