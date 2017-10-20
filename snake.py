""" Snake game for codeskulptor.org """

import simplegui


class Snake(object):

    def __init__(self):
        self.pos = {'x': 10, 'y': 10}
        self.vel = {'x': 1, 'y': 0}
        self.long = 1
        self.listaCuadrados = [Cuadrado((self.pos['x'], self.pos['y']))]
        self.keyDict = {37: self.left, 38: self.up, 39: self.right, 40: self.down}
        self.estado = None
        self.keyDict[39]()

    def draw(self, canvas):
        for cuadrado in self.listaCuadrados:
            cuadrado.draw(canvas)

    def actualize(self):
        self.pos['x'] += self.vel['x']
        self.pos['y'] += self.vel['y']
        self.listaCuadrados = [Cuadrado((self.pos['x'], self.pos['y']))]

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


class Cuadrado(object):
    ancho = 9

    def __init__(self, pos):
        self.pos = pos
        x = pos[0]-1
        y = pos[1]-1
        self.lista = [(x, y), (x + Cuadrado.ancho, y),
                      (x + Cuadrado.ancho, y + Cuadrado.ancho), (x, y + Cuadrado.ancho)]

    def draw(self, canvas):
        canvas.draw_polygon(self.lista, 1, 'white', 'white')

snake = Snake()


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
    except Exception as e:
        print e



# Handler to draw on canvas
def draw(canvas):
    snake.draw(canvas)

def actualize():
    snake.actualize()

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.set_draw_handler(draw)







