from boid import Boid
from flock import Flock

screenWidth = 800
screenHeight = 600

boids = Flock()

def setup():
    size(screenWidth, screenHeight)
    
def draw():
    background(50)
    boids.update()
    boids.draw()
    
def mousePressed():
    boids.add(Boid(mouseX, mouseY))
    
