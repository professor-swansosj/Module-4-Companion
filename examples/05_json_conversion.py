#!/usr/bin/env python3
"""
Module 4: Converting JSON Response to Python Dictionary
======================================================

This file demonstrates how to work with JSON responses from APIs,
convert them to Python data structures, and handle various scenarios.

Learning Objectives:
- Convert JSON responses to Python dictionaries
- Handle nested JSON structures
- Deal with malformed JSON and errors
- Work with JSON arrays and complex data

Author: FSCJ - Software Defined Networking Course
"""

import requests
import json
from datetime import datetime


def json_basics():
    """
    Introduction to JSON and its relationship to Python dictionaries
    """
    print("=" * 60)
    print("JSON BASICS")
    print("=" * 60)
    
    print("📚 JSON (JavaScript Object Notation) Overview:")
    print("• Lightweight data-interchange format")
    print("• Human-readable text format")
    print("• Language-independent (despite the name)")
    print("• Perfect for API communication")
    print("• Maps directly to Python data types")
    
    print("\n🔄 JSON ↔ Python Mapping:")
    
    mappings = [
        ("JSON Object { }", "Python Dictionary dict()"),
        ("JSON Array [ ]", "Python List list()"), 
        ("JSON String", "Python String str()"),
        ("JSON Number", "Python int() or float()"),
        ("JSON Boolean", "Python bool()"),
        ("JSON null", "Python None")
    ]
    
    for json_type, python_type in mappings:
        print(f"   {json_type:15} → {python_type}")
    
    print("\n🎯 Example JSON → Python Conversion:")
    
    # Example JSON string
    json_string = '''
    {
        "device_name": "Router-01",
        "ip_address": "192.168.1.1",
        "ports": [22, 80, 443],
        "is_active": true,
        "last_seen": null,
        "interfaces": {
            "eth0": "10.1.1.1",
            "eth1": "10.1.2.1"
        }
    }
    '''
    
    # Parse JSON string to Python dictionary
    device_data = json.loads(json_string)
    
    print("   JSON String →")
    print(f"   Python Dict: {type(device_data)}")
    print(f"   Keys: {list(device_data.keys())}")
    print(f"   Device Name: {device_data['device_name']}")
    print(f"   Ports: {device_data['ports']} (type: {type(device_data['ports'])})")
    print(f"   Is Active: {device_data['is_active']} (type: {type(device_data['is_active'])})")


def basic_json_conversion():
    """
    Demonstrate basic JSON response conversion
    """
    print("\n" + "=" * 60)
    print("BASIC JSON CONVERSION")
    print("=" * 60)
    
    print("1. Simple JSON Response:")
    
    try:
        url = "https://httpbin.org/json"
        response = requests.get(url, timeout=5)
        
        print(f"   Status: {response.status_code}")
        print(f"   Content-Type: {response.headers.get('content-type')}")
        
        # Method 1: Using .json() method (recommended)
        data = response.json()
        
        print("\n   📦 Converted Data:")
        print(f"   Type: {type(data)}")
        print(f"   Keys: {list(data.keys()) if isinstance(data, dict) else 'Not a dictionary'}")
        
        # Access specific values
        if isinstance(data, dict):
            for key, value in data.items():
                print(f"   {key}: {value} ({type(value).__name__})")
        
        print("\n   ✅ JSON conversion successful!")
        
    except ValueError as e:
        print(f"   ❌ JSON parsing error: {e}")
    except requests.RequestException as e:
        print(f"   ❌ Request error: {e}")
    
    print("\n2. Network Device API Simulation:")
    
    # Simulate a network device API response
    try:
        url = "https://httpbin.org/json"
        response = requests.get(url, timeout=5)
        
        # In a real scenario, this might be device information
        print("   Simulating device status API response...")
        
        if response.status_code == 200:
            device_info = response.json()
            
            # Simulate processing device information
            print("   📊 Processing device data:")
            print(f"   Response type: {type(device_info)}")
            
            # In real network automation, you might process data like:
            # if device_info.get('status') == 'online':
            #     print("   ✅ Device is online")
            # else:
            #     print("   ⚠️  Device may be offline")
            
            print("   ✅ Device data processed successfully")
        
    except Exception as e:
        print(f"   ❌ Error processing device data: {e}")


