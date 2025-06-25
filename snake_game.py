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

    

#food class inheriting from game object
#game class for handling logi and GUI 
