### Boids rules
from tkinter import *
import time
import math
import random

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
        self.listOfBoids = boids
        self.window = Tk()
        self.canvas = Canvas(self.window)
        self.canvas.pack(expand = True, fill = "both")
        self.canvas.tk_setPalette(background = "white")
        self.canvas.config(width=500, height=500)
        
        self.offset = (self.canvas.winfo_width() // 2,
                       self.canvas.winfo_height() // 2)
        
        
    def draw(self, boids):

        for b in boids:
            #self.canvas.delete(b.image)
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
        v4 = rule4(b, boids)

        velX = b.velocity[0] + v1[0] + v2[0] + v3[0]
        velY = b.velocity[1] + v1[1] + v2[1] + v3[1]
        
        b.velocity = (velX, velY)
        
        posX = b.position[0] + b.velocity[0]
        posY = b.position[1] + b.velocity[1]
        
        b.position = (posX, posY)
        
        time.sleep(0.001)

        posX = posX + v4[0]
        posY = posY + v4[1]
        b.position = (posX, posY)

        boundPosition(b)
        
def rule1(b1, boids):
    r1 = [0, 0]
    
    for b in boids:
        if b != b1:
            r1[0] = r1[0] + b.position[0]
            r1[1] = r1[1] + b.position[1]
            
    r1[0] = r1[0] / (len(boids)-1)
    r1[1] = r1[1] / (len(boids)-1)
    
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
            distance = math.sqrt((b.position[0] - b2.position[0])**2 + (b.position[1] - b2.position[1])**2)
            if distance < 10:
                r2[0] = r2[0] - (b.position[0] - b2.position[0])
                r2[1] = r2[1] - (b.position[1] - b2.position[1])
    return r2

def rule3(b3,boids):
    r3 = [0, 0]
    
    for b in boids:
        if b != b3:
            r3[0] = r3[0] + b.velocity[0]
            r3[1] = r3[1] + b.velocity[1]
            
    r3[0] = r3[0] / len(boids)
    r3[1] = r3[1] / len(boids)
    
    r3[0] = r3[0] - b3.velocity[0]
    r3[1] = r3[1] - b3.velocity[1]
    
    r3[0] = r3[0] / 8
    r3[1] = r3[1] / 8
    
    return r3
            
        
def rule4(b4,boids):
    wind = [1,0]
    return wind

def boundPosition(b):

    v = 10

    xVel = b.velocity[0]
    yVel = b.velocity[1]
    
    xMin = 10
    xMax = 490
    yMin = 10
    yMax = 490

    if b.position[0] < xMin:
        xVel = v
    elif b.position[0] > xMax:
        xVel = -v

    if b.position[1] < yMin:
        yVel = v
    elif b.position[1] > yMax:
        yVel = -v

    b.velocity = (xVel, yVel)

def main():
    boids = init(20) #boids is a list of boids
    graphics = Graphics(boids)

    while True:
        
        graphics.canvas.delete("all")
        graphics.draw(boids)
        graphics.canvas.update_idletasks()
        graphics.canvas.update()
        
        move_all_boids_to_new_positions(boids)

## returns list of x boids
def init(x):
    bList = []
    #starts each boid 10 ositions apart
    for i in range(0,x):
        randX = random.randint(200, 300)
        randY = random.randint(200, 300)
        newBoid = boid(randX, randY)
        bList.append(newBoid)
    return bList

def gui_init():
    window = Tk()
    canvas = Canvas(window)
    canvas.pack(expand = True, fill = "both")
    canvas.tk_setPalette(background = "white")
    return canvas
        
main()
