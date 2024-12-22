### Bunny Game: A Fun Coding Exercise for Beginners 🐇🥕

---

## Introduction

Welcome to the **Bunny Game**, a beginner-friendly coding project designed to make learning Python fun and interactive! This project helps you explore the basics of programming by creating a simple game. It uses the **Tkinter** library to build graphical user interfaces (GUIs) and introduces key concepts like event handling, random movements, collision detection, and more.

### Why This Game Was Created

The Bunny Game was born from a desire to make coding relatable and exciting for my kids. They often asked me, *"What do you mean when you say you're coding?"* It was hard to explain my work in a way they could understand. One day, I decided to turn it into an opportunity for them to learn, saying:  
*"Let’s make a game together, and I’ll show you what code is and how it can bring your ideas to life."*  

Since my daughter loves bunnies, we chose to build a game with a bunny as the main character. The result? An engaging, easy-to-understand project where they could not only play but also see how the code worked and even improve it themselves.

---

## Features of the Bunny Game

- **Bunny**: A cute character that can be controlled using the arrow keys 🐇.
- **Carrot**: A sneaky carrot that moves randomly every second to "avoid" being caught 🥕.
- **Score Counter**: A counter at the top of the screen that keeps track of how many carrots the bunny has caught.

The Bunny Game teaches fundamental coding principles while encouraging creativity. You’ll learn how to set up the game, understand the code, and even modify it to create your own features.

---

## Step-by-Step Setup Guide

### Step 1: Install Python

Python is the programming language we’ll use to create and run the Bunny Game. Follow these steps to install Python on your computer:

