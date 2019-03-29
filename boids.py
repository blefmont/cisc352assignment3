### Boids rules
class boid():
    def __init__(self):
        self.position = (0,0)
        self.velocity = (0,0)
    #creates boid at target location, with velocity (0,1)
    def __init__(self, x, y):
        self.position = (x,y)
        self.velocity = (0,1)

def move_all_boids_to_new_positions(boids):
    pass
def rule1():
    pass
def rule2():
    pass
def rule3():
    pass
def rule4():
    pass


def main():
    boids = init(5)
    move_all_boids_to_new_positions(boids)

## returns list of x boids
def init(x):
    blist = []
    #starts each boid 10 ositions apart
    for i in range(0,x):
        newBoid = boid(i*10,0)
        bList.append(newBoid)
    return bList

main()