def nested_json_handling():
    """
    Demonstrate handling nested JSON structures
    """
    print("\n" + "=" * 60)
    print("NESTED JSON HANDLING")
    print("=" * 60)
    
    print("📚 Understanding Nested JSON:")
    print("Network APIs often return complex, nested data structures")
    
    # Example of complex nested JSON (simulated network topology)
    network_topology = {
        "network_id": "CORP_NET_001",
        "description": "Corporate Network Topology", 
        "created": datetime.now().isoformat(),
        "devices": [
            {
                "device_id": "RTR-001",
                "type": "router",
                "hostname": "corp-router-01",
                "management_ip": "10.0.1.1",
                "interfaces": [
                    {
                        "name": "GigE0/0",
                        "ip": "192.168.1.1",
                        "netmask": "255.255.255.0",
                        "status": "up",
                        "connected_devices": ["SW-001", "SW-002"]
                    },
                    {
                        "name": "GigE0/1", 
                        "ip": "10.10.1.1",
                        "netmask": "255.255.255.0",
                        "status": "down",
                        "connected_devices": []
                    }
                ],
                "protocols": {
                    "ospf": {"area": "0.0.0.0", "enabled": True},
                    "bgp": {"asn": 65001, "enabled": False}
                }
            },
            {
                "device_id": "SW-001",
                "type": "switch",
                "hostname": "corp-switch-01", 
                "management_ip": "10.0.1.10",
                "interfaces": [
                    {
                        "name": "Fa0/1",
                        "vlan": 100,
                        "status": "up",
                        "connected_devices": ["RTR-001"]
                    }
                ],
                "vlans": [
                    {"id": 100, "name": "Management", "ports": ["Fa0/1", "Fa0/2"]},
                    {"id": 200, "name": "Users", "ports": ["Fa0/3", "Fa0/4"]}
                ]
            }
        ]
    }
    
    print(f"\n🏗️  Complex Network Topology Data:")
    print(f"   Network ID: {network_topology['network_id']}")
    print(f"   Total Devices: {len(network_topology['devices'])}")
    
    print(f"\n🔍 Navigating Nested Data:")
    
    # Navigate through nested structure
    for device in network_topology['devices']:
        print(f"\n   Device: {device['hostname']} ({device['type']})")
        print(f"   Management IP: {device['management_ip']}")
        
        # Access interfaces
        if 'interfaces' in device:
            print(f"   Interfaces: {len(device['interfaces'])}")
            for interface in device['interfaces']:
                status_icon = "🟢" if interface['status'] == 'up' else "🔴"
                print(f"     {status_icon} {interface['name']}: {interface.get('ip', 'No IP')}")
        
        # Access protocols (if router)
        if device['type'] == 'router' and 'protocols' in device:
            protocols = device['protocols']
            print(f"   Protocols:")
            for protocol, config in protocols.items():
                enabled_icon = "✅" if config.get('enabled') else "❌"
                print(f"     {enabled_icon} {protocol.upper()}: {config}")
        
        # Access VLANs (if switch)
        if device['type'] == 'switch' and 'vlans' in device:
            vlans = device['vlans']
            print(f"   VLANs: {len(vlans)}")
            for vlan in vlans:
                print(f"     VLAN {vlan['id']}: {vlan['name']} ({len(vlan['ports'])} ports)")


def safe_json_access():
    """
    Demonstrate safe ways to access JSON data
    """
    print("\n" + "=" * 60)
    print("SAFE JSON DATA ACCESS")
    print("=" * 60)
    
    print("🛡️  Safe Navigation Techniques:")
    
    # Example API response that might have missing fields
    api_response = {
        "device": {
            "name": "Router-01",
            "status": "online",
            # "ip" is missing
            "interfaces": [
                {"name": "eth0", "status": "up"},
                {"name": "eth1"}  # status is missing
            ]
        }
    }
    
    print("\n1. Using .get() method with defaults:")
    
    device = api_response.get('device', {})
    print(f"   Device name: {device.get('name', 'Unknown')}")
    print(f"   Device IP: {device.get('ip', 'Not configured')}")
    print(f"   Device status: {device.get('status', 'Unknown')}")
    
    print("\n2. Safely accessing nested data:")
    
    # Unsafe way (could raise KeyError)
    # ip = api_response['device']['ip']  # Would fail!
    
    # Safe way
    device_info = api_response.get('device', {})
    device_ip = device_info.get('ip', 'Not available')
    print(f"   Safe IP access: {device_ip}")
    
    print("\n3. Handling lists safely:")
    
    interfaces = device.get('interfaces', [])
    print(f"   Found {len(interfaces)} interfaces:")
    
    for i, interface in enumerate(interfaces):
        name = interface.get('name', f'Interface{i}')
        status = interface.get('status', 'Unknown')
        print(f"     {name}: {status}")
    
    print("\n4. Using try-except for complex access:")
    
    def get_nested_value(data, keys, default=None):
        """
        Safely get nested dictionary value
        """
        try:
            value = data
            for key in keys:
                value = value[key]
            return value
        except (KeyError, TypeError):
            return default
    
    # Example usage
    first_interface_status = get_nested_value(
        api_response, 
        ['device', 'interfaces', 0, 'status'],
        'Unknown'
    )
    print(f"   First interface status: {first_interface_status}")
    
    missing_value = get_nested_value(
        api_response,
        ['device', 'nonexistent', 'field'],
        'Default value'
    )
    print(f"   Missing nested field: {missing_value}")