1. **Download Python**:
   - Open your browser and visit the [official Python website](https://www.python.org).
   - Click the **Download Python** button. The website will suggest the correct version for your operating system (Windows, macOS, or Linux).

2. **Install Python**:
   - **Windows**:
     1. Open the downloaded file (e.g., `python-3.x.x.exe`).
     2. Check the box **Add Python to PATH** (this is very important!).
     3. Click **Install Now** and follow the instructions.
   - **macOS**:
     1. Open the downloaded `.pkg` file.
     2. Follow the prompts to install Python.
   - **Linux**:
     1. Python is often pre-installed. Check by typing the following command in the terminal:
        ```bash
        python3 --version
        ```
     2. If Python isn’t installed, use your package manager to install it:
        ```bash
        sudo apt-get install python3
        ```

3. **Verify the Installation**:
   - Open a terminal or command prompt.
   - Type:
     ```bash
     python --version
     ```
     or
     ```bash
     python3 --version
     ```
   - If you see a version number (e.g., `Python 3.10.x`), Python is installed correctly.

---

### Step 2: Install a Code Editor (Optional)

You can write and run Python code using just the terminal, but a code editor makes the process much easier. It provides features like syntax highlighting, error checking, and easier navigation of your code. Here are some beginner-friendly options:

1. **Thonny**:
   - A simple editor specifically designed for beginners.
   - [Download Thonny](https://thonny.org).

2. **VS Code**:
   - A powerful, flexible editor that supports many programming languages.
   - [Download VS Code](https://code.visualstudio.com).

3. **Notepad++** (My Recommendation):
   - I personally use Notepad++ because it’s simple, lightweight, and free.
   - [Download Notepad++](https://notepad-plus-plus.org/).

Choose the one that feels easiest for you to use.

---

### Step 3: Install Required Python Libraries

The Bunny Game requires two libraries:
1. **Tkinter**:
   - Tkinter comes pre-installed with Python and is used to create the game window and controls.
   - On most systems, you don’t need to install it separately. For Linux, you may need to install it with:
     ```bash
     sudo apt-get install python3-tk
     ```

2. **Pillow**:
   - Pillow handles the images (bunny and carrot) in the game.
   - To install Pillow, open a terminal or command prompt and type:
     ```bash
     pip install pillow
     ```

---

### Step 4: Set Up the Game Files

1. **Create a Folder**:
   - On your desktop, create a new folder named `BunnyGame`.

2. **Move the Files**:
   - Copy the following files into the `BunnyGame` folder:
     - `bunny.py` (the game script)
     - `bunny.png` (the bunny image)
     - `carrot.png` (the carrot image)

3. **Check the Folder**:
   - The folder should look like this:
     ```
     BunnyGame/
     ├── bunny.py
     ├── bunny.png
     └── carrot.png
     ```

---

### Step 5: Run the Bunny Game

1. **Open Command Prompt or Terminal**:
   - On Windows: Press `Win + R`, type `cmd`, and press Enter.
   - On macOS/Linux: Open the Terminal app.

2. **Navigate to the Game Folder**:
   - Use the `cd` command to move into the `BunnyGame` folder. For example:
     ```bash
     cd Desktop\BunnyGame
     ```

3. **Run the Game**:
   - Type the following command and press Enter:
     ```bash
     python bunny.py
     ```

4. **Play!**
   - The game window will open. Use the arrow keys to move the bunny and catch the carrot!

---

## How the Game Works

Here’s a quick breakdown of the gameplay:
1. **Bunny Movement**:
   - The bunny starts at the center of the screen and is controlled using the arrow keys.
2. **Carrot Movement**:
   - The carrot moves in random directions every second to avoid being caught.
3. **Score Counter**:
   - Every time the bunny catches the carrot, the score increases, and the carrot jumps to a new random position.

---


## Code Explanation
### 1. **Game Setup**
The game uses Python's `Tkinter` library to create a window and canvas for the game elements. Here's what happens:
- The **bunny** and **carrot** are represented by images loaded from your computer.
- The **canvas** is a 500x500 white background where the game takes place.

```python
self.canvas = tk.Canvas(root, width=500, height=500, bg='white')
```

### 2. **Controlling the Bunny**
The bunny moves in response to arrow key presses. Each key press updates the bunny's position on the canvas.

```python
self.root.bind("<Up>", self.move_up)
self.root.bind("<Down>", self.move_down)
self.root.bind("<Left>", self.move_left)
self.root.bind("<Right>", self.move_right)
```

The `move_up`, `move_down`, `move_left`, and `move_right` methods update the bunny's position and check for collisions with the carrot.

### 3. **Random Movement of the Carrot**
The carrot moves in a random direction every second using the `move_carrot_randomly` method. The `after` method schedules this action to happen repeatedly.

```python
self.root.after(1000, self.move_carrot_randomly)
```
### Understanding `random` and `randint` in the Bunny Game

The **`random`** module in Python is used to introduce randomness into the game. This makes the game more dynamic and fun by ensuring the carrot moves unpredictably. Here's how the `random` module, particularly the `randint` function, is used in the Bunny Game:

#### What is `random.randint`?
The `random.randint(a, b)` function generates a random integer between the values `a` and `b`, inclusive. For example:
```python
import random
print(random.randint(1, 10))  # Outputs a random integer between 1 and 10
```

#### How `random.randint` is Used in the Bunny Game
1. **Random Initial Carrot Position**:
   - When the game starts, the carrot is placed at a random position on the canvas using `random.randint` to generate x and y coordinates.
   - Example from the code:
     ```python
     self.carrot_x = random.randint(50, 450)
     self.carrot_y = random.randint(50, 450)
     ```
     This ensures the carrot starts somewhere within the canvas but not too close to the edges.

2. **Carrot Movement in Random Directions**:
   - The carrot moves randomly every second to avoid the bunny. The movement is determined by adding a random step (either -10, 0, or 10) to its current x and y coordinates:
     ```python
     dx = random.choice([-10, 0, 10])  # Random step in x direction
     dy = random.choice([-10, 0, 10])  # Random step in y direction
     ```
   - The random step is applied to both x and y coordinates, causing the carrot to move up, down, left, right, or stay in place.

3. **Resetting the Carrot's Position**:
   - When the bunny catches the carrot, `random.randint` is used again to place the carrot at a new random location:
     ```python
     self.carrot_x = random.randint(50, 450)
     self.carrot_y = random.randint(50, 450)
     ```

#### Why Use `random`?
Randomness makes the game more engaging and unpredictable, as the player cannot anticipate where the carrot will move next. It also introduces variety, making each game session unique.

---

### Experimenting with `random` in the Game
Encourage kids to modify the code and observe the effects:
1. **Change the Range**:
   - What happens if the range of `random.randint` is reduced (e.g., `random.randint(100, 400)`)?
   - Try adjusting the step size in the random movement.

2. **Use Other `random` Functions**:
   - Replace `random.choice([-10, 0, 10])` with `random.uniform(-10, 10)` for smoother movements.

3. **Add Random Obstacles**:
   - Use `random.randint` to generate random positions for obstacles and add them to the canvas.

Understanding and experimenting with `random` will help kids learn how to use randomness in programming to create exciting features in their projects!

### 4. **Collision Detection**
When the bunny gets close to the carrot (distance < 20), the `check_collision` method moves the carrot to a new random position and updates the score.

```python
if abs(self.bunny_x - self.carrot_x) < 20 and abs(self.bunny_y - self.carrot_y) < 20:
    self.update_score()
    self.move_carrot()
```

### 5. **Score Counter**
The score starts at 0 and increases by 1 every time the bunny catches the carrot. It is displayed at the top of the game window.

```python
self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16), bg="white")
```

---

## How to Play
1. Install Python and ensure you have the `Pillow` library installed (for image handling).
2. Save the bunny and carrot images to your computer and update the file paths in the code.
3. Run the code and use the arrow keys to move the bunny.
4. Try to catch the carrot as many times as possible while it moves around.

---

## Challenge: Make It Your Own!
This game is just the beginning. Here are some ideas for extending and improving the game:
- **Add a Timer**: Limit the time and see how many carrots you can catch before time runs out.
- **Obstacle Course**: Add obstacles that the bunny needs to avoid.
- **Levels**: Increase the carrot's speed as the score goes up to make the game more challenging.
- **Sound Effects**: Play a sound whenever the bunny catches the carrot.
- **Customize Graphics**: Replace the bunny and carrot with your favorite characters.

---

## Learning Outcomes
By working on this project, kids will:
1. Learn the basics of Python programming.
2. Understand how to create a GUI using `Tkinter`.
3. Explore key coding concepts like event handling, loops, and randomization.
4. Practice debugging and modifying code to see immediate results.

---

### Have Fun Coding! 🚀
This project is all about creativity and learning. Whether you stick with the basics or add cool new features, enjoy the process of turning ideas into reality!

