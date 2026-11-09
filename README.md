# Guess the Password
#This README was written by me and then put in to claude to make it in to a markdown type and organize it.

## What the app is about

Guess the Password is a small web game built with Python and Flet. A secret password is hidden, and the player has 10 guesses to find it. Every wrong guess costs one heart. If the hearts run out, the player dies. If the player guesses the password, the whole page turns into a party.

## Core features

- **Guessing game:** type a guess into the input box in the middle of the page and press Enter or click **Guess**.
- **10 lives:** a row of hearts shows how many guesses are left, and a message tells the player after each wrong guess.
- **Death screen:** after the 10th wrong guess the screen goes black and shows "YOU DIED 💀".
- **Party mode:** a correct guess starts an animation where the background and title colors change every fraction of a second and party emojis shuffle around the page.
- **Play again:** a button resets the game after a win or a loss.
- **Forgiving input:** guesses are not case-sensitive, and extra spaces at the start or end are ignored.
- **Empty guesses don't count:** pressing Enter on a blank box does not use up a guess.

## Dependencies

- Python 3.10 or newer
- [Flet](https://flet.dev) (installs the web and desktop parts with it)

The other imports, `asyncio` and `random`, are part of Python and need no installation.

Install Flet inside a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "flet[all]"
```

## How to run the code

1. Open a terminal in the project folder.
2. Activate the virtual environment (do this again every time you open a new terminal):
   ```bash
   source .venv/bin/activate
   ```
3. Start the game in your browser:
   ```bash
   flet run --web password_game.py
   ```
4. To open it in a desktop window instead, run `flet run password_game.py`.
5. Press `Ctrl+C` in the terminal to stop it.

## Extra sources

- Flet documentation (https://flet.dev/docs) for the controls, layout, and events
- Python documentation for `asyncio` (the animation timing) and `random` (random colors and emojis)

## Easter eggs

- There is a hidden message somewhere on the guessing screen. It matches the background color, so you can only find it by selecting text with your mouse. (Top left cornor, your cursor will change its shape so you know you're on it.)
- During the party, the colors and emojis are picked at random, so no two parties look the same.

## Project files

```
password_game.py   the game
README.md          this file
.gitignore         files git should ignore (.venv, .env, etc.)
```