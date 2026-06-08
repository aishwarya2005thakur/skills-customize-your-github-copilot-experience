
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a console Hangman game in Python that practices string manipulation, loops, conditionals, and basic input validation.

## 📝 Tasks

### 🛠️ Core Game

#### Description
Implement the Hangman game mechanics: select a word at random, accept single-letter guesses, reveal correct letters, track remaining attempts, and end the game with a clear win or loss message.

#### Requirements
Completed program should:

- Choose a word at random from a predefined list.
- Prompt the user for single-letter guesses and validate input (single alphabetic character).
- Display current progress using underscores and revealed letters (for example: `_ a _ _ e`).
- Track and display the number of incorrect attempts remaining.
- End the game when the word is fully guessed or when attempts reach zero and display a win/lose message.

### 🛠️ Extra Features (Optional)

#### Description
Add one or more optional improvements to practice additional skills and make the game more user-friendly.

#### Requirements
Completed program may include any of the following:

- Allow full-word guesses in addition to single-letter guesses.
- Show a list of previously guessed letters.
- Load the word list from a `data/words.txt` file if present.
- Organize code using functions and include basic docstrings.

## Example

Input/Output (example session):

```
Welcome to Hangman!
Word: _ _ _ _ _
Guess a letter: a
Correct! Word: _ a _ _ _
Attempts left: 6
Guess a letter: e
Incorrect. Attempts left: 5
...
```

Follow the project template in `templates/assignment-template.md` when creating or editing assignment files.
