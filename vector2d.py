from math import *
from random import *

class Vector2D(object):
  """
  This class represents a 2D pair of floats.
  This pair could either be interpreted as a
  mathematical vector describing the components 
  of a magnitude and direction or it could 
  describe the coordinates of a point location in
  an affine space
  """  
  
  def __init__(self, x, y):
    """ Construct a new vector """
    self.x = float(x)
    self.y = float(y)


  def __str__(self):
    """ print Vec2 in a nice way """
    return "(%.3f, %.3f)" % (self.x, self.y)

  """ 
  basic getters/setters, but feel free
  to use v1.x and v1.y directly
  """
  
  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def setX(self, x):
    self.x = x

  def setY(self, y):
    self.y = y

  def magSq(self):
    """
    return magnitude (length) of vector squared
    """
    return self.x**2 + self.y**2

  def mag(self):
    """
    return magnitude (length) of vector
    """
    return sqrt(self.x**2+self.y**2)

  def __add__(self, v):
    """ 
    vector vector addition
    returns vec + v 
    """
    return Vector2D(self.x+v.x, self.y+v.y)
  
  def __sub__(self, v):
    """ 
    vector vector subtraction
    returns vec - v 
    """
    return Vector2D(self.x-v.x, self.y-v.y)

  def __mul__(self, a):
    """
    returns vec multiplied by scalar a
    using vec*a
    """
    return Vector2D(self.x*a, self.y*a)

  def __rmul__(self, a):
    """
    returns vec multiplied by scalar a
    using a*vec
    """
    return Vector2D(self.x*a, self.y*a)

  def __div__(self, a):
    """
    scalar division of a vector
    return vec/a
    """
    return Vector2D(self.x/a, self.y/a)

  def __truediv__(self, a):
    """
    scalar division of a vector
    return vec/a
    """ 
    return self.__div__(a)

  def dist(self, pt):
    """
    returns distance between vec and pt, treating 
    both elements as mathematical points (location), 
    not mathematical vectors (magnitued and direction)
    """
    disp = self-pt
    return disp.mag()

  def dot(self, v):
    """
    return (scalar) dot product of self and v
    """
    return self.x*v.x+self.y*v.y

  def cross(self, v):
    """
    return z componenty of cross product of self and v
    """
    return self.x*v.y - self.y*v.x

  def normalize(self):
    """
    normalize vector to have unit length
    modifies current vector and returns nothing
    """
    self /= self.mag()

  def normalized(self):
    """
    returns a new vector in same direction of
    current vector but of unit length
    """
    return self / self.mag()
  
  def limit(self, maxlen):
    """
    limit the length of the current vector to maxlen
    """
    if self.magSq() > maxlen*maxlen:
      self.normalize()
      self *= maxlen

  def setMag(self, length):
    """
    set magnitude of vector to length
    """
    self.normalize()
    self *= length

  def heading(self):
    """
    Calculate the angle of rotation for this vector
    """
    unit = self.normalized()
    return atan2(unit.y, unit.x)

  def rotate(self, angle):
    """
    Rotate vector counter clockwise by angle
    return newly rotated vector, assuming
    a right-handed coordinate system.
    
    In the processing window, 0,0 is in the upper left
    and coordinate system is left-handed, so rotations
    are clockwise
    """
    cs = cos(angle)
    sn = sin(angle)
    x = self.x
    y = self.y
    return Vector2D(x*cs - y*sn, x*sn + y*cs)

  def lerp(self, v, t):
    """
    linearly interpolate between current vector and v
    using t as weight. Assumes 0 <= t <= 1
    returns newly interpolated vector
    """
    return self*(1-t)+v*t

  def angleBetween(self, v):
    """
    compute angle between current vector and v
    """
    return acos(self.normalized().dot(v.normalized()))


  """
  In place operators +=, -=, *=, /=
  """

  def __iadd__(self, v):
    """ 
    in place vector addition
    vec += v 
    """
    self.x = self.x + v.x
    self.y = self.y + v.y
    return self

  def __isub__(self, v):
    """ 
    in place vector subtraction
    vec -= v 
    """
    self.x = self.x - v.x
    self.y = self.y - v.y
    return self

  def __imul__(self, a):
    """
    in place scalar multiplication
    vec *= a
    """
    self.x = self.x*a
    self.y = self.y*a
    return self

  def __idiv__(self, a):
    """
    in place scalar division
    vec /= a
    """
    self.x = self.x/a
    self.y = self.y/a
    return self

  """
  @staticmethod tells python that these methods will not make direct
  use of self variables. They are methods of the class, not
  a particular object of the class. They can be called using
  
   Vector2D.random2D()
   
   or 
   
   v1=Vector2D(0,0)
   v1.random2D()
  """
  
  @staticmethod
  def random2D():
    """
    return a new random 2D unit vector
    """
    return Vector2D.fromAngle(2*pi*random())

  @staticmethod
  def fromAngle(theta):
    """
    Make a unit vector from an angle in radians
    """
    return Vector2D(cos(theta), sin(theta))


def testVector2D():
  v1 = Vector2D(1, 2)
  v2 = Vector2D(2, 1)
  v3 = Vector2D(-2,1)
  v4 = Vector2D(1,0)
  print v1, v1.getX(), v1.getY(), v1.x, v1.y
  print v1.magSq()
  print v1.mag()

  print v1 + v2
  print v1 - v2
  print v1*2
  print (2*v1)/2

  v1 *= 2
  print v1
  v1 /= 2
  print v1

  print v1.dist(v2)
  print v1.dot(v2)
  print v1.dot(v3)
  print v1.cross(v2)
  print v2.cross(v1)
  print v2.cross(v2)

  print v1.mag()
  v1.limit(2)
  print v1.mag()

  print degrees(v1.heading())
  v1.setMag(4)
  print v1.mag()
   
  print degrees(v4.heading())

  v5 = v4.rotate(radians(90))
  print v4, v5
  print degrees(v5.heading())
  print v5
  print degrees(v4.angleBetween(v5))

  v5 *= 2
  print v5.normalized()

  v6 = Vector2D.random2D()
  print v6, v6.mag()

if __name__ == "__main__":
  testVector2D()

