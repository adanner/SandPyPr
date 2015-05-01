from random import random
from math import *
from vector2d import Vector2D

boidSize  = 4
boidSpeed = 2
boidAccel = 0.03

class Boid(object):
    def __init__(self, x, y):
        self.position = Vector2D(x,y)
        self.velocity = Vector2D.random2D()
        self.acceleration = Vector2D(0,0)
        self.size = boidSize
        self.maxspeed = boidSpeed
        self.maxaccel = boidAccel
    
    def wrap(self):
        x = self.position.x
        y = self.position.y
        sz = self.size
        #hey, python's weird floating point mod is useful
        if  (x < -sz) or (x > width+sz):
           self.position.x= self.position.x % width
        if  (y < -sz) or (y > height+sz):
           self.position.y = self.position.y % height
    
    def draw(self):
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

    def decide(self, boids):
        return 
    
    def update(self):
       self.velocity += self.acceleration
       self.velocity.limit(self.maxspeed)
       self.position += self.velocity
       self.acceleration *= 0
       self.wrap()  
