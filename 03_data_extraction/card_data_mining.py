"""
Module 03: Card Data Mining - Extracting Gold from Deck API
TODO: Navigate complex API data structures and extract specific information

Your mission:
1. Create a deck and extract its ID and metadata
2. Draw cards and extract card details (value, suit, code)
3. Create formatted card descriptions
4. Build a card information system!

Hint: Card data has nested structures - each card has value, suit, code, etc.
"""

import requests
import json

def create_deck_and_extract_info():
    """
    TODO: Create deck and extract key information
    
    Steps to complete:
    1. TODO: Create new deck via API
    2. TODO: Extract deck_id, remaining cards, shuffled status
    3. TODO: Create formatted deck information display
    4. TODO: Return deck_id for drawing cards
    
    Hint: Look for 'deck_id', 'remaining', 'shuffled' in the response
    """
    print("🃏 Creating and analyzing a new deck...")
    
    # TODO: API call to create new deck
    
    # TODO: Extract key information
    # deck_id = data['???']
    # remaining = data['???'] 
    # shuffled = data['???']
    
    # TODO: Display formatted deck info
    print("\n📊 DECK INFORMATION")
    print("-" * 40)
    # print(f"Deck ID: {deck_id}")
    # print(f"Cards Remaining: {remaining}")
    # print(f"Shuffled: {shuffled}")
    
    # TODO: Return deck_id for drawing cards
    return None  # Replace with actual deck_id

def draw_and_analyze_cards(deck_id, count=3):
    """
    TODO: Draw cards and extract detailed card information
    
    Steps to complete:
    1. TODO: Draw cards from the deck using deck_id
    2. TODO: Extract individual card details (value, suit, code, image)
    3. TODO: Create formatted card descriptions
    4. TODO: Display cards in an organized way
    
    Hint: Cards are usually in a 'cards' array, each with 'value', 'suit', 'code'
    """
    if not deck_id:
        print("⚠️ Need a valid deck_id to draw cards!")
        return
    
    print(f"\n🎴 Drawing {count} cards from deck {deck_id}...")
    
    # TODO: API call to draw cards
    # url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    
    # TODO: Extract cards array
    # cards = data['cards']  # This should be a list of card dictionaries
    
    # TODO: Display each card nicely
    print("\n🃏 YOUR CARDS:")
    print("=" * 50)
    
    # TODO: Loop through cards and extract info
    # for i, card in enumerate(cards, 1):
    #     value = card['value']
    #     suit = card['suit'] 
    #     code = card['code']
    #     
    #     print(f"Card {i}: {value} of {suit} (Code: {code})")
    
    print("=" * 50)

def card_collection_summary(deck_id, draw_count=5):
    """
    TODO: Create a comprehensive card analysis system
    
    🎮 Try This: Extend your skills by analyzing multiple cards!
    This function is for when you want to challenge yourself further.
    """
    print(f"\n📈 CARD COLLECTION ANALYSIS")
    print("-" * 40)
    
    # TODO: Draw cards
    # TODO: Count suits (Hearts, Diamonds, etc.)
    # TODO: Identify face cards (Jack, Queen, King)
    # TODO: Calculate total card value (if numeric)
    
    print("Challenge: Implement this after mastering the functions above!")

def main():
    """
    TODO: Run your card data extraction system
    """
    print("🎨 Card Data Mining Operation!")
    print("=" * 50)
    
    # TODO: Create deck and get info
    deck_id = None  # TODO: Get from create_deck_and_extract_info()
    
    # TODO: Draw and analyze cards 
    # draw_and_analyze_cards(deck_id, 3)
    
    # TODO: Try the advanced analysis (when ready)
    # card_collection_summary(deck_id, 5)
    
    print("\n✨ You're mining API data like a professional!")

if __name__ == "__main__":
    main()