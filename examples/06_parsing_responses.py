#!/usr/bin/env python3
"""
Module 4: Advanced Response Parsing Techniques
=============================================

This file demonstrates advanced parsing techniques for different
data formats and complex response processing scenarios.

Learning Objectives:
- Parse different data formats (XML, CSV, YAML)
- Advanced JSON manipulation and filtering
- Data transformation and extraction techniques
- Handle mixed and complex response formats

Author: FSCJ - Software Defined Networking Course
"""

import requests
import json
import csv
import io
import re
from xml.etree import ElementTree as ET


def advanced_json_parsing():
    """
    Advanced JSON parsing and manipulation techniques
    """
    print("=" * 60)
    print("ADVANCED JSON PARSING")
    print("=" * 60)
    
    # Simulate complex API response
    complex_response = {
        "metadata": {
            "timestamp": "2024-10-12T10:30:00Z",
            "total_devices": 5,
            "query_time_ms": 45
        },
        "devices": [
            {
                "id": "dev-001",
                "hostname": "router-dc1-01.corp.com", 
                "type": "router",
                "vendor": "Cisco",
                "model": "ISR4451",
                "location": {"building": "DC1", "rack": "R01", "unit": 1},
                "management": {
                    "ip": "10.1.1.1",
                    "protocols": ["SSH", "HTTPS", "SNMP"],
                    "credentials": {"username": "admin", "auth_method": "key"}
                },
                "interfaces": [
                    {
                        "name": "GigE0/0/0",
                        "type": "physical",
                        "status": "up",
                        "ip_config": {"ip": "192.168.1.1", "netmask": "255.255.255.0"},
                        "statistics": {"rx_packets": 1500000, "tx_packets": 1400000, "errors": 0}
                    },
                    {
                        "name": "GigE0/0/1", 
                        "type": "physical",
                        "status": "down",
                        "ip_config": None,
                        "statistics": {"rx_packets": 0, "tx_packets": 0, "errors": 5}
                    }
                ],
                "routing": {
                    "protocols": ["OSPF", "BGP"],
                    "routes": [
                        {"network": "10.0.0.0/8", "next_hop": "192.168.1.254", "metric": 1},
                        {"network": "172.16.0.0/12", "next_hop": "192.168.1.254", "metric": 10}
                    ]
                }
            }
        ]
    }
    
    print("🔍 Complex JSON Data Extraction:")
    
    # Extract metadata
    metadata = complex_response.get('metadata', {})
    print(f"Query executed at: {metadata.get('timestamp')}")
    print(f"Query time: {metadata.get('query_time_ms')}ms")
    print(f"Total devices: {metadata.get('total_devices')}")
    
    # Process devices
    devices = complex_response.get('devices', [])
    for device in devices:
        print(f"\n📱 Device: {device.get('hostname')}")
        print(f"   Type: {device.get('vendor')} {device.get('model')} ({device.get('type')})")
        
        # Location information
        location = device.get('location', {})
        print(f"   Location: {location.get('building')} - Rack {location.get('rack')}")
        
        # Management info
        mgmt = device.get('management', {})
        protocols = mgmt.get('protocols', [])
        print(f"   Management IP: {mgmt.get('ip')}")
        print(f"   Protocols: {', '.join(protocols)}")
        
        # Interface analysis
        interfaces = device.get('interfaces', [])
        up_interfaces = [iface for iface in interfaces if iface.get('status') == 'up']
        down_interfaces = [iface for iface in interfaces if iface.get('status') == 'down']
        
        print(f"   Interfaces: {len(up_interfaces)} up, {len(down_interfaces)} down")
        
        for iface in interfaces:
            status_icon = "🟢" if iface.get('status') == 'up' else "🔴"
            ip_config = iface.get('ip_config')
            ip_info = f"{ip_config['ip']}" if ip_config else "No IP"
            errors = iface.get('statistics', {}).get('errors', 0)
            error_info = f" ({errors} errors)" if errors > 0 else ""
            
            print(f"     {status_icon} {iface.get('name')}: {ip_info}{error_info}")


