"""
Module 04: Simple Card War - Logic Meets APIs
TODO: Build a simple War card game using conditional logic

Your mission:
1. Create a deck and draw cards for two players
2. Compare card values using conditional logic
3. Determine winner based on card strength
4. Create an engaging game experience!

Hint: You'll need to convert card values to numbers for comparison!
"""

import requests

def get_card_value(card):
    """
    TODO: Convert card values to numbers for comparison
    
    Steps to complete:
    1. TODO: Get the card's value (like "KING", "7", "ACE")
    2. TODO: Convert face cards to numbers (Jack=11, Queen=12, King=13)
    3. TODO: Handle ACE (usually 14 in War, but could be 1)
    4. TODO: Convert number cards to integers
    
    Hint: Use if/elif statements to handle different card types
    """
    card_value = card['value']
    
    # TODO: Handle face cards
    if card_value == "JACK":
        return 11
    elif card_value == "QUEEN":
        return 12
    # TODO: Add more face card conditions
    # elif card_value == ???:
    #     return ???
    
    # TODO: Handle number cards
    # else:
    #     return int(card_value)
    
    return 0  # TODO: Replace with actual logic

def play_war_round(deck_id):
    """
    TODO: Draw cards for two players and determine winner
    
    Steps to complete:
    1. TODO: Draw 2 cards from the deck (one for each player)
    2. TODO: Extract card information for display
    3. TODO: Get numeric values for comparison
    4. TODO: Determine and announce winner
    5. TODO: Return winner info
    
    Hint: Use the get_card_value function you created above!
    """
    print("\n🎲 Drawing cards for the battle...")
    
    # TODO: Draw 2 cards from deck
    # url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=2"
    
    # TODO: Extract the two cards
    # cards = data['cards']
    # player1_card = cards[0]  
    # player2_card = cards[1]
    
    # TODO: Display the cards
    print("\n🎴 THE CARDS ARE DRAWN!")
    print("-" * 40)
    # print(f"Player 1: {player1_card['value']} of {player1_card['suit']}")
    # print(f"Player 2: {player2_card['value']} of {player2_card['suit']}")
    
    # TODO: Get numeric values for comparison
    # value1 = get_card_value(player1_card)
    # value2 = get_card_value(player2_card)
    
    # TODO: Determine winner
    print("\n⚔️ BATTLE RESULT:")
    # if value1 > value2:
    #     print("🏆 Player 1 wins this round!")
    #     return "Player 1"
    # elif value2 > value1:
    #     print("🏆 Player 2 wins this round!")
    #     return "Player 2"
    # else:
    #     print("🤝 It's a tie!")
    #     return "Tie"

def play_war_game(rounds=3):
    """
    TODO: Play multiple rounds and track winners
    
    Steps to complete:
    1. TODO: Create a new deck for the game
    2. TODO: Play specified number of rounds
    3. TODO: Track wins for each player
    4. TODO: Announce final winner
    
    🎮 Try This: Add more rounds or best-of-X gameplay!
    """
    print("⚔️ WELCOME TO CARD WAR!")
    print("=" * 50)
    
    # TODO: Create new shuffled deck
    
    # TODO: Initialize score tracking
    player1_wins = 0
    player2_wins = 0
    ties = 0
    
    # TODO: Play multiple rounds
    for round_num in range(1, rounds + 1):
        print(f"\n🎯 ROUND {round_num}")
        
        # TODO: Play one round and get winner
        # winner = play_war_round(deck_id)
        
        # TODO: Update scores based on winner
        # if winner == "Player 1":
        #     player1_wins += 1
        # elif winner == "Player 2":  
        #     player2_wins += 1
        # else:
        #     ties += 1
        
        input("Press Enter to continue to next round...")
    
    # TODO: Announce final results
    print("\n🏁 FINAL RESULTS")
    print("=" * 30)
    # print(f"Player 1 wins: {player1_wins}")
    # print(f"Player 2 wins: {player2_wins}")  
    # print(f"Ties: {ties}")
    
    # TODO: Declare overall winner
    # if player1_wins > player2_wins:
    #     print("🎉 Player 1 is the War Champion!")
    # elif player2_wins > player1_wins:
    #     print("🎉 Player 2 is the War Champion!")
    # else:
    #     print("🤝 It's a tie overall!")

def main():
    """
    TODO: Start your War card game!
    """
    print("🎮 Simple Card War Game!")
    print("=" * 30)
    
    # TODO: Ask user how many rounds to play
    # rounds = int(input("How many rounds would you like to play? (1-10): "))
    
    # TODO: Start the game
    # play_war_game(rounds)
    
    print("\n✨ You just built a game with API logic!")

if __name__ == "__main__":
    main()