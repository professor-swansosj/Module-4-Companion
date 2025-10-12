"""
Game Logic Module - War Card Game Implementation
===============================================

This module contains the core game logic for the War card game.
It demonstrates object-oriented programming principles and state
management while integrating with the API module.

Learning Objectives Demonstrated:
- Class design and encapsulation
- State management
- Algorithm implementation
- Data validation and error handling
- Integration with external APIs
"""

import random
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class Card:
    """
    Represents a playing card with value and suit
    """
    
    # Define card value hierarchy for comparison
    VALUE_ORDER = {
        'ACE': 14, 'KING': 13, 'QUEEN': 12, 'JACK': 11,
        '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5,
        '4': 4, '3': 3, '2': 2
    }
    
    def __init__(self, api_card: Dict):
        """
        Initialize card from API response
        
        Args:
            api_card: Dictionary from Deck of Cards API
        """
        self.code = api_card.get('code', '')
        self.value = api_card.get('value', '')
        self.suit = api_card.get('suit', '')
        self.image_url = api_card.get('image', '')
        
    def get_numeric_value(self) -> int:
        """Get numeric value for card comparison"""
        return self.VALUE_ORDER.get(self.value, 0)
    
    def __str__(self) -> str:
        """String representation of the card"""
        return f"{self.value} of {self.suit}"
    
    def __repr__(self) -> str:
        """Developer representation of the card"""
        return f"Card({self.code}: {self.value} of {self.suit})"
    
    def __eq__(self, other) -> bool:
        """Check if two cards have equal value"""
        if isinstance(other, Card):
            return self.get_numeric_value() == other.get_numeric_value()
        return False
    
    def __gt__(self, other) -> bool:
        """Check if this card is greater than another"""
        if isinstance(other, Card):
            return self.get_numeric_value() > other.get_numeric_value()
        return False
    
    def __lt__(self, other) -> bool:
        """Check if this card is less than another"""
        if isinstance(other, Card):
            return self.get_numeric_value() < other.get_numeric_value()
        return False


