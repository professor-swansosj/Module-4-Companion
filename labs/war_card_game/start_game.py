#!/usr/bin/env python3
"""
War Card Game - Easy Launcher Script
====================================

This script provides an easy way to start the War Card Game
with environment checking and setup assistance.

Usage:
    python start_game.py

For Students:
    This launcher script helps ensure you have everything set up
    correctly before starting the main game.
"""

import sys
import os
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    
    print(f"🐍 Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Error: This game requires Python 3.7 or higher")
        print("   Please upgrade your Python installation")
        return False
    else:
        print("✅ Python version is compatible")
        return True


def check_required_modules():
    """Check if required modules are available"""
    print("\n🔍 Checking required modules...")
    
    required_modules = ['requests', 'json', 'datetime', 'typing']
    missing_modules = []
    
    for module in required_modules:
        try:
            if module == 'requests':
                import requests
                print(f"✅ {module} - version {requests.__version__}")
            elif module == 'json':
                import json
                print(f"✅ {module} - built-in module")
            elif module == 'datetime':
                import datetime
                print(f"✅ {module} - built-in module")
            elif module == 'typing':
                import typing
                print(f"✅ {module} - built-in module")
        except ImportError:
            print(f"❌ {module} - not installed")
            missing_modules.append(module)
    
    if missing_modules:
        print(f"\n📦 Missing modules: {', '.join(missing_modules)}")
        print("To install missing modules, run:")
        print("   pip install requests")
        print("Or:")
        print("   pip install -r requirements.txt")
        return False
    else:
        print("✅ All required modules are available")
        return True


def check_internet_connection():
    """Test internet connection to the Deck of Cards API"""
    print("\n🌐 Testing internet connection...")
    
    try:
        import requests
        
        # Test with a simple request to the API
        response = requests.get(
            "https://deckofcardsapi.com/api/deck/new/",
            timeout=5
        )
        
        if response.status_code == 200:
            print("✅ Internet connection works")
            print("✅ Deck of Cards API is accessible")
            return True
        else:
            print(f"⚠️  API returned status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ No internet connection detected")
        print("   This game requires internet to access the Deck of Cards API")
        return False
    except requests.exceptions.Timeout:
        print("⚠️  Connection timeout - internet may be slow")
        return False
    except Exception as e:
        print(f"❌ Connection test failed: {e}")
        return False


def show_game_info():
    """Display game information"""
    print("\n" + "=" * 60)
    print("🎮 WAR CARD GAME - Module 4 Lab Project")
    print("FSCJ - Software Defined Networking Course")
    print("=" * 60)
    print("Learning Objectives:")
    print("• Practice making HTTP requests with Python")
    print("• Handle JSON responses from APIs")
    print("• Implement error handling and retry logic")
    print("• Manage application state and user interaction")
    print("• Create a complete Python application")
    print()
    print("Game Features:")
    print("• Full War card game implementation")
    print("• Real-time API integration")
    print("• Statistics tracking")
    print("• User-friendly interface")
    print("• Comprehensive error handling")
    print("=" * 60)


def get_user_permission():
    """Ask user if they want to start the game"""
    while True:
        choice = input("\n🚀 Start the War Card Game? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no")


def start_game():
    """Launch the main game"""
    try:
        print("\n🎮 Starting War Card Game...")
        print("-" * 30)
        
        # Import and run the main game
        from war_game import main
        main()
        
    except ImportError as e:
        print(f"❌ Error importing game module: {e}")
        print("Make sure all game files are in the same directory")
        return False
    except Exception as e:
        print(f"❌ Error starting game: {e}")
        return False
    
    return True


def main():
    """Main launcher function"""
    print("🎯 War Card Game Launcher")
    print("=" * 30)
    
    # Check system requirements
    if not check_python_version():
        input("Press Enter to exit...")
        return
    
    if not check_required_modules():
        input("Press Enter to exit...")
        return
    
    if not check_internet_connection():
        print("\n⚠️  Warning: Internet connection issues detected")
        print("The game may not work properly without internet access")
        
        continue_anyway = input("Continue anyway? (y/n): ").lower().strip()
        if continue_anyway not in ['y', 'yes']:
            print("👋 Exiting launcher")
            return
    
    # Show game info
    show_game_info()
    
    # Get permission to start
    if not get_user_permission():
        print("👋 Maybe next time! Good luck with your studies.")
        return
    
    # Launch the game
    if start_game():
        print("\n🎊 Thanks for playing! You've completed the Module 4 lab.")
    else:
        print("\n❌ Game ended with errors. Check the error messages above.")
    
    input("Press Enter to exit...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Launcher interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected launcher error: {e}")
        input("Press Enter to exit...")