# WordleBot

WordleBot is a Python tool to help you solve Wordle puzzles by suggesting valid English words based on your current knowledge of the puzzle.

## Features

- Set known letters at specific positions.
- Specify letters that must be included in the word (as a string or list).
- Remove invalid letters from possible guesses (as a string or list).
- Generate all valid English words matching the current constraints.

## Requirements

- Python 3.x
- `pyenchant` library

Install dependencies with pip

## Usage

1. **Import and Initialize:**
    ```python
    from wordleCheat import WordleBot
    bot = WordleBot()
    ```

2. **Set Known Letters:**
    Set a known letter at a specific position (0-based index).
    ```python
    bot.set_known_letter('e', 1)  # Sets 'e' at position 1
    ```

3. **Set Included Letters:**
    Specify letters that must be present in the word. You can pass a string (e.g., `'ih'`) or a list (e.g., `['i', 'h']`).
    ```python
    bot.set_include_letters('ih')
    # or
    bot.set_include_letters(['i', 'h'])
    ```

4. **Remove Invalid Letters:**
    Remove letters you know are not in the word. You can pass a string (e.g., `'eroasgcn'`) or a list (e.g., `['e', 'r', 'o', 'a', 's', 'g', 'c', 'n']`).
    ```python
    bot.remove_invalid_letters('eroasgcn')
    # or
    bot.remove_invalid_letters(['e', 'r', 'o', 'a', 's', 'g', 'c', 'n'])
    ```

5. **Find Valid Words:**
    Get a list of all valid words matching the constraints.
    ```python
    valid_words = bot.find_all_valid_words()
    print(valid_words)
    ```

## Example

```python
from wordleCheat import WordleBot

bot = WordleBot()
bot.set_include_letters('ih')
bot.remove_invalid_letters('eroasgcn')
valid_words = bot.find_all_valid_words()
print(valid_words)# WordleBot