class WarGame:
    """
    Implements the War card game logic
    """
    
    def __init__(self, deck_api, player1_name: str = "Player 1", player2_name: str = "Player 2"):
        """
        Initialize a new War game
        
        Args:
            deck_api: Instance of DeckAPI for card operations
            player1_name: Name of first player
            player2_name: Name of second player
        """
        self.deck_api = deck_api
        self.player1_name = player1_name
        self.player2_name = player2_name
        
        # Game state
        self.deck_id = None
        self.player1_cards = []
        self.player2_cards = []
        
        # Statistics
        self.rounds_played = 0
        self.wars_fought = 0
        self.start_time = datetime.now()
        self.end_time = None
        
        # Game history for debugging/analysis
        self.game_history = []
    
    def setup_game(self) -> bool:
        """
        Setup a new game by creating deck and dealing cards
        
        Returns:
            True if setup successful, False otherwise
        """
        try:
            # Create a new shuffled deck
            deck_info = self.deck_api.create_new_deck(shuffled=True)
            if not deck_info:
                return False
                
            self.deck_id = deck_info['deck_id']
            
            # Draw all 52 cards
            all_cards = self.deck_api.draw_cards(self.deck_id, 52)
            if not all_cards or len(all_cards) != 52:
                return False
            
            # Convert API cards to Card objects
            cards = [Card(api_card) for api_card in all_cards]
            
            # Deal cards alternately to each player
            self.player1_cards = cards[0::2]  # Even indices (0, 2, 4, ...)
            self.player2_cards = cards[1::2]  # Odd indices (1, 3, 5, ...)
            
            # Verify each player has 26 cards
            if len(self.player1_cards) != 26 or len(self.player2_cards) != 26:
                return False
            
            self.start_time = datetime.now()
            return True
            
        except Exception as e:
            print(f"Error setting up game: {e}")
            return False
    
    def play_round(self) -> Optional[Dict]:
        """
        Play one round of War
        
        Returns:
            Dictionary with round results or None if error
        """
        if self.is_game_over():
            return None
            
        try:
            # Each player plays their top card
            p1_card = self.player1_cards.pop(0)
            p2_card = self.player2_cards.pop(0)
            
            # Track cards in play
            cards_in_play = [p1_card, p2_card]
            
            result = {
                'round_number': self.rounds_played + 1,
                'player1_card': {
                    'value': p1_card.value,
                    'suit': p1_card.suit,
                    'code': p1_card.code
                },
                'player2_card': {
                    'value': p2_card.value,
                    'suit': p2_card.suit,
                    'code': p2_card.code
                }
            }
            
            # Compare cards
            if p1_card > p2_card:
                # Player 1 wins
                self.player1_cards.extend(cards_in_play)
                result['winner'] = self.player1_name
                result['cards_won'] = len(cards_in_play)
                
            elif p2_card > p1_card:
                # Player 2 wins
                self.player2_cards.extend(cards_in_play)
                result['winner'] = self.player2_name
                result['cards_won'] = len(cards_in_play)
                
            else:
                # War! Cards are equal
                war_result = self._handle_war(cards_in_play)
                result['winner'] = 'tie'
                
                if war_result:
                    result.update(war_result)
                else:
                    # War couldn't be completed (not enough cards)
                    result['war_incomplete'] = True
            
            self.rounds_played += 1
            self.game_history.append(result)
            
            return result
            
        except (IndexError, Exception) as e:
            print(f"Error in round: {e}")
            return None
    
    def _handle_war(self, cards_in_play: List[Card]) -> Optional[Dict]:
        """
        Handle a war situation when cards are equal
        
        Args:
            cards_in_play: List of cards currently in play
            
        Returns:
            Dictionary with war results or None if war impossible
        """
        self.wars_fought += 1
        
        # Check if both players have enough cards for war
        # Need at least 4 cards each (3 down + 1 up)
        if len(self.player1_cards) < 4 or len(self.player2_cards) < 4:
            # Not enough cards for war - player with more cards wins all
            if len(self.player1_cards) > len(self.player2_cards):
                self.player1_cards.extend(cards_in_play)
                self.player1_cards.extend(self.player2_cards)
                self.player2_cards.clear()
                return {
                    'war_incomplete': True,
                    'final_winner': self.player1_name,
                    'cards_won': len(cards_in_play) + len(self.player2_cards)
                }
            else:
                self.player2_cards.extend(cards_in_play)
                self.player2_cards.extend(self.player1_cards)
                self.player1_cards.clear()
                return {
                    'war_incomplete': True,
                    'final_winner': self.player2_name,
                    'cards_won': len(cards_in_play) + len(self.player1_cards)
                }
        
        # Both players have enough cards for war
        # Each player puts down 3 cards face-down and 1 face-up
        p1_war_cards = [self.player1_cards.pop(0) for _ in range(4)]
        p2_war_cards = [self.player2_cards.pop(0) for _ in range(4)]
        
        # Add war cards to cards in play
        cards_in_play.extend(p1_war_cards)
        cards_in_play.extend(p2_war_cards)
        
        # Compare the face-up cards (last card from each player)
        p1_battle_card = p1_war_cards[-1]
        p2_battle_card = p2_war_cards[-1]
        
        war_result = {
            'war_cards': {
                'player1': [{
                    'value': card.value,
                    'suit': card.suit,
                    'code': card.code
                } for card in p1_war_cards],
                'player2': [{
                    'value': card.value,
                    'suit': card.suit,
                    'code': card.code
                } for card in p2_war_cards]
            }
        }
        
        # Determine winner of war
        if p1_battle_card > p2_battle_card:
            self.player1_cards.extend(cards_in_play)
            war_result['final_winner'] = self.player1_name
            
        elif p2_battle_card > p1_battle_card:
            self.player2_cards.extend(cards_in_play)
            war_result['final_winner'] = self.player2_name
            
        else:
            # Another tie! Recursive war
            nested_war = self._handle_war(cards_in_play)
            if nested_war:
                war_result.update(nested_war)
            else:
                war_result['multiple_wars'] = True
        
        war_result['cards_won'] = len(cards_in_play)
        return war_result
    
    def is_game_over(self) -> bool:
        """Check if the game is over"""
        return len(self.player1_cards) == 0 or len(self.player2_cards) == 0
    
    def get_winner(self) -> Optional[str]:
        """
        Get the winner of the game
        
        Returns:
            Name of winning player or None if game not over
        """
        if not self.is_game_over():
            return None
            
        if len(self.player1_cards) == 0:
            return self.player2_name
        else:
            return self.player1_name
    
    def get_game_duration(self) -> str:
        """
        Get formatted game duration
        
        Returns:
            String representation of game duration
        """
        if self.end_time:
            duration = self.end_time - self.start_time
        else:
            duration = datetime.now() - self.start_time
            
        total_seconds = int(duration.total_seconds())
        
        if total_seconds < 60:
            return f"{total_seconds} seconds"
        elif total_seconds < 3600:
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            return f"{minutes}m {seconds}s"
        else:
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            return f"{hours}h {minutes}m"
    
    def get_game_stats(self) -> Dict:
        """
        Get comprehensive game statistics
        
        Returns:
            Dictionary with game statistics
        """
        return {
            'rounds_played': self.rounds_played,
            'wars_fought': self.wars_fought,
            'duration': self.get_game_duration(),
            'player1_cards': len(self.player1_cards),
            'player2_cards': len(self.player2_cards),
            'game_over': self.is_game_over(),
            'winner': self.get_winner(),
            'start_time': self.start_time.isoformat(),
            'cards_distribution': {
                self.player1_name: len(self.player1_cards),
                self.player2_name: len(self.player2_cards)
            }
        }


