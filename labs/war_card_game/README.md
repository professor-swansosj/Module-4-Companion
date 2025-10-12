# War Card Game - Module 4 Lab Project

## 🎮 Project Overview

Welcome to the **War Card Game** - the capstone lab project for Module 4: Python Requests Library. This comprehensive application demonstrates all the concepts learned throughout the module while creating an engaging and educational card game experience.

## 🎯 Learning Objectives

By completing this lab project, students will demonstrate mastery of:

- **HTTP Requests**: Making GET requests to external APIs
- **JSON Processing**: Parsing and handling JSON responses
- **Error Handling**: Implementing robust retry logic and error management
- **State Management**: Managing complex application state across game rounds
- **User Interface Design**: Creating an interactive command-line interface
- **API Integration**: Working with real-world REST APIs
- **Object-Oriented Programming**: Designing classes and managing object relationships

## 📚 Module Concepts Applied

This project integrates concepts from all Module 4 examples:

| Example | Concept Applied | Implementation |
|---------|-----------------|----------------|
| 01_introduction.py | Basic API requests | DeckAPI.create_new_deck() |
| 02_creating_requests.py | HTTP methods & parameters | Card drawing with count parameters |
| 03_sending_requests.py | Timeouts & retry logic | Robust error handling with backoff |
| 04_viewing_responses.py | Response analysis | Status code checking and validation |
| 05_json_conversion.py | JSON to Python objects | Card objects from API responses |
| 06_parsing_responses.py | Data validation | Response structure verification |

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Internet connection (for Deck of Cards API)
- Basic understanding of command-line interfaces

### Installation

1. **Clone or download** the lab files to your local machine
2. **Open terminal/command prompt** and navigate to the `war_card_game` directory
3. **Install requirements**:

   ```bash
   pip install requests
   ```

   Or use the requirements file:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

#### Option 1: Use the launcher script (Recommended)

```bash
python start_game.py
```

#### Option 2: Run directly

```bash
python war_game.py
```

The launcher script will check your environment and help troubleshoot any issues.

## 🎲 How to Play War

### Game Rules

1. **Setup**: The deck is shuffled and split evenly between two players (26 cards each)
2. **Battle**: Players simultaneously reveal their top card
3. **Winner**: Higher card wins both cards (Ace is high: A > K > Q > J > 10 > ... > 2)
4. **War**: When cards are equal, each player places 3 cards down and 1 up
5. **Victory**: Game ends when one player runs out of cards

### Game Controls

- **Enter**: Flip next cards
- **'stats'**: View current game statistics
- **'quit'**: End current game

## 🏗️ Project Structure

```bash
war_card_game/
├── war_game.py          # Main application and user interface
├── card_api.py          # Deck of Cards API integration
├── game_logic.py        # War game rules and mechanics
├── start_game.py        # Environment checker and launcher
├── requirements.txt     # Python dependencies
└── README.md           # This documentation
```

### File Descriptions

#### `war_game.py` - Main Application

- **WarCardGameApp**: Main application class managing the game flow
- **User Interface**: Menu system, game display, and user interaction
- **Game Management**: Starting games, showing statistics, API testing

#### `card_api.py` - API Integration

- **DeckAPI**: Complete interface to Deck of Cards API
- **Error Handling**: Retry logic with exponential backoff
- **Request Management**: Timeout handling and response validation
- **Statistics**: API call tracking and error monitoring

#### `game_logic.py` - Game Engine

- **Card**: Represents individual playing cards with comparison logic
- **WarGame**: Implements complete War game rules and mechanics
- **GameStats**: Tracks statistics across multiple games
- **War Resolution**: Handles complex war scenarios and edge cases

#### `start_game.py` - Environment Launcher

- **System Check**: Python version and module availability
- **Network Test**: Internet connection and API accessibility
- **User Guidance**: Setup assistance and troubleshooting

## 🔧 Technical Implementation

### API Integration Patterns

```python
# Example: Creating a new deck with proper error handling
def create_new_deck(self, shuffled=True):
    url = f"{self.base_url}/new/shuffle/{'true' if shuffled else 'false'}/"
    
    result = self._make_request(url)
    if result and all(field in result for field in ['deck_id', 'shuffled', 'remaining']):
        return result
    return None
```

### Error Handling Strategy

```python
# Retry logic with exponential backoff
for attempt in range(max_retries + 1):
    try:
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        if attempt < max_retries:
            time.sleep(1 * (attempt + 1))  # Exponential backoff
```

### State Management

The game maintains state across multiple objects:

- **DeckAPI**: Tracks API calls and errors
- **WarGame**: Manages current game state and history
- **GameStats**: Accumulates statistics across games

## 📊 Features & Functionality

### Core Features

