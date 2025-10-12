"""
Card API Module - Deck of Cards API Interface
============================================

This module handles all interactions with the Deck of Cards API.
It demonstrates proper API request patterns, error handling, and
response processing techniques learned in Module 4.

API Documentation: https://deckofcardsapi.com/

Learning Objectives Demonstrated:
- Making HTTP GET requests
- Handling API responses and errors
- Processing JSON data
- Implementing retry logic
- Managing API state and rate limits
"""

import requests
import json
import time
from typing import Dict, List, Optional, Union


class DeckAPI:
    """
    Interface to the Deck of Cards API
    
    This class demonstrates best practices for API interaction:
    - Proper error handling
    - Request retry logic  
    - Response validation
    - State management
    """
    
    def __init__(self):
        """Initialize the API client"""
        self.base_url = "https://deckofcardsapi.com/api/deck"
        self.session = requests.Session()
        
        # Set reasonable timeouts
        self.session.timeout = 10
        
        # Add headers for better API experience
        self.session.headers.update({
            'User-Agent': 'FSCJ-SDN-Module4-WarGame/1.0',
            'Accept': 'application/json'
        })
        
        # Statistics tracking
        self._api_calls = 0
        self._api_errors = 0
        self._last_error = None
        
    def _make_request(self, url: str, max_retries: int = 3) -> Optional[Dict]:
        """
        Make an API request with retry logic
        
        Args:
            url: The URL to request
            max_retries: Maximum number of retry attempts
            
        Returns:
            JSON response as dictionary or None if failed
        """
        self._api_calls += 1
        
        for attempt in range(max_retries + 1):
            try:
                response = self.session.get(url)
                
                # Check for HTTP errors
                response.raise_for_status()
                
                # Parse JSON response
                data = response.json()
                
                # Check for API-specific errors
                if not data.get('success', True):
                    error_msg = data.get('error', 'Unknown API error')
                    raise Exception(f"API Error: {error_msg}")
                
                return data
                
            except requests.exceptions.Timeout:
                self._api_errors += 1
                self._last_error = f"Timeout on attempt {attempt + 1}"
                if attempt < max_retries:
                    time.sleep(1 * (attempt + 1))  # Exponential backoff
                    continue
                    
            except requests.exceptions.ConnectionError:
                self._api_errors += 1
                self._last_error = f"Connection error on attempt {attempt + 1}"
                if attempt < max_retries:
                    time.sleep(2 * (attempt + 1))
                    continue
                    
            except requests.exceptions.HTTPError as e:
                self._api_errors += 1
                self._last_error = f"HTTP {e.response.status_code}: {e.response.reason}"
                # Don't retry on 4xx client errors
                if 400 <= e.response.status_code < 500:
                    break
                if attempt < max_retries:
                    time.sleep(1 * (attempt + 1))
                    continue
                    
            except json.JSONDecodeError:
                self._api_errors += 1
                self._last_error = f"Invalid JSON response on attempt {attempt + 1}"
                if attempt < max_retries:
                    time.sleep(1 * (attempt + 1))
                    continue
                    
            except Exception as e:
                self._api_errors += 1
                self._last_error = f"Unexpected error: {str(e)}"
                if attempt < max_retries:
                    time.sleep(1 * (attempt + 1))
                    continue
        
        # All attempts failed
        return None
    
    def create_new_deck(self, shuffled: bool = True) -> Optional[Dict]:
        """
        Create a new shuffled deck of cards
        
        Args:
            shuffled: Whether to shuffle the deck (default: True)
            
        Returns:
            Dictionary with deck info or None if failed
            Example: {
                'success': True,
                'deck_id': 'abc123',
                'shuffled': True,
                'remaining': 52
            }
        """
        shuffle_param = "true" if shuffled else "false"
        url = f"{self.base_url}/new/shuffle/{shuffle_param}/"
        
        result = self._make_request(url)
        
        if result:
            # Validate expected fields
            required_fields = ['deck_id', 'shuffled', 'remaining']
            if all(field in result for field in required_fields):
                return result
            else:
                self._last_error = "API response missing required fields"
        
        return None
    
    def draw_cards(self, deck_id: str, count: int = 1) -> Optional[List[Dict]]:
        """
        Draw cards from a deck
        
        Args:
            deck_id: The ID of the deck to draw from
            count: Number of cards to draw (default: 1)
            
        Returns:
            List of card dictionaries or None if failed
            Example card: {
                'code': 'AS',
                'image': 'https://...',
                'images': {...},
                'value': 'ACE',
                'suit': 'SPADES'
            }
        """
        if not deck_id or count <= 0:
            self._last_error = "Invalid deck_id or count"
            return None
            
        url = f"{self.base_url}/{deck_id}/draw/?count={count}"
        
        result = self._make_request(url)
        
        if result and 'cards' in result:
            cards = result['cards']
            
            # Validate card structure
            valid_cards = []
            for card in cards:
                if all(field in card for field in ['code', 'value', 'suit']):
                    valid_cards.append(card)
                    
            return valid_cards if valid_cards else None
        
        return None
    
    def get_deck_info(self, deck_id: str) -> Optional[Dict]:
        """
        Get information about a deck
        
        Args:
            deck_id: The ID of the deck
            
        Returns:
            Dictionary with deck info or None if failed
        """
        if not deck_id:
            self._last_error = "Invalid deck_id"
            return None
            
        url = f"{self.base_url}/{deck_id}/"
        
        return self._make_request(url)
    
    def shuffle_deck(self, deck_id: str) -> Optional[Dict]:
        """
        Shuffle an existing deck
        
        Args:
            deck_id: The ID of the deck to shuffle
            
        Returns:
            Dictionary with shuffle result or None if failed
        """
        if not deck_id:
            self._last_error = "Invalid deck_id"
            return None
            
        url = f"{self.base_url}/{deck_id}/shuffle/"
        
        return self._make_request(url)
    
    def create_pile(self, deck_id: str, pile_name: str, cards: List[str]) -> Optional[Dict]:
        """
        Create a pile with specific cards
        
        Args:
            deck_id: The ID of the deck
            pile_name: Name for the pile
            cards: List of card codes (e.g., ['AS', 'KH'])
            
        Returns:
            Dictionary with pile creation result or None if failed
        """
        if not all([deck_id, pile_name, cards]):
            self._last_error = "Invalid parameters for pile creation"
            return None
            
        cards_param = ','.join(cards)
        url = f"{self.base_url}/{deck_id}/pile/{pile_name}/add/?cards={cards_param}"
        
        return self._make_request(url)
    
    def draw_from_pile(self, deck_id: str, pile_name: str, count: int = 1) -> Optional[List[Dict]]:
        """
        Draw cards from a pile
        
        Args:
            deck_id: The ID of the deck
            pile_name: Name of the pile
            count: Number of cards to draw
            
        Returns:
            List of card dictionaries or None if failed
        """
        if not all([deck_id, pile_name]) or count <= 0:
            self._last_error = "Invalid parameters for pile draw"
            return None
            
        url = f"{self.base_url}/{deck_id}/pile/{pile_name}/draw/?count={count}"
        
        result = self._make_request(url)
        
        if result and 'cards' in result:
            return result['cards']
        
        return None
    
    def get_api_call_count(self) -> int:
        """Get the total number of API calls made"""
        return self._api_calls
    
    def get_error_count(self) -> int:
        """Get the total number of API errors encountered"""
        return self._api_errors
    
    def get_last_error(self) -> Optional[str]:
        """Get the last error message"""
        return self._last_error
    
    def reset_stats(self):
        """Reset API statistics"""
        self._api_calls = 0
        self._api_errors = 0
        self._last_error = None


