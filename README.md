

---

# Bunny Game: A Fun Coding Exercise for Kids 🐇🥕

## Introduction
This project is a simple **Python game** designed as a learning exercise for kids to explore the basics of coding. It uses the `Tkinter` library for creating graphical user interfaces (GUIs) and introduces concepts like event handling, random movements, and collision detection.

The game features:
- A bunny controlled by arrow keys 🐇
- A carrot that moves randomly to avoid the bunny 🥕
- A score counter to track how many times the bunny catches the carrot

The goal is to expose kids to coding in a fun and engaging way, while also encouraging them to think creatively and make their own modifications to the game.
---
### How to Install Python: A Beginner's Guide

If you're new to coding, the first step is to install Python on your computer. Python is the programming language used to create the Bunny Game. Follow these simple steps to get started:

---

### Step 1: Download Python
1. Open your web browser and go to the official Python website: [https://www.python.org](https://www.python.org).
2. Click on the **Download Python** button. The website will automatically suggest the right version for your operating system (Windows, macOS, or Linux).

---

### Step 2: Install Python
#### For Windows:
1. Open the downloaded file (e.g., `python-3.x.x.exe`).
2. Check the box **Add Python to PATH** (this is very important!).
3. Click **Install Now** and wait for the installation to complete.
4. Once installed, click **Close**.

#### For macOS:
1. Open the downloaded `.pkg` file.
2. Follow the prompts to install Python on your system.
3. Once installed, Python will be available in your Applications folder or through the terminal.

#### For Linux:
1. Most Linux distributions come with Python pre-installed. You can check by opening a terminal and typing:
   ```bash
   python3 --version
   ```
2. If Python is not installed, use your package manager to install it. For example:
   ```bash
   sudo apt-get install python3
   ```

---

### Step 3: Verify the Installation
To ensure Python is installed correctly:
1. Open a terminal or command prompt:
   - On Windows: Press `Win + R`, type `cmd`, and press Enter.
   - On macOS/Linux: Open the Terminal app.
2. Type the following command and press Enter:
   ```bash
   python --version
   ```
   or
   ```bash
   python3 --version
   ```
3. You should see a version number (e.g., `Python 3.x.x`). This confirms Python is installed.

---

### Step 4: Install a Code Editor (Optional)
While Python can be written and run in a terminal, using a code editor makes things easier. Here are two beginner-friendly options:
1. **Thonny**:
   - A simple Python IDE designed for beginners.
   - Download it from [https://thonny.org](https://thonny.org).
2. **VS Code**:
   - A powerful code editor with Python support.
   - Download it from [https://code.visualstudio.com](https://code.visualstudio.com).

---

### Step 5: Install Required Libraries
For the Bunny Game, you’ll need the `Pillow` library. Once Python is installed, open a terminal or command prompt and type:
```bash
pip install pillow
```

---

### You're Ready to Code!
With Python installed, you can now run the Bunny Game and explore coding. Follow the instructions in this guide to set up the game and have fun learning! 🚀

---


---
### Required Python Libraries

Before running the game, make sure you have the following Python libraries installed. These libraries are necessary for the game to work correctly:

1. **Tkinter** (Built-in with Python)
   - Tkinter is the standard GUI library included with Python. It is used to create the game window and handle user interactions.
   - You don't need to install it separately if you have Python installed. However, on some Linux distributions, you may need to install it using your package manager:
     ```bash
     sudo apt-get install python3-tk
     ```

2. **Pillow** (PIL - Python Imaging Library)
   - Pillow is used to handle the bunny and carrot images in the game.
   - Install it using `pip`:
     ```bash
     pip install pillow
     ```

### Installation Instructions
1. Open a terminal or command prompt.
2. Run the following command to ensure `Pillow` is installed:
   ```bash
   pip install pillow
   ```
3. If you're using Linux and encounter issues with Tkinter, install it using your package manager as shown above.

### Verifying the Installation
To verify the required libraries are installed, try running the following Python script:

```python
import tkinter
from PIL import Image, ImageTk

print("Tkinter and Pillow are installed correctly!")
```

If no errors appear, you're good to go! If there are errors, double-check the installation steps above.


### Setting Up the Bunny Game: Ensuring the `.png` Files and Script Are in the Same Folder

To run the Bunny Game correctly, it’s important to ensure the `.png` image files (for the bunny and carrot) and the Python script (`bunny.py`) are stored in the same folder. Here’s how to do it step-by-step:

---

### Step 1: Create a Folder for the Bunny Game
1. **On Your Desktop**:
   - Right-click on an empty area of your desktop and select **New > Folder**.
   - Name the folder something like `BunnyGame`.
   
2. **Move Your Files**:
   - Copy the `bunny.png`, `carrot.png`, and `bunny.py` files into this folder.
   - You should now have all three files inside the `BunnyGame` folder:
     ```
     BunnyGame/
     ├── bunny.py
     ├── bunny.png
     └── carrot.png
     ```

---

### Step 2: Navigate to the Folder Using Command Prompt (cmd)
To run the game, you need to use the command prompt to navigate to the folder where your files are stored.

1. **Open the Command Prompt**:
   - Press `Win + R`, type `cmd`, and hit Enter.

2. **Navigate to the Folder**:
   - Use the `cd` (change directory) command to navigate to the `BunnyGame` folder on your desktop. Here's how:
     ```bash
     cd Desktop\BunnyGame
     ```
   - If successful, your command prompt should now show:
     ```
     C:\Users\YourUsername\Desktop\BunnyGame>
     ```

3. **Verify Your Files Are There**:
   - Type `dir` and press Enter (Windows) or `ls` (Mac/Linux). You should see the following files listed:
     ```
     bunny.py
     bunny.png
     carrot.png
     ```

---

### Step 3: Start the Python Game
Once you're in the correct folder, you can start the game with the following command:
```bash
python bunny.py
```
This will run the `bunny.py` script, and the game window should open.

---

### Troubleshooting
- **Error: `'python' is not recognized`**:
   - This means Python is not added to your system's PATH. During installation, ensure you check the box **Add Python to PATH**. If you missed this step, you may need to reinstall Python or manually add it to PATH.
   - Alternatively, try using `python3` instead of `python`:
     ```bash
     python3 bunny.py
     ```

- **Error: File Not Found**:
   - Ensure the `bunny.png` and `carrot.png` files are in the same folder as `bunny.py`. Double-check the file paths and folder location.

---

### Tips for Ease of Use
1. **Stick to the Desktop**:
   - Keeping the `BunnyGame` folder on the desktop makes it easier to find and navigate to using `cd`.

2. **Practice Using `cd` Commands**:
   - `cd ..`: Go back one folder.
   - `cd folder_name`: Move into a folder.
   - Use `dir` or `ls` to list the contents of the current folder.

3. **Double-Check Filenames**:
   - Ensure the filenames are exactly `bunny.py`, `bunny.png`, and `carrot.png`. File extensions matter!

---

---

## How the Game Works
1. The **bunny** starts at the center of the screen and is controlled using the arrow keys (Up, Down, Left, Right).
2. The **carrot** appears at a random position and moves in random directions every second.
3. If the bunny gets close enough to the carrot, the carrot "gets caught," and the score increases.
4. The carrot then moves to a new random position, and the game continues.

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

