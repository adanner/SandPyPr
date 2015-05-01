from boid import *
       
class Flock(object):
    def __init__(self):
        self.boids = []
        
    def add(self, boid):
        self.boids.append(boid)
        
    def update(self):
        for boid in self.boids:
            boid.update()
            
    def draw(self):
        for boid in self.boids:
            boid.draw()
   