def json_arrays_handling():
    """
    Demonstrate working with JSON arrays
    """
    print("\n" + "=" * 60)
    print("HANDLING JSON ARRAYS")
    print("=" * 60)
    
    print("📊 Working with API responses that return arrays:")
    
    # Simulate API that returns list of devices
    devices_response = [
        {
            "id": 1,
            "hostname": "router-01.corp.com",
            "type": "router",
            "location": "Datacenter A",
            "status": "online",
            "last_seen": "2024-10-12T10:30:00Z"
        },
        {
            "id": 2, 
            "hostname": "switch-01.corp.com",
            "type": "switch",
            "location": "Datacenter A",
            "status": "online",
            "last_seen": "2024-10-12T10:29:45Z"
        },
        {
            "id": 3,
            "hostname": "firewall-01.corp.com", 
            "type": "firewall",
            "location": "DMZ",
            "status": "offline",
            "last_seen": "2024-10-12T08:15:30Z"
        }
    ]
    
    print(f"\n📋 Device Inventory ({len(devices_response)} devices):")
    
    # Process array data
    online_devices = 0
    offline_devices = 0
    
    for device in devices_response:
        status_icon = "🟢" if device['status'] == 'online' else "🔴"
        print(f"   {status_icon} {device['hostname']} ({device['type']}) - {device['location']}")
        
        if device['status'] == 'online':
            online_devices += 1
        else:
            offline_devices += 1
    
    print(f"\n📊 Summary:")
    print(f"   Online: {online_devices}")
    print(f"   Offline: {offline_devices}")
    print(f"   Total: {len(devices_response)}")
    
    print(f"\n🔍 Filtering and Searching Arrays:")
    
    # Find devices by type
    routers = [d for d in devices_response if d['type'] == 'router']
    switches = [d for d in devices_response if d['type'] == 'switch']
    
    print(f"   Routers found: {len(routers)}")
    print(f"   Switches found: {len(switches)}")
    
    # Find offline devices
    offline = [d for d in devices_response if d['status'] == 'offline']
    print(f"   Offline devices: {[d['hostname'] for d in offline]}")
    
    # Find devices in specific location
    datacenter_a = [d for d in devices_response if d['location'] == 'Datacenter A']
    print(f"   Datacenter A devices: {len(datacenter_a)}")


def error_handling_json():
    """
    Demonstrate proper JSON error handling
    """
    print("\n" + "=" * 60)
    print("JSON ERROR HANDLING")
    print("=" * 60)
    
    print("🚨 Common JSON Errors and How to Handle Them:")
    
    # Test scenarios that might cause JSON errors
    test_scenarios = [
        {
            "name": "Valid JSON",
            "url": "https://httpbin.org/json",
            "should_work": True
        },
        {
            "name": "HTML Response (not JSON)",
            "url": "https://httpbin.org/html", 
            "should_work": False
        },
        {
            "name": "Empty Response",
            "url": "https://httpbin.org/status/204",  # No content
            "should_work": False
        }
    ]
    
    for scenario in test_scenarios:
        print(f"\n🧪 Testing: {scenario['name']}")
        
        try:
            response = requests.get(scenario['url'], timeout=5)
            print(f"   Status: {response.status_code}")
            print(f"   Content-Type: {response.headers.get('content-type', 'Unknown')}")
            
            # Check if response has content
            if not response.content:
                print("   ⚠️  Response is empty")
                continue
            
            # Check if content type suggests JSON
            content_type = response.headers.get('content-type', '')
            if 'application/json' not in content_type:
                print(f"   ⚠️  Content-Type suggests non-JSON: {content_type}")
            
            # Attempt JSON conversion
            try:
                data = response.json()
                print(f"   ✅ JSON parsed successfully: {type(data)}")
                
                # Show some data if it's a dict
                if isinstance(data, dict) and data:
                    first_key = list(data.keys())[0]
                    print(f"   Sample data: {first_key} = {data[first_key]}")
                
            except ValueError as json_error:
                print(f"   ❌ JSON parsing failed: {json_error}")
                print(f"   Raw content preview: {response.text[:100]}...")
            
        except requests.RequestException as e:
            print(f"   ❌ Request failed: {e}")
    
    print(f"\n💡 JSON Error Handling Best Practices:")
    practices = [
        "Always check Content-Type header before parsing",
        "Use try-except blocks around .json() calls",
        "Provide meaningful fallbacks for JSON errors",
        "Log JSON parsing errors for debugging", 
        "Validate JSON structure after parsing",
        "Handle empty responses gracefully"
    ]
    
    for i, practice in enumerate(practices, 1):
        print(f"   {i}. {practice}")


