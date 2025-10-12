#!/usr/bin/env python3
"""
War Card Game - Main Lab Project for Module 4
============================================

This is the main War Card Game that demonstrates all concepts learned
in Module 4: Python Requests Library. The game uses the Deck of Cards API
to create an authentic card game experience while practicing API skills.

Learning Objectives Demonstrated:
- Making API requests to external services
- Handling JSON responses and error cases
- Managing game state with API data
- Implementing retry logic and error handling
- User interface and experience design

Author: FSCJ - Software Defined Networking Course
API Used: https://deckofcardsapi.com/
"""

import sys
import os
import time
from datetime import datetime

# Add the current directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from card_api import DeckAPI
from game_logic import WarGame, GameStats


class WarCardGameApp:
    """
    Main application class for the War Card Game
    """
    
    def __init__(self):
        """Initialize the game application"""
        self.deck_api = DeckAPI()
        self.current_game = None
        self.game_stats = GameStats()
        self.running = True
        
    def display_welcome(self):
        """Display the welcome screen"""
        print("=" * 70)
        print("🎮 WAR CARD GAME - Module 4 Lab Project")
        print("Software Defined Networking - Python Requests Library")
        print("FSCJ Computer Science Department")
        print("=" * 70)
        print()
        print("Welcome to War! This classic card game demonstrates:")
        print("✓ Making HTTP requests to external APIs")
        print("✓ Processing JSON responses")  
        print("✓ Error handling and retry logic")
        print("✓ Managing application state")
        print("✓ Creating user-friendly interfaces")
        print()
        print("Game Rules:")
        print("• Each player gets half the deck (26 cards)")
        print("• Players simultaneously reveal their top card")
        print("• Higher card wins both cards")
        print("• Ace is high (A > K > Q > J > 10 > ... > 2)")
        print("• When cards are equal, it's WAR!")
        print("• In war, each player places 3 cards down and 1 up")
        print("• Winner of war takes all cards")
        print("• Game ends when one player runs out of cards")
        print()
        
    def display_main_menu(self):
        """Display the main menu"""
        print("🎯 MAIN MENU")
        print("-" * 30)
        print("1. 🆚 Start New Game")
        print("2. 📊 View Game Statistics") 
        print("3. 🔧 Test API Connection")
        print("4. 📚 How to Play")
        print("5. 🚪 Exit")
        print()
        
    def test_api_connection(self):
        """Test the connection to the Deck of Cards API"""
        print("🔍 Testing API Connection...")
        print("-" * 40)
        
        try:
            # Test creating a new deck
            deck_info = self.deck_api.create_new_deck()
            if deck_info:
                print("✅ API Connection: SUCCESS")
                print(f"📦 Created test deck: {deck_info['deck_id']}")
                print(f"🃏 Cards in deck: {deck_info['remaining']}")
                print(f"🔀 Shuffled: {'Yes' if deck_info['shuffled'] else 'No'}")
                
                # Test drawing cards
                cards = self.deck_api.draw_cards(deck_info['deck_id'], 2)
                if cards:
                    print(f"\n🎴 Drew {len(cards)} test cards:")
                    for card in cards:
                        print(f"   • {card['value']} of {card['suit']}")
                    
                    print("\n✅ All API functions working correctly!")
                else:
                    print("⚠️  Could draw cards, but no data returned")
            else:
                print("❌ Failed to create test deck")
                
        except Exception as e:
            print(f"❌ API Connection Failed: {e}")
            print("💡 Please check your internet connection")
            
        input("\nPress Enter to continue...")
        
    def show_how_to_play(self):
        """Display detailed game rules"""
        print("📚 HOW TO PLAY WAR")
        print("=" * 50)
        
        rules = [
            "🎯 OBJECTIVE: Capture all 52 cards to win!",
            "",
            "🎴 SETUP:",
            "  • The deck is shuffled and split evenly",
            "  • Each player gets 26 cards face-down",
            "  • Cards are kept in a stack, no looking!",
            "",
            "⚔️  BATTLE PHASE:",
            "  • Both players flip their top card simultaneously",
            "  • Higher card wins both cards (A > K > Q > J > 10...2)",
            "  • Winner puts both cards at bottom of their stack",
            "",
            "💥 WAR SITUATION:",
            "  • When both cards have the same value: WAR!",
            "  • Each player places 3 cards face-down, then 1 face-up",
            "  • The face-up cards compete normally",
            "  • Winner takes all 8+ cards from the war",
            "",
            "🏆 WINNING:",
            "  • Game ends when one player runs out of cards",
            "  • Player with all cards wins!",
            "",
            "🎮 CONTROLS:",
            "  • Press Enter to flip next cards",
            "  • Type 'stats' to see current game stats", 
            "  • Type 'quit' to end current game",
            "",
            "💡 TIP: Games can be quick or last a very long time!"
        ]
        
        for rule in rules:
            print(rule)
            
        input("\nPress Enter to return to menu...")
        
    def start_new_game(self):
        """Start a new War card game"""
        print("🎮 STARTING NEW GAME")
        print("-" * 30)
        
        # Get player names
        player1_name = input("Enter Player 1 name (or press Enter for 'Player 1'): ").strip()
        if not player1_name:
            player1_name = "Player 1"
            
        player2_name = input("Enter Player 2 name (or press Enter for 'Player 2'): ").strip()  
        if not player2_name:
            player2_name = "Player 2"
            
        print(f"\n🎊 Welcome {player1_name} and {player2_name}!")
        print("Setting up the game...")
        
        # Create and setup the game
        try:
            self.current_game = WarGame(self.deck_api, player1_name, player2_name)
            
            if self.current_game.setup_game():
                print("✅ Game setup complete!")
                print(f"🃏 Each player has {len(self.current_game.player1_cards)} cards")
                self.play_game()
            else:
                print("❌ Failed to setup game. Please try again.")
                input("Press Enter to continue...")
                
        except Exception as e:
            print(f"❌ Error starting game: {e}")
            input("Press Enter to continue...")
            
    def play_game(self):
        """Main game loop"""
        print(f"\n🚀 Game Started! {datetime.now().strftime('%H:%M:%S')}")
        print("=" * 50)
        print("Press Enter to flip cards, 'stats' for info, 'quit' to exit")
        print()
        
        round_number = 1
        
        while not self.current_game.is_game_over():
            # Show current status
            p1_count = len(self.current_game.player1_cards)
            p2_count = len(self.current_game.player2_cards)
            
            print(f"🎯 Round {round_number}")
            print(f"{self.current_game.player1_name}: {p1_count} cards | {self.current_game.player2_name}: {p2_count} cards")
            
            # Get user input
            user_input = input(">>> ").strip().lower()
            
            if user_input == 'quit':
                print("🏃 Quitting current game...")
                break
            elif user_input == 'stats':
                self.show_game_stats()
                continue
            elif user_input != '':
                print("💡 Press Enter to continue, 'stats' for info, or 'quit' to exit")
                continue
            
            # Play a round
            try:
                result = self.current_game.play_round()
                
                if result:
                    self.display_round_result(result, round_number)
                    round_number += 1
                    
                    # Small delay for dramatic effect
                    time.sleep(0.5)
                else:
                    print("❌ Error playing round")
                    break
                    
            except Exception as e:
                print(f"❌ Error during round: {e}")
                break
        
        # Game over
        if self.current_game.is_game_over():
            self.display_game_over()
            self.game_stats.record_game(self.current_game)
        
        input("\nPress Enter to return to main menu...")
        
    def display_round_result(self, result, round_num):
        """Display the result of a round"""
        print(f"\n📋 Round {round_num} Results:")
        print("-" * 30)
        
        # Show the cards played
        p1_card = result['player1_card']
        p2_card = result['player2_card']
        
        print(f"{self.current_game.player1_name}: {p1_card['value']} of {p1_card['suit']}")
        print(f"{self.current_game.player2_name}: {p2_card['value']} of {p2_card['suit']}")
        
        # Show the result
        if result['winner'] == 'tie':
            print("⚔️  WAR! Cards are equal!")
            if 'war_cards' in result:
                print(f"💥 Each player plays {len(result['war_cards']['player1'])} cards in war")
                war_p1 = result['war_cards']['player1'][-1]  # Last card is face-up
                war_p2 = result['war_cards']['player2'][-1]
                print(f"War cards: {war_p1['value']} of {war_p1['suit']} vs {war_p2['value']} of {war_p2['suit']}")
                print(f"🏆 {result['final_winner']} wins the war and {result['cards_won']} cards!")
        else:
            print(f"🏆 {result['winner']} wins this round!")
            print(f"🃏 Cards won: {result['cards_won']}")
        
        print()
        
    def show_game_stats(self):
        """Show current game statistics"""
        if not self.current_game:
            print("❌ No game in progress")
            return
            
        print("\n📊 CURRENT GAME STATS")
        print("-" * 25)
        print(f"Rounds played: {self.current_game.rounds_played}")
        print(f"Wars fought: {self.current_game.wars_fought}")
        print(f"Game duration: {self.current_game.get_game_duration()}")
        
        p1_count = len(self.current_game.player1_cards)
        p2_count = len(self.current_game.player2_cards)
        total_cards = p1_count + p2_count
        
        print(f"\n🃏 Card Distribution:")
        print(f"{self.current_game.player1_name}: {p1_count} cards ({p1_count/total_cards*100:.1f}%)")
        print(f"{self.current_game.player2_name}: {p2_count} cards ({p2_count/total_cards*100:.1f}%)")
        print()
        
    def display_game_over(self):
        """Display game over screen"""
        winner = self.current_game.get_winner()
        duration = self.current_game.get_game_duration()
        
        print("\n" + "=" * 50)
        print("🎊 GAME OVER! 🎊")
        print("=" * 50)
        
        if winner:
            print(f"🏆 WINNER: {winner}")
        else:
            print("🤝 Game ended in a tie (or was quit)")
            
        print(f"\n📊 Final Statistics:")
        print(f"   Rounds played: {self.current_game.rounds_played}")
        print(f"   Wars fought: {self.current_game.wars_fought}")
        print(f"   Game duration: {duration}")
        print(f"   Total API calls: {self.deck_api.get_api_call_count()}")
        
        # Show dramatic winner announcement
        if winner:
            print(f"\n🎉 Congratulations {winner}! 🎉")
            print("You have conquered the battlefield of War!")
        
    def view_statistics(self):
        """View overall game statistics"""
        print("📊 GAME STATISTICS")
        print("=" * 30)
        
        stats = self.game_stats.get_summary()
        
        if stats['total_games'] == 0:
            print("📈 No games played yet!")
            print("Start a game to see statistics here.")
        else:
            print(f"Total games played: {stats['total_games']}")
            print(f"Average game duration: {stats['average_duration']}")
            print(f"Average rounds per game: {stats['average_rounds']:.1f}")
            print(f"Total wars fought: {stats['total_wars']}")
            print(f"Longest game: {stats['longest_game']} rounds")
            print(f"Shortest game: {stats['shortest_game']} rounds")
            
            if stats['player_wins']:
                print(f"\n🏆 Player Win Records:")
                for player, wins in stats['player_wins'].items():
                    print(f"   {player}: {wins} wins")
        
        print(f"\nAPI Performance:")
        print(f"   Total API calls made: {self.deck_api.get_api_call_count()}")
        print(f"   API errors encountered: {self.deck_api.get_error_count()}")
        
        input("\nPress Enter to continue...")
        
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while self.running:
            self.display_main_menu()
            
            choice = input("Choose an option (1-5): ").strip()
            
            if choice == '1':
                self.start_new_game()
            elif choice == '2':
                self.view_statistics()
            elif choice == '3':
                self.test_api_connection()
            elif choice == '4':
                self.show_how_to_play()
            elif choice == '5':
                print("👋 Thanks for playing War!")
                print("You've successfully completed Module 4's lab project!")
                self.running = False
            else:
                print("❌ Invalid choice. Please select 1-5.")
                time.sleep(1)
            
            # Clear screen effect (works on most terminals)
            if self.running:
                print("\n" * 2)


def main():
    """Main entry point"""
    try:
        app = WarCardGameApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("Please report this to your instructor.")


if __name__ == "__main__":
    main()