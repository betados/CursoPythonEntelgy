""" Snake game for codeskulptor.org """

import simplegui
import random


class Snake(object):

    def __init__(self):
        self.pos = {'x': 10, 'y': 10}
        self.vel = {'x': 1, 'y': 0}
        self.long = 1
        self.lista = [(self.pos['x'], self.pos['y'])]
        self.listaCuadrados = []
        self.add()
        self.createSquares()
        self.keyDict = {37: self.left, 38: self.up, 39: self.right, 40: self.down}
        self.estado = None
        self.keyDict[39]()

    def createSquares(self):
        for element in self.lista:
            self.listaCuadrados = [Square(element, 9)]

    def add(self):
        self.lista.append((self.lista[-1][0]+10, self.lista[-1][0]))

    def draw(self, canvas):
        for element in self.lista:
            Square(element, 9).draw(canvas)
        # for cuadrado in self.listaCuadrados:
        #     cuadrado.draw(canvas)

    def actualize(self):
        self.lista[0] = self.lista[0][0] + self.vel['x'], self.lista[0][1] + self.vel['y']


        # self.pos['x'] += self.vel['x']
        # self.pos['y'] += self.vel['y']
        # for cuadrado in self.listaCuadrados:
        #     cuadrado.pos(self.pos['x'], self.pos['y'])

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

    def __init__(self, pos, width, color='Blue'):
        # self.pos = pos
        self.color = color
        self.width = width
        x = pos[0]-1
        y = pos[1]-1
        self.lista = []
        self.pos(x, y)


    def draw(self, canvas):
        canvas.draw_polygon(self.lista, 1, self.color, self.color)

    def pos(self, x, y):
        self.lista = [(x, y), (x + self.width, y),
                      (x + self.width, y + self.width), (x, y + self.width)]


class Scenario(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.chips = [(random.randrange(0, width, 10)+5, random.randrange(0, height, 10)+5) for _ in range(20)]
        self.lightGreen = [Square((x+10*(y%20==0), y), 10, 'GreenYellow ') for x in range(width) if x%20 == 0 for y in range(height) if y%10==0]
        self.backGround = Square((0, 0), width, 'DarkKhaki')

    def draw(self, canvas):
        self.backGround.draw(canvas)
        for square in self.lightGreen:
            square.draw(canvas)
        for chip in self.chips:
            canvas.draw_circle(chip, 4, 1, 'Red', 'Red')


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
    # scenario.draw(canvas)
    snake.draw(canvas)

def actualize():
    snake.actualize()


width = 320
height = 240
snake = Snake()
scenario = Scenario(width, height)

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", width, height)
frame.add_button("Start", start)
frame.set_draw_handler(draw)