def json_filtering_and_transformation():
    """
    Demonstrate JSON data filtering and transformation
    """
    print("\n" + "=" * 60)
    print("JSON FILTERING AND TRANSFORMATION")
    print("=" * 60)
    
    # Sample network monitoring data
    monitoring_data = {
        "timestamp": "2024-10-12T10:30:00Z",
        "alerts": [
            {"id": "ALT-001", "severity": "critical", "type": "interface_down", "device": "router-01", "message": "Interface GigE0/1 is down"},
            {"id": "ALT-002", "severity": "warning", "type": "high_cpu", "device": "switch-01", "message": "CPU usage at 85%"},
            {"id": "ALT-003", "severity": "info", "type": "backup_complete", "device": "router-02", "message": "Configuration backup completed"},
            {"id": "ALT-004", "severity": "critical", "type": "power_failure", "device": "ups-01", "message": "Primary power source failed"},
            {"id": "ALT-005", "severity": "warning", "type": "high_memory", "device": "router-01", "message": "Memory usage at 90%"}
        ]
    }
    
    print("🚨 Alert Filtering Examples:")
    
    alerts = monitoring_data.get('alerts', [])
    
    # Filter by severity
    critical_alerts = [alert for alert in alerts if alert['severity'] == 'critical']
    warning_alerts = [alert for alert in alerts if alert['severity'] == 'warning'] 
    
    print(f"\n📊 Alert Summary:")
    print(f"   Critical: {len(critical_alerts)}")
    print(f"   Warning: {len(warning_alerts)}")
    print(f"   Total: {len(alerts)}")
    
    print(f"\n🔥 Critical Alerts:")
    for alert in critical_alerts:
        print(f"   • {alert['device']}: {alert['message']}")
    
    # Filter by device
    router_01_alerts = [alert for alert in alerts if alert['device'] == 'router-01']
    print(f"\n🔍 Alerts for router-01 ({len(router_01_alerts)}):")
    for alert in router_01_alerts:
        severity_icon = "🔥" if alert['severity'] == 'critical' else "⚠️" if alert['severity'] == 'warning' else "ℹ️"
        print(f"   {severity_icon} {alert['type']}: {alert['message']}")
    
    # Transform data - create summary by device
    device_summary = {}
    for alert in alerts:
        device = alert['device']
        if device not in device_summary:
            device_summary[device] = {'critical': 0, 'warning': 0, 'info': 0}
        device_summary[device][alert['severity']] += 1
    
    print(f"\n📈 Alert Summary by Device:")
    for device, counts in device_summary.items():
        total = sum(counts.values())
        print(f"   {device}: {total} total (🔥{counts['critical']} ⚠️{counts['warning']} ℹ️{counts['info']})")


