"""
Module 03: Joke Extractor - Mining Gold from Dad Jokes API
TODO: Extract specific data from API responses and use it creatively

Your mission:
1. Get dad jokes from the API
2. Extract just the joke text (not all the extra data)
3. Create custom formatted messages with the joke
4. Build a professional joke presentation system!

Hint: The API returns a dictionary - dig into it and pull out the good stuff!
"""

import requests

def extract_and_format_joke():
    """
    TODO: Extract joke text and create beautiful formatted output
    
    Steps to complete:
    1. TODO: Make API call to get dad joke
    2. TODO: Convert response to dictionary
    3. TODO: Extract just the joke text from the dictionary
    4. TODO: Create a formatted message with the joke
    5. TODO: Add some creative presentation elements!
    
    Hint: Look for a field called 'joke' in the API response dictionary
    """
    print("🎭 Fetching a premium dad joke...")
    
    # TODO: Your API call here
    
    # TODO: Convert to dictionary
    
    # TODO: Extract the joke text
    # joke_text = data['???']  # What field contains the joke?
    
    # TODO: Create formatted output
    print("\n" + "="*60)
    print("🎪 DAD JOKE OF THE DAY 🎪")
    print("="*60)
    # TODO: Display the joke nicely
    # print(f"   {joke_text}")
    print("="*60)
    print("😂 Hope that made you smile! 😂")

def get_multiple_jokes(count=3):
    """
    TODO: Get multiple jokes and present them as a collection
    
    Steps to complete:
    1. TODO: Create a loop to get multiple jokes
    2. TODO: Extract joke text from each response  
    3. TODO: Store jokes in a list
    4. TODO: Present them in a numbered format
    
    🎮 Try This: Make this function work after you finish the one above!
    """
    print(f"\n🎪 Getting {count} dad jokes for you...")
    
    jokes = []
    
    # TODO: Loop to get multiple jokes
    for i in range(count):
        # TODO: Make API call
        # TODO: Extract joke text
        # TODO: Add to jokes list
        pass
    
    # TODO: Display all jokes in a nice format
    print("\n🎭 YOUR DAD JOKE COLLECTION:")
    print("-" * 50)
    
    # TODO: Loop through jokes and display with numbers
    # for i, joke in enumerate(jokes, 1):
    #     print(f"{i}. {joke}")
    #     print()

def main():
    """
    TODO: Run your joke extraction functions
    """
    print("🎨 Dad Joke Data Mining Operation!")
    print("=" * 50)
    
    # TODO: Extract and format a single joke
    # extract_and_format_joke()
    
    # TODO: Try getting multiple jokes (uncomment when ready)
    # get_multiple_jokes(3)
    
    print("\n✨ You're extracting API data like a pro!")

if __name__ == "__main__":
    main()