class GameStats:
    """
    Tracks statistics across multiple games
    """
    
    def __init__(self):
        """Initialize statistics tracker"""
        self.games_played = []
        
    def record_game(self, game: WarGame):
        """
        Record a completed game
        
        Args:
            game: Completed WarGame instance
        """
        game.end_time = datetime.now()
        
        game_record = {
            'player1_name': game.player1_name,
            'player2_name': game.player2_name,
            'winner': game.get_winner(),
            'rounds_played': game.rounds_played,
            'wars_fought': game.wars_fought,
            'duration_seconds': (game.end_time - game.start_time).total_seconds(),
            'start_time': game.start_time,
            'end_time': game.end_time
        }
        
        self.games_played.append(game_record)
    
    def get_summary(self) -> Dict:
        """
        Get summary statistics across all games
        
        Returns:
            Dictionary with summary statistics
        """
        if not self.games_played:
            return {
                'total_games': 0,
                'average_duration': '0 seconds',
                'average_rounds': 0.0,
                'total_wars': 0,
                'longest_game': 0,
                'shortest_game': 0,
                'player_wins': {}
            }
        
        total_games = len(self.games_played)
        total_rounds = sum(game['rounds_played'] for game in self.games_played)
        total_wars = sum(game['wars_fought'] for game in self.games_played)
        total_duration = sum(game['duration_seconds'] for game in self.games_played)
        
        # Calculate averages
        avg_duration_seconds = total_duration / total_games
        avg_rounds = total_rounds / total_games
        
        # Format average duration
        if avg_duration_seconds < 60:
            avg_duration_str = f"{avg_duration_seconds:.1f} seconds"
        elif avg_duration_seconds < 3600:
            minutes = avg_duration_seconds // 60
            seconds = avg_duration_seconds % 60
            avg_duration_str = f"{minutes:.0f}m {seconds:.0f}s"
        else:
            hours = avg_duration_seconds // 3600
            minutes = (avg_duration_seconds % 3600) // 60
            avg_duration_str = f"{hours:.0f}h {minutes:.0f}m"
        
        # Find longest and shortest games
        rounds_list = [game['rounds_played'] for game in self.games_played]
        longest_game = max(rounds_list)
        shortest_game = min(rounds_list)
        
        # Count player wins
        player_wins = {}
        for game in self.games_played:
            winner = game['winner']
            if winner:
                player_wins[winner] = player_wins.get(winner, 0) + 1
        
        return {
            'total_games': total_games,
            'average_duration': avg_duration_str,
            'average_rounds': avg_rounds,
            'total_wars': total_wars,
            'longest_game': longest_game,
            'shortest_game': shortest_game,
            'player_wins': player_wins
        }
    
    def get_recent_games(self, count: int = 5) -> List[Dict]:
        """
        Get most recent games
        
        Args:
            count: Number of recent games to return
            
        Returns:
            List of recent game records
        """
        return self.games_played[-count:] if self.games_played else []
    
    def clear_stats(self):
        """Clear all recorded statistics"""
        self.games_played.clear()


def demo_game_logic():
    """
    Demo function for testing game logic without API
    """
    print("🎮 War Game Logic Demo")
    print("=" * 30)
    
    # Create mock cards for testing
    class MockDeckAPI:
        def __init__(self):
            pass
            
        def create_new_deck(self, shuffled=True):
            return {'deck_id': 'mock123', 'shuffled': True, 'remaining': 52}
            
        def draw_cards(self, deck_id, count):
            # Create a simple set of test cards
            suits = ['HEARTS', 'DIAMONDS', 'CLUBS', 'SPADES']
            values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING', 'ACE']
            
            cards = []
            for i in range(count):
                suit = suits[i % 4]
                value = values[i % 13]
                cards.append({
                    'code': f'{value[0]}{suit[0]}',
                    'value': value,
                    'suit': suit,
                    'image': 'mock_image_url'
                })
            return cards
    
    # Test card comparison
    print("1. Testing card values...")
    card1 = Card({'code': 'AS', 'value': 'ACE', 'suit': 'SPADES'})
    card2 = Card({'code': 'KH', 'value': 'KING', 'suit': 'HEARTS'})
    
    print(f"   {card1} vs {card2}")
    print(f"   ACE > KING: {card1 > card2}")
    print(f"   Values: ACE={card1.get_numeric_value()}, KING={card2.get_numeric_value()}")
    
    # Test game setup
    print("\n2. Testing game setup...")
    mock_api = MockDeckAPI()
    game = WarGame(mock_api, "Alice", "Bob")
    
    if game.setup_game():
        print("   ✅ Game setup successful")
        print(f"   Alice has {len(game.player1_cards)} cards")
        print(f"   Bob has {len(game.player2_cards)} cards")
    else:
        print("   ❌ Game setup failed")
    
    print("\n✅ Game logic demo complete!")


if __name__ == "__main__":
    # Run demo if script is executed directly
    demo_game_logic()