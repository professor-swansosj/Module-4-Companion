"""
Module 05: Robust API Calls - Professional Error Handling
TODO: Add error handling to make your API calls bulletproof

Your mission:
1. Add try/except blocks to handle API failures
2. Check status codes before processing responses
3. Handle JSON parsing errors
4. Create user-friendly error messages
5. Test with both working and broken API calls

Hint: Professional code assumes things will go wrong and handles it gracefully!
"""

import requests
import json

def safe_dad_joke():
    """
    TODO: Get a dad joke with full error handling
    
    Steps to complete:
    1. TODO: Wrap API call in try/except block
    2. TODO: Check response status code
    3. TODO: Handle JSON parsing errors
    4. TODO: Provide user-friendly error messages
    5. TODO: Return success/failure status
    
    Hint: Use requests.exceptions.RequestException to catch network errors
    """
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    
    try:
        print("🔄 Attempting to fetch dad joke...")
        
        # TODO: Make API request with error handling
        # response = requests.get(url, headers=headers)
        
        # TODO: Check status code
        # if response.status_code == 200:
        #     # TODO: Try to parse JSON
        #     data = response.json()
        #     joke = data['joke']
        #     print(f"✅ Success! Here's your joke:")
        #     print(f"   {joke}")
        #     return True
        # else:
        #     print(f"❌ API returned status code: {response.status_code}")
        #     return False
        
        print("TODO: Implement the API call with error handling!")
        return False
        
    except requests.exceptions.ConnectionError:
        print("❌ Network connection failed. Check your internet!")
        return False
    except requests.exceptions.Timeout:
        print("❌ Request timed out. Try again later.")
        return False
    except json.JSONDecodeError:
        print("❌ Received invalid JSON from API")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def safe_deck_creation():
    """
    TODO: Create deck with comprehensive error handling
    
    Steps to complete:
    1. TODO: Add try/except for deck creation
    2. TODO: Validate response has required fields
    3. TODO: Handle missing deck_id gracefully  
    4. TODO: Return deck_id or None based on success
    
    🎮 Try This: Test with a bad URL to see your error handling work!
    """
    url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
    
    try:
        print("🔄 Creating new shuffled deck...")
        
        # TODO: Make API request
        # response = requests.get(url)
        
        # TODO: Check response status
        # response.raise_for_status()  # Raises exception for 4xx/5xx status codes
        
        # TODO: Parse JSON
        # data = response.json()
        
        # TODO: Validate response has required fields
        # if 'deck_id' in data and data['success']:
        #     deck_id = data['deck_id']
        #     print(f"✅ Deck created successfully! ID: {deck_id}")
        #     return deck_id
        # else:
        #     print("❌ API response missing required fields")
        #     return None
            
        print("TODO: Implement safe deck creation!")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error creating deck: {e}")
        return None
    except json.JSONDecodeError:
        print("❌ Invalid JSON response from deck API")
        return None
    except KeyError as e:
        print(f"❌ Missing expected field in response: {e}")
        return None

def test_error_scenarios():
    """
    TODO: Test your error handling with broken URLs
    
    This function tests how your code handles various failure scenarios.
    Use it to verify your error handling works!
    """
    print("\n🧪 TESTING ERROR SCENARIOS")
    print("=" * 40)
    
    # Test with broken URL
    broken_url = "https://this-api-does-not-exist.com/"
    
    print("\nTesting with broken URL...")
    try:
        # TODO: Try making request to broken URL
        # response = requests.get(broken_url, timeout=5)
        print("TODO: Test with broken URL to see error handling")
    except requests.exceptions.RequestException as e:
        print(f"✅ Correctly caught error: {type(e).__name__}")
    
    print("\n🎯 Your error handling is being tested!")

def main():
    """
    TODO: Test all your robust API functions
    """
    print("🛡️ Testing Robust API Calls!")
    print("=" * 40)
    
    # TODO: Test safe dad joke function
    print("\n1. Testing Safe Dad Joke:")
    # success = safe_dad_joke()
    
    print("\n2. Testing Safe Deck Creation:")
    # deck_id = safe_deck_creation()
    
    print("\n3. Testing Error Scenarios:")
    # test_error_scenarios()
    
    print("\n✨ You're building professional-grade error handling!")

if __name__ == "__main__":
    main()