def demo_api_usage():
    """
    Demonstration function showing various API features
    """
    print("🎴 Deck of Cards API Demo")
    print("=" * 30)
    
    # Create API client
    api = DeckAPI()
    
    # Test 1: Create a new deck
    print("1. Creating a new shuffled deck...")
    deck_info = api.create_new_deck()
    
    if deck_info:
        deck_id = deck_info['deck_id']
        print(f"   ✅ Created deck: {deck_id}")
        print(f"   🃏 Cards remaining: {deck_info['remaining']}")
    else:
        print(f"   ❌ Failed to create deck: {api.get_last_error()}")
        return
    
    # Test 2: Draw some cards
    print("\n2. Drawing 5 cards...")
    cards = api.draw_cards(deck_id, 5)
    
    if cards:
        print(f"   ✅ Drew {len(cards)} cards:")
        for i, card in enumerate(cards, 1):
            print(f"      {i}. {card['value']} of {card['suit']}")
    else:
        print(f"   ❌ Failed to draw cards: {api.get_last_error()}")
    
    # Test 3: Check deck status
    print("\n3. Checking deck status...")
    deck_status = api.get_deck_info(deck_id)
    
    if deck_status:
        print(f"   ✅ Cards remaining: {deck_status['remaining']}")
    else:
        print(f"   ❌ Failed to get deck info: {api.get_last_error()}")
    
    # Test 4: Show statistics
    print(f"\n4. API Statistics:")
    print(f"   Total API calls: {api.get_api_call_count()}")
    print(f"   API errors: {api.get_error_count()}")
    
    if api.get_last_error():
        print(f"   Last error: {api.get_last_error()}")


if __name__ == "__main__":
    # Run demo if script is executed directly
    demo_api_usage()