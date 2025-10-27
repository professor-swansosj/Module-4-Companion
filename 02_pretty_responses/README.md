# 02: Making Data Beautiful

## 🎯 Mission

Transform raw API responses into readable, formatted output that actually makes sense! Learn to convert JSON responses into Python dictionaries and present data beautifully.

## 🎖 Goals

- [ ] Convert API response text to Python dictionaries using `.json()`
- [ ] Use `json.dumps()` with `indent=4` to pretty print JSON data
- [ ] Make your Dad Jokes output more readable and professional
- [ ] Format your Deck of Cards data to see the structure clearly

## 💡 Hints

### JSON is Your Friend

- Raw API responses are often hard to read
- Use `response.json()` to convert to a Python dictionary
- Then use `json.dumps(data, indent=4)` to make it pretty!

### The Pattern

```python
response = requests.get('api-url')
data = response.json()  # Convert to dictionary
print(json.dumps(data, indent=4))  # Pretty print
```

**Make It Professional**
Instead of printing raw text, present the data clearly with labels and formatting.

## 🚀 Ready to Code?

**Start with `pretty_dad_jokes.py`** - make those jokes look professional!
**Then enhance `pretty_deck_cards.py`** - see the card data structure clearly!

**You're building real programming skills!** 🎨