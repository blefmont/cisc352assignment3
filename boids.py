### Boids rules
from tkinter import *

class boid():
    #creates boid at target location, with velocity (0,1)
    def __init__(self, x, y):
        self.position = (x,y)
        self.velocity = (0,1)
        self.image = None
## Graphics class, manages drawing of the boids in one place and keeping
## the variables that hold the tkinter objects
class Graphics():
    def __init__(self, boids):
        self.window = Tk()
        self.canvas = Canvas(self.window)
        self.canvas.pack(expand = True, fill = "both")
        self.canvas.tk_setPalette(background = "white")
        
        self.offset = (self.canvas.winfo_width() // 2,
                       self.canvas.winfo_height() // 2)
        
        
    def update(self, boids):
        
        self.offset = (self.canvas.winfo_width() // 2,
                       self.canvas.winfo_height() // 2)
        for b in boids:
            self.canvas.delete(b.image)
            b.image = self.canvas.create_oval((b.position[0] - 3 + self.offset[0],
                                          b.position[1] - 3 + self.offset[1]),
                                         (b.position[0] + 3 + self.offset[0],
                                          b.position[1] + 3 + self.offset[1]))        
            
def move_all_boids_to_new_positions(boids):
    v1 = []
    v2 = []
    v3 = []
    for b in boids:
        velX = 0
        velY = 0
        posX = 0
        posY = 0
        v1 = rule1(b, boids)
        v2 = rule2(b, boids)
        v3 = rule3(b, boids)
        velX = b.velocity[0] + v1[0] + v2[0] + v3[0]
        velY = b.velocity[1] + v1[1] + v2[1] + v3[1]
        b.velocity = (velX, velY)
        posX = b.position[0] + b.velocity[0]
        posY = b.position[1] + b.velocity[1]
        b.position = (posX, posY)
        
def rule1(b1, boids):
    r1 = [0,0]
    for b in boids:
        if b != b1:
            r1[0] = r1[0] + b.position[0]
            r1[1] = r1[1] + b.position[1]
    r1[0] = r1[0] / len(boids)
    r1[1] = r1[1] / len(boids)
    r1[0] = r1[0] - b1.position[0]
    r1[1] = r1[1] - b1.position[1]
    r1[0] = r1[0] / 100
    r1[1] = r1[1] / 100
    return r1

def rule2(b2, boids):
    r2 = [0,0]
    for b in boids:
        if b != b2:
            distance = 0
            distance = abs(b.position[0] - b2.position[0]) + abs(b.position[1] - b2.position[1])
            if distance < 100:
                r2[0] = r2[0] - (b.position[0] - b2.position[0])
                r2[1] = r2[1] - (b.position[1] - b2.position[1])
    return r2

def rule3():
    pass
def rule4():
    pass


def main():
    boids = init(5)
    graphics = Graphics(boids)
    for i in range(10000):
        move_all_boids_to_new_positions(boids)
        graphics.update()
    
    

## returns list of x boids
def init(x):
    bList = []
    #starts each boid 10 ositions apart
    for i in range(0,x):
        newBoid = boid(i*10,0)
        bList.append(newBoid)
    return bList

def gui_init():
    window = Tk()
    canvas = Canvas(window)
    canvas.pack(expand = True, fill = "both")
    canvas.tk_setPalette(background = "white")
    return canvas

def draw_boids(canvas, boids):
    for b in boids:
        canvas.delete(b.image)
        b.image = canvas.create_oval((b.position[0]-3,b.position[1]-3),
                         (b.position[0]+3,b.position[1]+3))
        
        
main()

