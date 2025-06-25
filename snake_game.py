#SNAKE GAME 
#import libraries
from tkinter import *
import random

#constant variables for the game 
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
SPEED = 120
BODY_PARTS = 3
SNAKE_COLOR = "#00F000"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

#abstract class game object
class GameObject:
    def __init__(self, canvas):
        self._canvas = canvas 

    def draw(self):
        raise NotImplementedError("Must be implemented in subclass")
    
#snake class inheriting from game object
class Snake(GameObject):
    def __init__(self, canvas):
        super().__init__(canvas)
        self.body_size = BODY_PARTS
        self.coordinates = [[0,0] for _ in range(self.body_size)] 
        self.squares = [] #store canvas rectangles
        self._create_body() 

    def _create_body(self):
        for x, y in self.coordinates:
            square = self._canvas.create_rectangle(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "snake")
            self.squares.append(square)

    def move(self,direction):
        #get current position
        x, y = self.coordinates[0]

        #update position base on direction
        if direction == "up":
            y -= SPACE_SIZE
        elif direction == "down":
            y += SPACE_SIZE
        elif direction == "left":
            x -= SPACE_SIZE
        elif direction == "right":
            x += SPACE_SIZE
        
        #inserts new head to the front
        self.coordinates.insert(0,[x,y])
        square = self._canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR)
        self.squares.insert(0, square)

    def remove_tail(self):
        self._canvas.delete(self.squares[-1])
        del self.squares[-1]
        del self.coordinates[-1]

#food class inheriting from game object
class Food(GameObject):
    def __init__(self,canvas):
        super().__init__(canvas)
        self.coordinates = self._random_position()
        self.square = self.draw()

    def _random_position(self):
        #randomly choose a position aligned to the grid
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1 ) * SPACE_SIZE
        y = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1 ) * SPACE_SIZE
        return [x ,y]
    
    def draw(self):
        x, y = self.coordinates
        return self._canvas.create.oval(x, y , x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "food")
    
#game class for handling logi and GUI 
class Game:
    def __init__(self):
        self.window = Tk()
        self.window.title("Snake Game OOP")
        self.window.resizable(False, False)

        #Center window screen
        screen_width = self.window.winfo_screenwidth
        screen_height = self.window.winfo_screenheight
        x = int((screen_width / 2) - (GAME_WIDTH / 2))
        y = int((screen_height / 2) - (GAME_HEIGHT / 2))
        self.window.geometry(f"{GAME_WIDTH} x {GAME_HEIGHT} + {x} + {y}")

        self.canvas = Canvas(self.window, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)    
        self.canvas.pack()

        self.score = 0 
        self.score_text = self.canvas.create_text(GAME_WIDTH / 2, 20, text = f"Score: {self.score}", fill ="white", font = ("consolas", 20)) #displays score

        #initial direction
        self.direction = "down"

        #create snake and food 
        self.snake = Snake(self.canvas)
        self.food = Food(self.canvas)

        #bind arrow keys to control snake
        self.window.bind("<Left>", self.turn_left)
        self.window.bind("<RIght>", self.turn_right)
        self.window.bind("<Up>", self.turn_up)
        self.window.bind("<Down>", self.turn_down)

        self._update()
        self.window.mainloop()

    def _update(self):
        self.snake.move(self.direction)

        if self.snake.coordinates[0] == self.food.coordinates:
            self.score += 1 
            self.canvas.delete("food") 
            self.food = Food(self.canvas)
            self.canvas.itemconfig(self.score_text, text = f"Score: {self.score}")   
        else: 
            self.snake.remove_tail()

        #check for collision
        if self.check_collision():
            self.game_over()
        else:
            self.window.after(SPEED, self._update())

    def check_collision(self):
        x, y = self.snake.coordinates[0]

        #checks wall collision
        if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
            return True
        #check self collision
        for segment in self.snake.coordinates[1:]:
            if segment == [x, y]:
                return True
        return False            
    
    #Arrow key events
    def turn_left(self,event):
        if self.direction != "right":
            self.direction = "left"

    def turn_right(self, event):
        if self.direction != "left":
            self.direction = "right"

    def turn_up(self,event):
        if self.direction != "down":
            self.direction = "up"

    def turn_down(self,event):
        if self.direction != "up":
            self.direction = "down"