def xml_parsing():
    """
    Demonstrate XML response parsing
    """
    print("\n" + "=" * 60)
    print("XML RESPONSE PARSING")
    print("=" * 60)
    
    print("📄 XML is common in network device APIs and configuration files")
    
    # Sample XML response (simulating network device configuration)
    xml_response = """<?xml version="1.0" encoding="UTF-8"?>
    <network_config>
        <device id="RTR-001" type="router">
            <hostname>corp-router-01</hostname>
            <management_ip>10.1.1.1</management_ip>
            <interfaces>
                <interface name="GigE0/0">
                    <ip_address>192.168.1.1</ip_address>
                    <netmask>255.255.255.0</netmask>
                    <status>up</status>
                    <description>LAN Interface</description>
                </interface>
                <interface name="GigE0/1">
                    <ip_address>10.10.1.1</ip_address>
                    <netmask>255.255.255.0</netmask>
                    <status>down</status>
                    <description>WAN Interface</description>
                </interface>
            </interfaces>
            <routing>
                <protocol name="OSPF">
                    <area>0.0.0.0</area>
                    <enabled>true</enabled>
                </protocol>
                <static_routes>
                    <route network="0.0.0.0" netmask="0.0.0.0" gateway="10.10.1.254"/>
                </static_routes>
            </routing>
        </device>
    </network_config>"""
    
    print("🔧 Parsing XML Configuration:")
    
    try:
        # Parse XML
        root = ET.fromstring(xml_response)
        
        # Extract device information
        device = root.find('device')
        device_id = device.get('id')
        device_type = device.get('type')
        hostname = device.find('hostname').text
        mgmt_ip = device.find('management_ip').text
        
        print(f"   Device ID: {device_id}")
        print(f"   Type: {device_type}")
        print(f"   Hostname: {hostname}")
        print(f"   Management IP: {mgmt_ip}")
        
        # Parse interfaces
        interfaces = device.find('interfaces')
        print(f"\n   Interfaces:")
        
        for interface in interfaces.findall('interface'):
            name = interface.get('name')
            ip = interface.find('ip_address').text
            status = interface.find('status').text
            description = interface.find('description').text
            
            status_icon = "🟢" if status == 'up' else "🔴"
            print(f"     {status_icon} {name}: {ip} ({description})")
        
        # Parse routing information
        routing = device.find('routing')
        ospf = routing.find('protocol[@name="OSPF"]')
        if ospf is not None:
            area = ospf.find('area').text
            enabled = ospf.find('enabled').text == 'true'
            print(f"\n   OSPF: {'Enabled' if enabled else 'Disabled'} (Area {area})")
        
        # Parse static routes
        static_routes = routing.find('static_routes')
        if static_routes is not None:
            routes = static_routes.findall('route')
            print(f"   Static Routes: {len(routes)}")
            for route in routes:
                network = route.get('network')
                gateway = route.get('gateway')
                print(f"     Default route via {gateway}")
    
    except ET.ParseError as e:
        print(f"   ❌ XML parsing error: {e}")
    except Exception as e:
        print(f"   ❌ Error processing XML: {e}")


def csv_parsing():
    """
    Demonstrate CSV response parsing
    """
    print("\n" + "=" * 60)
    print("CSV RESPONSE PARSING")
    print("=" * 60)
    
    print("📊 CSV is common for bulk data exports and reports")
    
    # Sample CSV data (network device inventory)
    csv_data = """hostname,ip_address,device_type,location,status,last_seen
router-01.corp.com,10.1.1.1,router,Datacenter_A,online,2024-10-12 10:15:00
switch-01.corp.com,10.1.1.10,switch,Datacenter_A,online,2024-10-12 10:14:30
firewall-01.corp.com,10.1.1.100,firewall,DMZ,online,2024-10-12 10:13:45
router-02.corp.com,10.1.2.1,router,Datacenter_B,offline,2024-10-12 08:30:00
switch-02.corp.com,10.1.2.10,switch,Datacenter_B,maintenance,2024-10-12 07:00:00"""
    
    print("🗂️  Processing Device Inventory CSV:")
    
    try:
        # Parse CSV data
        csv_file = io.StringIO(csv_data)
        reader = csv.DictReader(csv_file)
        
        devices = list(reader)
        
        print(f"   Total devices: {len(devices)}")
        
        # Analyze device status
        status_counts = {}
        type_counts = {}
        location_counts = {}
        
        for device in devices:
            # Count by status
            status = device['status']
            status_counts[status] = status_counts.get(status, 0) + 1
            
            # Count by type
            device_type = device['device_type']
            type_counts[device_type] = type_counts.get(device_type, 0) + 1
            
            # Count by location
            location = device['location']
            location_counts[location] = location_counts.get(location, 0) + 1
        
        print(f"\n   📊 Status Distribution:")
        for status, count in status_counts.items():
            status_icon = "🟢" if status == 'online' else "🔴" if status == 'offline' else "🔧"
            print(f"     {status_icon} {status}: {count}")
        
        print(f"\n   🏷️  Device Types:")
        for device_type, count in type_counts.items():
            print(f"     {device_type}: {count}")
        
        print(f"\n   🏢 Locations:")
        for location, count in location_counts.items():
            print(f"     {location}: {count}")
        
        # Show devices needing attention
        offline_devices = [d for d in devices if d['status'] in ['offline', 'maintenance']]
        if offline_devices:
            print(f"\n   ⚠️  Devices Needing Attention ({len(offline_devices)}):")
            for device in offline_devices:
                print(f"     • {device['hostname']} ({device['status']}) - Last seen: {device['last_seen']}")
    
    except Exception as e:
        print(f"   ❌ Error processing CSV: {e}")


