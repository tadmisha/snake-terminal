*ChatGPT Generated*

# Terminal Snake 🐍

A classic Snake game implemented in Python for the terminal!  
Use `WASD` or the arrow keys to control the snake. Eat apples, grow longer, and avoid crashing into yourself!

---

## 🎮 Features

- Real-time keyboard input using `pynput`
- Smooth frame updates and snake movement
- Apple spawns randomly on the grid
- Terminal-based visual rendering
- Game-over detection on self-collision
- Configurable map size and frame rate

---

## 🧰 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
```
pynput
numpy
opencv-python
```

---

## ▶️ How to Run

```bash
python main.py
```

Make sure to run the script **in a terminal**, not an IDE — for best input behavior.

---

## 🕹️ Controls

| Key         | Action        |
|-------------|---------------|
| W / ↑       | Move Up       |
| A / ←       | Move Left     |
| S / ↓       | Move Down     |
| D / →       | Move Right    |
| Q / Esc     | Quit Game     |

---

## 📦 Project Structure

```
terminal-snake/
├── ascii_videos/        # (empty) folder used in future plans
├── main.py              # main game logic
├── requirements.txt     # required dependencies
└── README.md            # project description and instructions
```

---

## 📌 Notes

- The game wraps around the screen when hitting walls.
- You cannot reverse direction immediately (e.g. Right → Left).
- Pressing `Q` or `Esc` exits the game cleanly.
- The game prints a new frame in each cycle, so use a terminal that can handle fast output without lag.

---

## 🧠 Inspiration

This project is a fun way to practice Python fundamentals like:

- Grid representation
- Realtime input handling
- State updates and loops
- Terminal rendering logic

---

Enjoy the game!