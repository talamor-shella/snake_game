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
#game class for handling logi and GUI 