def mixed_content_parsing():
    """
    Handle responses with mixed or unknown content types
    """
    print("\n" + "=" * 60)
    print("MIXED CONTENT TYPE HANDLING")
    print("=" * 60)
    
    print("🎭 Real APIs sometimes return unexpected content types")
    
    def smart_content_parser(response_text, content_type_header):
        """
        Intelligently parse content based on type and content
        """
        print(f"\n🔍 Parsing content (Content-Type: {content_type_header}):")
        
        # Try to determine actual content type
        if content_type_header and 'json' in content_type_header.lower():
            try:
                data = json.loads(response_text)
                print("   ✅ Successfully parsed as JSON")
                return {'type': 'json', 'data': data}
            except ValueError:
                print("   ⚠️  Content-Type says JSON but parsing failed")
        
        # Check if it looks like XML
        if response_text.strip().startswith('<?xml') or response_text.strip().startswith('<'):
            try:
                root = ET.fromstring(response_text)
                print("   ✅ Successfully parsed as XML")
                return {'type': 'xml', 'data': root}
            except ET.ParseError:
                print("   ⚠️  Looks like XML but parsing failed")
        
        # Check if it looks like CSV
        if ',' in response_text and '\n' in response_text:
            try:
                lines = response_text.strip().split('\n')
                if len(lines) > 1 and ',' in lines[0]:
                    csv_file = io.StringIO(response_text)
                    reader = csv.DictReader(csv_file)
                    data = list(reader)
                    print("   ✅ Successfully parsed as CSV")
                    return {'type': 'csv', 'data': data}
            except Exception:
                pass
        
        # Check if it's JSON without proper Content-Type
        try:
            data = json.loads(response_text)
            print("   ✅ Found JSON despite incorrect Content-Type")
            return {'type': 'json', 'data': data}
        except ValueError:
            pass
        
        # Fall back to plain text
        print("   📄 Treating as plain text")
        return {'type': 'text', 'data': response_text}
    
    # Test different content scenarios
    test_scenarios = [
        {
            "name": "JSON with correct Content-Type",
            "content": '{"status": "ok", "message": "Device online"}',
            "content_type": "application/json"
        },
        {
            "name": "JSON with wrong Content-Type", 
            "content": '{"error": "Authentication failed"}',
            "content_type": "text/plain"
        },
        {
            "name": "XML response",
            "content": '<?xml version="1.0"?><status>ok</status>',
            "content_type": "application/xml"
        },
        {
            "name": "CSV response",
            "content": "name,status\nrouter-01,online\nswitch-01,offline",
            "content_type": "text/csv"
        },
        {
            "name": "Plain text response",
            "content": "System status: All services running normally",
            "content_type": "text/plain"
        }
    ]
    
    for scenario in test_scenarios:
        print(f"\n🧪 Test: {scenario['name']}")
        result = smart_content_parser(scenario['content'], scenario['content_type'])
        print(f"   Detected type: {result['type']}")
        
        if result['type'] == 'json' and isinstance(result['data'], dict):
            print(f"   Keys: {list(result['data'].keys())}")
        elif result['type'] == 'csv' and isinstance(result['data'], list):
            print(f"   Rows: {len(result['data'])}")
        elif result['type'] == 'xml':
            print(f"   Root element: {result['data'].tag}")
        else:
            preview = str(result['data'])[:50]
            print(f"   Content preview: {preview}...")