def practical_json_examples():
    """
    Show practical network automation JSON examples
    """
    print("\n" + "=" * 60)
    print("PRACTICAL NETWORK AUTOMATION EXAMPLES")
    print("=" * 60)
    
    print("🌐 Real-world JSON processing scenarios:")
    
    # Example 1: Processing interface statistics
    def process_interface_stats(stats_json):
        """
        Process interface statistics from network device
        """
        print("\n📊 Example 1: Interface Statistics Processing")
        
        for interface_name, stats in stats_json.items():
            rx_bytes = stats.get('rx_bytes', 0)
            tx_bytes = stats.get('tx_bytes', 0)
            errors = stats.get('errors', 0)
            
            # Convert bytes to MB
            rx_mb = rx_bytes / 1024 / 1024
            tx_mb = tx_bytes / 1024 / 1024
            
            status_icon = "🟢" if errors == 0 else "🔴"
            print(f"   {status_icon} {interface_name}:")
            print(f"     RX: {rx_mb:.2f} MB")
            print(f"     TX: {tx_mb:.2f} MB") 
            print(f"     Errors: {errors}")
    
    # Sample interface data
    interface_data = {
        "GigE0/0": {"rx_bytes": 1048576000, "tx_bytes": 524288000, "errors": 0},
        "GigE0/1": {"rx_bytes": 2097152000, "tx_bytes": 1048576000, "errors": 2},
        "GigE0/2": {"rx_bytes": 0, "tx_bytes": 0, "errors": 0}
    }
    
    process_interface_stats(interface_data)
    
    # Example 2: Configuration validation
    def validate_device_config(config_json):
        """
        Validate device configuration from JSON
        """
        print("\n🔧 Example 2: Configuration Validation")
        
        required_fields = ['hostname', 'management_ip', 'interfaces']
        issues = []
        
        for field in required_fields:
            if field not in config_json:
                issues.append(f"Missing required field: {field}")
        
        # Check IP format (basic validation)
        if 'management_ip' in config_json:
            ip = config_json['management_ip']
            if not isinstance(ip, str) or ip.count('.') != 3:
                issues.append(f"Invalid IP format: {ip}")
        
        # Check interfaces
        if 'interfaces' in config_json:
            interfaces = config_json['interfaces']
            if not isinstance(interfaces, list):
                issues.append("Interfaces should be a list")
            elif len(interfaces) == 0:
                issues.append("No interfaces configured")
        
        if issues:
            print("   ❌ Configuration issues found:")
            for issue in issues:
                print(f"     • {issue}")
        else:
            print("   ✅ Configuration validation passed")
            
        return len(issues) == 0
    
    # Test configuration
    test_config = {
        "hostname": "router-01",
        "management_ip": "192.168.1.1",
        "interfaces": [
            {"name": "GigE0/0", "ip": "10.1.1.1"},
            {"name": "GigE0/1", "ip": "10.1.2.1"}
        ]
    }
    
    validate_device_config(test_config)


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - JSON CONVERSION")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    json_basics()
    basic_json_conversion()
    nested_json_handling()
    safe_json_access()
    json_arrays_handling()
    error_handling_json()
    practical_json_examples()
    
    print("\n" + "=" * 60)
    print("🎓 NEXT STEPS")
    print("=" * 60)
    print("""
Fantastic! You now understand JSON conversion and manipulation.

Key skills acquired:
✓ Converting JSON responses to Python dictionaries
✓ Navigating nested JSON structures safely
✓ Handling JSON arrays and lists
✓ Proper error handling for JSON operations
✓ Real-world network automation JSON processing

Next, you'll learn about:
• Advanced response parsing techniques
• Working with different data formats (XML, CSV)
• Data transformation and filtering

Continue to: examples/06_parsing_responses.py
    """)


if __name__ == "__main__":
    main()