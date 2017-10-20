""" Snake game for codeskulptor.org """

import simplegui
import random


class Snake(object):

    def __init__(self):
        self.pos = {'x': 10, 'y': 10}
        self.vel = {'x': 1, 'y': 0}
        self.long = 1
        self.listaCuadrados = [Square((self.pos['x'], self.pos['y']), 9)]
        self.keyDict = {37: self.left, 38: self.up, 39: self.right, 40: self.down}
        self.estado = None
        self.keyDict[39]()

    def draw(self, canvas):
        for cuadrado in self.listaCuadrados:
            cuadrado.draw(canvas)

    def actualize(self):
        self.pos['x'] += self.vel['x']
        self.pos['y'] += self.vel['y']
        self.listaCuadrados = [Square((self.pos['x'], self.pos['y']), 9)]

    def left(self):
        if self.estado != "right":
            self.vel = {'x': -1, 'y': 0}
            self.estado = "left"

    def right(self):
        if self.estado != "left":
            self.vel = {'x': 1, 'y': 0}
            self.estado = "right"

    def up(self):
        if self.estado != "down":
            self.vel = {'x': 0, 'y': -1}
            self.estado = "up"

    def down(self):
        if self.estado != "up":
            self.vel = {'x': 0, 'y': 1}
            self.estado = "down"


class Square(object):

    def __init__(self, pos, width):
        self.pos = pos
        self.width = width
        x = pos[0]-1
        y = pos[1]-1
        self.lista = [(x, y), (x + self.width, y),
                      (x + self.width, y + self.width), (x, y + self.width)]

    def draw(self, canvas):
        canvas.draw_polygon(self.lista, 1, 'white', 'white')


class Scenario(object):
    def __init__(self, width, height):
        self.chips = [Square((random.randrange(width), random.randrange(height)), 3) for _ in range(20)]

    def draw(self, canvas):
        for chip in self.chips:
            chip.draw(canvas)




# Handler for mouse click
def start():
    # Start the frame animation
    frame.start()
    timer = simplegui.create_timer(50, actualize)
    frame.set_keydown_handler(keyDown)
    timer.start()


def keyDown(key):

    print(key)
    try:
        snake.keyDict[key]()
    except:
        if key == 27:
            exit()



# Handler to draw on canvas
def draw(canvas):
    snake.draw(canvas)
    scenario.draw(canvas)

def actualize():
    snake.actualize()


width = 620
height = 480
snake = Snake()
scenario = Scenario(width, height)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.add_button("Start", start)
frame.set_draw_handler(draw)