def response_validation():
    """
    Demonstrate response validation techniques
    """
    print("\n" + "=" * 60)
    print("RESPONSE VALIDATION")
    print("=" * 60)
    
    print("🛡️  Validating API responses for data integrity:")
    
    def validate_device_response(response_data):
        """
        Validate a device API response
        """
        errors = []
        warnings = []
        
        # Required fields check
        required_fields = ['device_id', 'hostname', 'status', 'type']
        for field in required_fields:
            if field not in response_data:
                errors.append(f"Missing required field: {field}")
        
        # Data type validation
        if 'device_id' in response_data:
            if not isinstance(response_data['device_id'], str):
                errors.append("device_id must be a string")
        
        if 'hostname' in response_data:
            hostname = response_data['hostname']
            if not isinstance(hostname, str) or len(hostname) == 0:
                errors.append("hostname must be a non-empty string")
            elif not re.match(r'^[a-zA-Z0-9.-]+$', hostname):
                warnings.append("hostname contains unusual characters")
        
        # Status validation
        if 'status' in response_data:
            valid_statuses = ['online', 'offline', 'maintenance', 'unknown']
            if response_data['status'] not in valid_statuses:
                errors.append(f"Invalid status: {response_data['status']}")
        
        # IP address validation (if present)
        if 'management_ip' in response_data:
            ip = response_data['management_ip']
            ip_pattern = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
            if not re.match(ip_pattern, ip):
                errors.append(f"Invalid IP address format: {ip}")
        
        return errors, warnings
    
    # Test validation with different responses
    test_responses = [
        {
            "name": "Valid response",
            "data": {
                "device_id": "RTR-001",
                "hostname": "router-01.corp.com",
                "status": "online",
                "type": "router",
                "management_ip": "10.1.1.1"
            }
        },
        {
            "name": "Missing fields", 
            "data": {
                "device_id": "SW-001",
                "hostname": "switch-01"
                # Missing status and type
            }
        },
        {
            "name": "Invalid data types",
            "data": {
                "device_id": 123,  # Should be string
                "hostname": "",    # Empty string
                "status": "active", # Invalid status
                "type": "switch",
                "management_ip": "300.1.1.1"  # Invalid IP
            }
        }
    ]
    
    for test in test_responses:
        print(f"\n🧪 Validating: {test['name']}")
        errors, warnings = validate_device_response(test['data'])
        
        if not errors and not warnings:
            print("   ✅ Validation passed")
        else:
            if errors:
                print("   ❌ Validation errors:")
                for error in errors:
                    print(f"     • {error}")
            if warnings:
                print("   ⚠️  Warnings:")
                for warning in warnings:
                    print(f"     • {warning}")


def main():
    """
    Main function to run all examples
    """
    print("🐍 PYTHON REQUESTS LIBRARY - PARSING RESPONSES")
    print("Software Defined Networking - Module 4")
    print("FSCJ Computer Science Department")
    
    # Run all sections
    advanced_json_parsing()
    json_filtering_and_transformation()
    xml_parsing()
    csv_parsing() 
    mixed_content_parsing()
    response_validation()
    
    print("\n" + "=" * 60)
    print("🎓 CONGRATULATIONS!")
    print("=" * 60)
    print("""
Outstanding work! You've completed all the core examples for Module 4.

Skills mastered:
✓ Advanced JSON parsing and manipulation
✓ Data filtering and transformation
✓ XML parsing for network configurations
✓ CSV data processing
✓ Mixed content type handling
✓ Response validation techniques

🎮 NEXT CHALLENGE:
Now you're ready for the main lab project - the War Card Game!
This will combine ALL the skills you've learned in a fun, practical application.

Continue to: labs/war_card_game/war_game.py

The War Card Game will demonstrate:
• Real API integration (Deck of Cards API)
• JSON response handling
• Game state management
• Error handling and retry logic
• User interface design
• Object-oriented programming

Good luck with the lab! 🚀
    """)


if __name__ == "__main__":
    main()