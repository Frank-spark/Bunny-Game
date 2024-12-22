import tkinter as tk
from PIL import Image, ImageTk
import random

class BunnyGame:
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("Bunny Game")
        self.canvas = tk.Canvas(root, width=500, height=500, bg='green')
        self.canvas.pack()
        
        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 16), bg="white")
        self.score_label.pack()

        # Load the bunny image
        self.bunny_image = Image.open(r"C:\Users\nfj76\Desktop\bunny.png")
        self.bunny_photo = ImageTk.PhotoImage(self.bunny_image)

        # Load the carrot image
        self.carrot_image = Image.open(r"C:\Users\nfj76\Desktop\carrot.png")
        self.carrot_photo = ImageTk.PhotoImage(self.carrot_image)

        # Initialize bunny position and add image to canvas
        self.bunny_x = 250
        self.bunny_y = 250
        self.bunny = self.canvas.create_image(self.bunny_x, self.bunny_y, image=self.bunny_photo)

        # Initialize carrot position and add to canvas
        self.carrot_x = random.randint(50, 450)
        self.carrot_y = random.randint(50, 450)
        self.carrot = self.canvas.create_image(self.carrot_x, self.carrot_y, image=self.carrot_photo)

        # Bind arrow keys for movement
        self.root.bind("<Up>", self.move_up)
        self.root.bind("<Down>", self.move_down)
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        self.move_carrot_randomly()
        
    def move_carrot_randomly(self):
        # Move the carrot in a random direction
        dx = random.choice([-20, 0, 20])  # Random step in x direction
        dy = random.choice([-20, 0, 20])  # Random step in y direction

        # Update carrot position
        self.carrot_x = max(20, min(490, self.carrot_x + dx))
        self.carrot_y = max(20, min(490, self.carrot_y + dy))
        self.canvas.coords(self.carrot, self.carrot_x, self.carrot_y)

        # Schedule the next movement
        self.root.after(200, self.move_carrot_randomly)
    def move_up(self, event):
        # Move the bunny up
        if self.bunny_y > 10:
            self.bunny_y -= 10
            self.canvas.coords(self.bunny, self.bunny_x, self.bunny_y)
            self.check_collision()

    def move_down(self, event):
        # Move the bunny down
        if self.bunny_y < 490:
            self.bunny_y += 10
            self.canvas.coords(self.bunny, self.bunny_x, self.bunny_y)
            self.check_collision()

    def move_left(self, event):
        # Move the bunny left
        if self.bunny_x > 10:
            self.bunny_x -= 10
            self.canvas.coords(self.bunny, self.bunny_x, self.bunny_y)
            self.check_collision()

    def move_right(self, event):
        # Move the bunny right
        if self.bunny_x < 490:
            self.bunny_x += 10
            self.canvas.coords(self.bunny, self.bunny_x, self.bunny_y)
            self.check_collision()

    def move_carrot(self):
        # Move the carrot to a new random position
        self.carrot_x = random.randint(50, 450)
        self.carrot_y = random.randint(50, 450)
        self.canvas.coords(self.carrot, self.carrot_x, self.carrot_y)

    def check_collision(self):
        # Check if the bunny is close to the carrot
        if abs(self.bunny_x - self.carrot_x) < 20 and abs(self.bunny_y - self.carrot_y) < 20:
            self.update_score()
            self.move_carrot()
            
    def update_score(self):
        # Increment the score and update the label
        self.score += 1
        self.score_label.config(text=f"Score: {self.score}")        

# Create the main window and pass it to the BunnyGame class
root = tk.Tk()
app = BunnyGame(root)
root.mainloop()
