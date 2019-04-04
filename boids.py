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
        ## Window and canvas set up
        self.window = Tk()
        self.canvas = Canvas(self.window)
        self.canvas.pack(expand = True, fill = "both")
        self.canvas.tk_setPalette(background = "white")
        self.canvas.config(width=500, height=500) ## Hard coded size, no resizing availible
        
        self.offset = [250,250]

    ## Draws all the boids
    def draw(self, boids):

        for b in boids:
            ## Create the boid circles, We use offset so the screen can pan
            ## and we divide the position and size by 2 to account for faster movement
            b.image = self.canvas.create_oval(((b.position[0] - 3)/2 + self.offset[0],
                                          (b.position[1] - 3)/2 + self.offset[1]),
                                         ((b.position[0] + 3)/2 + self.offset[0],
                                          (b.position[1] + 3)/2 + self.offset[1]))
       

         
def move_all_boids_to_new_positions(boids):
    ## Create 3 vectors
    v1 = []
    v2 = []
    v3 = []
    for b in boids:
        
        velX = 0
        velY = 0
        
        posX = 0
        posY = 0

        ## Run the rules
        v1 = rule1(b, boids)
        v2 = rule2(b, boids)
        v3 = rule3(b, boids)

        ## Sum rule velocities and adjust
        velX = b.velocity[0] + v1[0] + v2[0] + v3[0]
        velY = b.velocity[1] + v1[1] + v2[1] + v3[1]
        
        b.velocity = (velX, velY)

        ## Change boids position
        posX = b.position[0] + b.velocity[0]
        posY = b.position[1] + b.velocity[1]
        
        b.position = (posX, posY)
        
        ## Change camera positon if boids hit edge
        boundPosition(b)
        
def rule1(b1, boids):
    r1 = [0, 0]
    
    for b in boids:
        if b != b1:
            r1[0] = r1[0] + b.position[0]
            r1[1] = r1[1] + b.position[1]

    ## len(boids) - 1 == N-1
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
            ## Calculate euclidian distance between boids
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
    wind = [1,1]
    return wind

## Function for panning screen if boids run off
def boundPosition(b):
    global graphics # Global because called from move all and that doesn't have
                    ## access to graphics but need it to change offset
    # Zero the offset changes
    xOffset = 0
    yOffset = 0

    ## Min and max are based on predetermined window size
    xMin = 10
    xMax = 490
    yMin = 10
    yMax = 490

    
    if (b.position[0]/2 + graphics.offset[0]) < xMin:
        xOffset = 400
    elif (b.position[0]/2 + graphics.offset[0]) > xMax:
        xOffset = -400
    if (b.position[1]/2 + graphics.offset[1]) < yMin:
        yOffset = 400
    elif (b.position[1]/2 + graphics.offset[1]) > yMax:
        yOffset = -400

    ## If the boid has hit x and or y "wall", change the offset
    if (xOffset != 0 or yOffset != 0):
        
        graphics.offset[0] += xOffset
        graphics.offset[1] += yOffset
        

## Main function, contains main loop
def main():
    global graphics
    boids = init(20) #boids is a list of boids
    graphics = Graphics(boids) ## init Graphics window

    while True:
        
        graphics.canvas.delete("all")
        graphics.draw(boids)
        graphics.canvas.update_idletasks()
        graphics.canvas.update()
        graphics.canvas.after(10)
        move_all_boids_to_new_positions(boids)

## returns list of x boids
def init(x):
    bList = []
    #starts boids at random postion in middle
    for i in range(0,x):
        randX = random.randint(-50, 50)
        randY = random.randint(-50, 50)
        newBoid = boid(randX, randY)
        bList.append(newBoid)
    return bList
        
main()