- ✅ **Complete War Implementation**: All rules including multiple wars
- ✅ **Real-time API Integration**: Live card data from Deck of Cards API  
- ✅ **Comprehensive Error Handling**: Network timeouts, API errors, edge cases
- ✅ **Statistics Tracking**: Game duration, rounds, wars, player wins
- ✅ **User-friendly Interface**: Clear menus, helpful messages, game status
- ✅ **Environment Validation**: Python version, modules, internet connectivity

### Advanced Features

- 🎯 **War Scenarios**: Handles multiple consecutive wars
- 📈 **Performance Monitoring**: API call tracking and timing
- 🔄 **Retry Logic**: Automatic recovery from temporary failures
- 💾 **Game History**: Complete record of game events
- 🏆 **Winner Detection**: Proper end-game conditions

## 🧪 Testing & Debugging

### Manual Testing

1. **API Connection Test**:

   ```bash
   python -c "from card_api import DeckAPI; api = DeckAPI(); print(api.create_new_deck())"
   ```

2. **Game Logic Test**:

   ```bash
   python -c "from game_logic import demo_game_logic; demo_game_logic()"
   ```

3. **Full Integration Test**:
   Use the built-in "Test API Connection" option in the main menu

### Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| Import errors | Missing requests module | `pip install requests` |
| Connection timeout | Network issues | Check internet connection |
| API rate limits | Too many rapid requests | Built-in retry logic handles this |
| Game freezes | Infinite war scenario | Game includes safeguards |

## 📖 Educational Value

### For Students

This project demonstrates real-world software development practices:

- **API Integration**: Working with external services
- **Error Handling**: Building resilient applications
- **User Experience**: Creating intuitive interfaces
- **Code Organization**: Modular design and separation of concerns

### For Instructors

The project provides assessment opportunities for:

- **Technical Skills**: API usage, error handling, OOP
- **Problem Solving**: Debugging network and logic issues
- **Code Quality**: Documentation, organization, best practices
- **User Experience**: Interface design and usability

## 🔗 API Reference

This project uses the [Deck of Cards API](https://deckofcardsapi.com/):

- **Base URL**: `https://deckofcardsapi.com/api/deck`
- **Authentication**: None required
- **Rate Limits**: Reasonable usage expected
- **Documentation**: <https://deckofcardsapi.com/>

### Key Endpoints Used

- `GET /deck/new/shuffle/true/` - Create shuffled deck
- `GET /deck/{deck_id}/draw/?count={n}` - Draw cards
- `GET /deck/{deck_id}/` - Get deck info

## 🎓 Assessment Rubric

| Criteria | Excellent (A) | Good (B) | Satisfactory (C) | Needs Work (D/F) |
|----------|---------------|----------|------------------|------------------|
| **API Integration** | Proper error handling, retry logic | Basic requests work | Simple API calls | Frequent failures |
| **Game Logic** | All rules implemented correctly | Most rules work | Basic gameplay | Major logic errors |
| **Error Handling** | Comprehensive exception management | Handles common errors | Basic try/catch | Poor error handling |
| **Code Quality** | Clean, documented, organized | Good structure | Acceptable organization | Poor organization |
| **User Experience** | Intuitive, helpful interface | Functional interface | Basic functionality | Confusing interface |

## 🏆 Extension Challenges

For advanced students, consider implementing:

1. **Persistent Statistics**: Save game data to files
2. **Multiplayer Network**: Allow games over network connections  
3. **GUI Interface**: Replace command-line with graphical interface
4. **Tournament Mode**: Multiple players, elimination brackets
5. **Card Animation**: Visual card reveals and movements
6. **Sound Effects**: Audio feedback for game events
7. **AI Players**: Computer opponents with different strategies

## 📞 Support & Resources

### Getting Help

1. **Check the launcher**: Run `python start_game.py` for environment diagnosis
2. **Review error messages**: The game provides detailed error information
3. **Test components individually**: Each module can be run standalone
4. **Verify internet connection**: The game requires API access

### Additional Resources

- **Python Requests Documentation**: <https://docs.python-requests.org/>
- **JSON Processing Guide**: <https://docs.python.org/3/library/json.html>
- **Command Line Interfaces**: <https://docs.python.org/3/library/cmd.html>
- **Deck of Cards API**: <https://deckofcardsapi.com/>

## 🎉 Conclusion

Congratulations on completing the Module 4 War Card Game project! You've successfully created a complete application that demonstrates professional-level API integration, error handling, and user interface design.

This project showcases your ability to:

- ✅ Work with external APIs reliably
- ✅ Handle complex application state  
- ✅ Create user-friendly interfaces
- ✅ Write maintainable, documented code
- ✅ Debug and troubleshoot issues

These skills are directly applicable to real-world software development, network automation, and system administration tasks.

## Well done! You're ready for advanced networking and automation challenges! 🚀

---

*FSCJ - Software Defined Networking Course*  
*Module 4: Python Requests Library*  
*Lab Project: War Card Game*
