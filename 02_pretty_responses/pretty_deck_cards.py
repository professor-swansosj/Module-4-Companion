"""
Module 02: Pretty Deck of Cards - Understanding API Data Structure  
TODO: Explore the structure of the Deck of Cards API responses

Your mission:
1. Create a new deck and examine its data structure
2. Pretty print the response to understand what data is available  
3. Draw some cards and see that data structure too
4. Learn to navigate JSON data like a pro!

Hint: The Deck of Cards API returns rich data - deck_id, remaining cards, success status, etc.
"""

import requests
import json

def create_and_explore_deck():
    """
    TODO: Create a deck and explore its data structure
    
    Steps to complete:
    1. TODO: Make API call to create new deck
    2. TODO: Convert response to dictionary  
    3. TODO: Pretty print the structure to see what's available
    4. TODO: Extract and display key information (deck_id, remaining cards, etc.)
    
    Hint: Look for deck_id in the response - you'll need it to draw cards!
    """
    print("🃏 Creating a new deck...")
    
    # TODO: API call to create new deck (https://deckofcardsapi.com/api/deck/new/)
    
    # TODO: Convert to dictionary
    
    # TODO: Pretty print the structure
    print("📋 New Deck Data Structure:")
    # print(json.dumps(your_data, indent=4))
    
    # TODO: Extract key info
    print("\n🔍 Key Information:")
    # print(f"   Deck ID: {deck_id}")
    # print(f"   Cards Remaining: {remaining}")
    # print(f"   Success: {success}")
    
    return None  # TODO: Return the deck_id for use in drawing cards

def draw_and_explore_cards(deck_id, count=2):
    """
    TODO: Draw cards and explore that data structure too
    
    This function shows you there's always more to learn from APIs!
    For now, just get the deck creation working above.
    """
    if deck_id:
        print(f"\n🎴 Drawing {count} cards from deck {deck_id}...")
        # TODO: Implement in next module
    else:
        print("⚠️ Need a deck_id first - complete the create_and_explore_deck function!")

def main():
    """
    TODO: Explore the API data structures
    """
    print("🎨 Exploring Deck of Cards API Data!")
    print("="*50)
    
    # TODO: Create deck and get deck_id
    deck_id = None  # TODO: Get this from create_and_explore_deck()
    
    # TODO: Try drawing cards (we'll implement this fully later)
    draw_and_explore_cards(deck_id, 3)
    
    print("\n✨ You're learning to read API data like a pro!")

if __name__ == "__main__":
    main()