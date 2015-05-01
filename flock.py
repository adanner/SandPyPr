from boid import *
       
class Flock(object):
    """
    A flock is just a list of Boids
    """
    def __init__(self):
        """ create empty flock """
        self.boids = []
        
    def add(self, boid):
        """ add boid to flock """
        self.boids.append(boid)

    def decide(self):
        """ 
        have each boid decide its new acceleration
        for the next time stamp by examining other
        boid locations
        """
        for boid in self.boids:
            boid.decide(self.boids)
            
    def update(self):
        """
        apply acceleration to each boid and
        compute new position/velocity of boid
        """
        for boid in self.boids:
            boid.update()
            
    def draw(self):
        """
        draw each boid in its current location with
        current heading
        """
        for boid in self.boids:
            boid.draw()
   
