"""
Module 01: From Postman to Python - Dad Jokes API
TODO: Take your Postman-exported code and make it work in Python

Your mission: 
1. Export Python code from your working Dad Jokes request in Postman
2. Paste it below and modify as needed
3. Run it and see your first programmatic API call!

Hint: Look for 'requests.get()' in the exported code - that's the magic!
"""

import requests

def get_dad_joke():
    """
    TODO: Paste your exported Postman code here and make it work
    
    Steps to complete:
    1. TODO: Replace this comment with your Postman-exported requests.get() call
    2. TODO: Store the response in a variable (maybe call it 'response')  
    3. TODO: Print the response text to see your joke
    
    Hint: The basic pattern is:
    response = requests.get('your-api-url-here')
    print(response.text)
    """
    # TODO: Your Postman-exported code goes here
    pass

def main():
    """
    TODO: Call your get_dad_joke function and see the magic happen!
    """
    print("🎭 Getting a dad joke from the API...")
    
    # TODO: Call get_dad_joke() here
    
    print("✨ You just made your first API call with Python!")

if __name__ == "__main__":
    main()