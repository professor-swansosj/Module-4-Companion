"""
Module 02: Pretty Dad Jokes - Making API Data Beautiful
TODO: Convert raw API responses to formatted, readable output

Your mission:
1. Take your working Dad Jokes code from Module 01
2. Convert the response to a Python dictionary
3. Pretty print the JSON structure
4. Display the joke in a nice, formatted way

Hint: response.json() converts API text to a Python dictionary!
"""

import requests
import json

def get_pretty_dad_joke():
    """
    TODO: Get a dad joke and display it beautifully
    
    Steps to complete:
    1. TODO: Make your API call to get a dad joke (copy from Module 01)
    2. TODO: Convert response to dictionary using response.json()
    3. TODO: Pretty print the full JSON structure with json.dumps(data, indent=4)
    4. TODO: Extract just the joke text and display it nicely
    
    Hint: The Dad Jokes API probably returns something like {'joke': 'Why did...'}
    """
    print("📡 Calling Dad Jokes API...")
    
    # TODO: Your API call here (from Module 01)
    
    # TODO: Convert to dictionary with response.json()
    
    # TODO: Pretty print the full structure 
    print("📋 Raw API Response Structure:")
    # print(json.dumps(your_data_variable, indent=4))
    
    # TODO: Extract and display just the joke nicely
    print("\n🎭 Your Dad Joke:")
    # print(f"   {your_joke_text}")
    
def main():
    """
    TODO: Run your pretty joke function
    """
    print("🎨 Making Dad Jokes Beautiful!")
    print("="*50)
    
    # TODO: Call get_pretty_dad_joke()
    
    print("\n✨ Now that's a professionally formatted API response!")

if __name__ == "__main__":
    main()