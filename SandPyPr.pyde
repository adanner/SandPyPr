from boid import Boid
from flock import Flock

"""
Global Variables
for Processing framework
"""
screenWidth = 800
screenHeight = 600
allboids = Flock()

def setup():
    """
    create initial screen
    """
    size(screenWidth, screenHeight)
    for i in range(20):
        allboids.add(Boid(screenWidth/2,screenHeight/2))
    
def draw():
    """
    animate boids
    """
    background(50)
    allboids.decide()
    allboids.update()
    allboids.draw()
    
def mousePressed():
    """
    add new boid when user clicks mouse
    at the mouse location with a random
    unit velocity
    """
    allboids.add(Boid(mouseX, mouseY))
    
