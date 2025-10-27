"""
Module 01: From Postman to Python - Deck of Cards API
TODO: Export and run your Deck of Cards API request

Your mission: 
1. Export Python code from your Deck of Cards request in Postman  
2. Paste it below and make it work
3. See how easy it is to get API data programmatically!

Hint: The Deck of Cards API gives you JSON data about card decks - perfect for learning!
"""

import requests

def get_new_deck():
    """
    TODO: Create a new deck of cards using the API
    
    Steps to complete:
    1. TODO: Use your exported Postman code to make the API call
    2. TODO: The API endpoint is probably something like 'https://deckofcardsapi.com/api/deck/new/'
    3. TODO: Store the response and print it out
    
    Hint: Start simple - just get the response and print response.text
    """
    # TODO: Your Postman-exported code goes here
    pass

def draw_cards(deck_id, count=2):
    """
    TODO: Draw cards from your deck (we'll build on this later!)
    
    For now, just focus on getting the new deck working above.
    This function is here to show you what's coming next!
    """
    # We'll implement this in the next module
    print(f"Coming soon: Draw {count} cards from deck {deck_id}!")

def main():
    """
    TODO: Create your first deck and celebrate!
    """
    print("🃏 Creating a new deck of cards...")
    
    # TODO: Call get_new_deck() here
    
    print("🎉 Perfect! You're ready to work with card data programmatically!")

if __name__ == "__main__":
    main()