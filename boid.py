from random import random
from math import *
from vector2d import Vector2D

boidSize  = 2
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
        self.maxSpeed = boidSpeed
        self.maxAccel = boidAccel
        #print self.position, self.velocity
    
    def decide(self, boids):
        """
        Have each boid decide how to modify its velocity,
        based on location, velocity of nearby boids
        """
        
        sep = self.separate(boids)
        coh = self.cohesion(boids)
        ali = self.align(boids)
        self.acceleration = 1.5*sep + 0.5*coh + 1*ali
        self.acceleration.limit(self.maxAccel)
        #return #do nothing

        #in this toy example, every boid just wants to circle
        #self.turn(90)

    def separate(self, boids):
        """
        apply acceleration forcing boid away from
        other boids that are too close
        """
        mindist = 25 #desired minimum separtion

        vDesired = Vector2D(0,0)
        closeBoids = 0
        for boid in boids:
          dist = self.position.dist(boid.position)
          if (dist > 0) and (dist < mindist):
             #other boid is too close, move away
             disp = self.position - boid.position
             disp.normalize()
             disp /= dist 
             vDesired += disp
             closeBoids = closeBoids + 1
        
        if closeBoids > 0: #average
          vDesired /= closeBoids

        if vDesired.mag() > 0:
          vDesired.setMag(self.maxSpeed)
          accel = vDesired - self.velocity
          accel.limit(self.maxAccel)
          return accel
        else:
          #no need to separate
          return Vector2D(0,0)
 
    def cohesion(self, boids):
        """
        apply acceleration forcing boid towards 
        center of other nearby boids
        """
        neighborhood = 50 #radius of local neighborhood

        posSum = Vector2D(0,0)
        closeBoids = 0
        for boid in boids:
          dist = self.position.dist(boid.position)
          if (dist > 0) and (dist < neighborhood):
             #this boid is a neighbore, average location
             posSum += boid.position
             closeBoids = closeBoids + 1
        
        if closeBoids > 0: #average location, steer there
          return self.seek(posSum/closeBoids)
        else: #no one nearby, no cohesion
          return Vector2D(0,0)     
    
    def align(self, boids):
        """
        apply acceleration forcing boid to 
        align with direction of other nearby boids
        """
        neighborhood = 50 #radius of local neighborhood

        dirSum = Vector2D(0,0)
        closeBoids = 0
        for boid in boids:
          dist = self.position.dist(boid.position)
          if (dist > 0) and (dist < neighborhood):
             #this boid is a neighbore, average location
             dirSum += boid.position
             closeBoids = closeBoids + 1
        
        if closeBoids > 0: #average alignment
          vDesired = dirSum / closeBoids
          vDesired.setMag(self.maxSpeed)
          accel = vDesired - self.velocity
          accel.limit(self.maxAccel)
          return accel  
        else: #no one nearby, no alignment
          return Vector2D(0,0)     
 
    def seek(self, loc):
      """
      compute acceleration that steers current velocity
      towards target loc
      """
      vDesired = loc - self.position
      vDesired.setMag(self.maxSpeed)
      accel = vDesired - self.velocity
      accel.limit(self.maxAccel)
      return accel


    def turn(self, degrees):
        """ apply turning nudge by degrees """
        theta = radians(degrees)
        self.acceleration = self.velocity.rotate(theta)
        self.acceleration.limit(self.maxAccel)

    
    def update(self):
       """
       Apply acceleration of current time step 
       to update velocity an position. Reset acceleration
       to zero before next time step
       """
       self.velocity += self.acceleration
       self.velocity.limit(self.maxSpeed)
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
           self.position.x = self.position.x % width
        if  (y < -sz) or (y > height+sz):
           self.position.y = self.position.y % height
 
 
