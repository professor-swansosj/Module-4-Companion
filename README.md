# Module 4: The Python Requests Library

## Software Defined Networking - Network Automation Course

### FSCJ Computer Science Department

---

## 📚 Module Overview

Welcome to Module 4 of the Software Defined Networking course! This module focuses on the **Python Requests Library** and teaches you how to interact with APIs programmatically. You'll learn essential skills for network automation by mastering HTTP requests and response handling.

### 🎯 Learning Objectives

By the end of this module, you will be able to:

- Understand the fundamentals of the Python Requests library
- Create and send various types of HTTP requests (GET, POST, PUT, DELETE)
- Handle and parse API responses effectively
- Convert JSON responses to Python dictionaries
- Process different data formats (JSON, XML, CSV, YAML)
- Apply these skills in a practical project (War Card Game)

### 📋 Prerequisites

- Linux+ certification knowledge
- Introduction to Python (completed)
- Cisco 1, 2, 3 courses (completed)
- Basic understanding of HTTP protocols
- Python environment setup

---

## 📖 Table of Contents

### Theory and Examples

1. [Introduction to Requests](#1-introduction-to-requests)
2. [Creating a Request](#2-creating-a-request)
3. [Sending Requests](#3-sending-requests)
4. [Viewing Response](#4-viewing-response)
5. [Converting JSON Response to Python Dictionary](#5-converting-json-response-to-python-dictionary)
6. [Parsing the Response](#6-parsing-the-response)

### Hands-On Labs

7. [Lab: War Card Game Project](#7-lab-war-card-game-project)
8. [Practice Exercises](#8-practice-exercises)

---

## 🗂️ Repository Structure

```bash
Module-4-Companion/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── examples/                    # Step-by-step code examples
│   ├── 01_introduction.py      # Basic requests introduction
│   ├── 02_creating_requests.py # How to create requests
│   ├── 03_sending_requests.py  # Sending different request types
│   ├── 04_viewing_responses.py # Response handling
│   ├── 05_json_conversion.py   # JSON to Python dict
│   └── 06_parsing_responses.py # Advanced parsing techniques
├── labs/                       # Main lab projects
│   ├── war_card_game/          # War card game implementation
│   │   ├── war_game.py         # Main game file
│   │   ├── card_api.py         # API interaction module
│   │   └── game_logic.py       # Game mechanics
│   └── practice_exercises/     # Additional practice
├── data/                       # Sample data files
│   ├── sample_api_responses/   # Example API responses
│   ├── network_devices.json    # Network device data
│   ├── config_templates.yaml   # Configuration templates
│   ├── device_inventory.csv    # Device inventory
│   └── network_topology.xml    # Network topology data
└── resources/                  # Additional learning materials
    ├── api_reference.md        # Quick API reference
    ├── troubleshooting.md      # Common issues and solutions
    └── further_reading.md      # Additional resources
```

---

## 🚀 Getting Started

### Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/professor-swansosj/Module-4-Companion.git
   cd Module-4-Companion
   ```

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Test your setup:**

   ```bash
   python examples/01_introduction.py
   ```

### Follow Along with the Video

During the instructional video, you'll be guided through:

- Each example in the `examples/` directory
- Progressive skill building from basic to advanced concepts
- Hands-on coding exercises
- The final War Card Game project

---

## 📝 Module Sections

### 1. Introduction to Requests

**Location:** `examples/01_introduction.py`

- What is the Requests library?
- Installation and import
- Basic concepts and terminology
- Your first API call

### 2. Creating a Request

**Location:** `examples/02_creating_requests.py`

- Request methods (GET, POST, PUT, DELETE)
- Adding headers and parameters
- Authentication methods
- Request customization

### 3. Sending Requests

**Location:** `examples/03_sending_requests.py`

- Making synchronous requests
- Handling timeouts
- Error handling and exceptions
- Best practices for network requests

### 4. Viewing Response

**Location:** `examples/04_viewing_responses.py`

- Response object properties
- Status codes and their meanings
- Headers analysis
- Response content types

### 5. Converting JSON Response to Python Dictionary

**Location:** `examples/05_json_conversion.py`

- Understanding JSON format
- `.json()` method
- Error handling for malformed JSON
- Working with nested JSON structures

### 6. Parsing the Response

**Location:** `examples/06_parsing_responses.py`

- Advanced parsing techniques
- Handling different data formats
- Data extraction and manipulation
- Real-world parsing scenarios

### 7. Lab: War Card Game Project

**Location:** `labs/war_card_game/`

- **Objective:** Build a complete War card game using API calls
- **Skills Applied:** All module concepts in a practical project
- **API Used:** Deck of Cards API (<https://deckofcardsapi.com/>)
- **Features:**
  - Create and shuffle card decks via API
  - Draw cards for players
  - Implement War game logic
  - Handle game state and scoring
  - Error handling and user experience

### 8. Practice Exercises

**Location:** `labs/practice_exercises/`

- Network device API interactions
- Configuration management via APIs
- Data format conversions
- Mini-projects for skill reinforcement

---

## 🎮 War Card Game - Main Lab Project

The War Card Game is the culminating project for this module. It demonstrates practical application of all concepts learned:

**Game Features:**

- Two-player card game simulation
- API-driven card deck management
- Real-time game state updates
- Score tracking and win conditions
- Clean, user-friendly interface

**Technical Skills Demonstrated:**

- API integration and error handling
- JSON data manipulation
- Object-oriented programming
- Game logic implementation
- User input validation

---

## 📊 Sample Data Files

The `data/` directory contains various sample files to practice with:

- **JSON Files:** Network device configurations, API responses
- **YAML Files:** Configuration templates, deployment specs
- **CSV Files:** Device inventories, performance metrics
- **XML Files:** Network topology data, configuration exports

These files simulate real-world network automation scenarios you'll encounter in your career.

---

## 🔧 Tools and Technologies

- **Python 3.7+**
- **Requests library**
- **JSON/YAML/CSV/XML parsing libraries**
- **Git for version control**
- **VS Code or preferred IDE**

---

## 📚 Additional Resources

- **API Reference:** Quick reference for common API patterns
- **Troubleshooting Guide:** Solutions to common issues
- **Further Reading:** Links to advanced topics and documentation

---

## 🤝 Getting Help

If you encounter issues during the module:

1. Check the troubleshooting guide in `resources/troubleshooting.md`
2. Review the example code carefully
3. Test each section step by step
4. Ask questions during class or office hours

---

## 📝 Assessment

This module contributes to your understanding of:

- Network automation principles
- API integration skills
- Python programming proficiency
- Real-world problem solving

The War Card Game project will be part of your practical assessment for this module.

---

**Happy Learning! 🚀**

*Remember: The goal is not just to make API calls, but to understand how these skills apply to network automation and software-defined networking in your future career.*
