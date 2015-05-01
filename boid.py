from random import random
from math import *
from vector2d import Vector2D

boidSize  = 4
boidSpeed = 2
boidAccel = 0.03

class Boid(object):
    
    def __init__(self, x, y):
        """
        Create new boid at position x,y
        with a random unit velocity
        and no acceleration
        """
        self.position = Vector2D(x,y)
        self.velocity = Vector2D.random2D()
        self.acceleration = Vector2D(0,0)

        """
        experiment by changing the constants
        above
        """
        self.size = boidSize
        self.maxspeed = boidSpeed
        self.maxaccel = boidAccel
        #print self.position, self.velocity
    
    def decide(self, boids):
        """
        Have each boid decide how to modify its velocity,
        based on location, velocity of nearby boids
        """
      
        return #do nothing

        #in this toy example, every boid just wants to circle
        self.turn(90)

    def turn(self, degrees):
        """ apply turning nudge by degrees """
        theta = radians(degrees)
        self.acceleration = self.velocity.rotate(theta)
        self.acceleration.limit(self.maxaccel)

    
    def update(self):
       """
       Apply acceleration of current time step 
       to update velocity an position. Reset acceleration
       to zero before next time step
       """
       self.velocity += self.acceleration
       self.velocity.limit(self.maxspeed)
       self.position += self.velocity
       self.acceleration *= 0
       self.wrap() #keep boid on torroidal screen

   
    def draw(self):
        """
        Draw boid as a triangle
        pointing in direction of current velocity
        at current position
        """
        sz = self.size
        theta = self.velocity.heading()
        fill(252,244,71)
        stroke(255)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            with beginShape(TRIANGLES):
                vertex( sz*2,  0)
                vertex(-sz*2,-sz)
                vertex(-sz*2, sz)

    def wrap(self):
        """
        Keep boid on screen by updating position 
        if boid is travelling off the edge. Wrap 
        the boid position as if screen were a torus
        """
        x = self.position.x
        y = self.position.y
        sz = self.size
        #hey, python's weird floating point mod is useful
        if  (x < -sz) or (x > width+sz):
           self.position.x= self.position.x % width
        if  (y < -sz) or (y > height+sz):
           self.position.y = self.position.y % height
 
 
