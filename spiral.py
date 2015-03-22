import sys
import math

class Spiral(object):

    def isqrt(self, n):
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    def lrange(self, start, stop, step):
        while start < stop:
            yield start
            start += step

    def prime(self, n):
        if n == 2:
            return True
        if (n < 2) or (n % 2 == 0):
            return False
        return all(n % i for i in self.lrange(3, int(self.isqrt(n)) + 1, 2))
    
    @staticmethod
    def tempprime(n):
        if n == 2:
            return True
        if (n < 2) or (n % 2 == 0):
            return False
        return all(n % i for i in xrange(3,int(math.sqrt(n))+1, 2))

    def base(self, x, y):
        """
        returns base of x value in the spiral
        negative should be even (2,4,6,8,...)
             corrosponding coordinate would be (x, x*-1)
        positive should be odd    (1,3,5,7,...)
             corrosponding coordinate would be (x,x*-1 -1)
        basically r = 2x, +3 if >= 0
        
        """
        
        rx = 2*x
        if x >= 0:
            rx += 3
        
        ry = 2*y
        if y < 0:
            ry -= 1
        
        return long(rx),long(ry)
        
        
    def position(self, x, y):
        bases = self.base(x,y)
        
        if x*-1 > abs(y) or x >= abs(y): # left and right
            sign = cmp(bases[0], 0)
            r = (bases[0]-2*sign)**2 + abs(bases[0]) + y*sign - x*sign - sign-1
        elif y*-1 >= abs(x) or y > abs(x): # top and bottom
            sign = cmp(bases[1] , 0)
            r = bases[1]**2 + abs(bases[1]) - x*sign - y*sign * 3
        else:
            r = bases[0]**2
        return r
    
    def __init__(self, radius=None):
        self.radius = radius
        
        if radius:
          self.generate()
      
    def generate(self, radius=None):
        if radius:
            self.radius = radius
        
        self.grid = {}
        if self.radius:
            r = range(self.radius * -1 -1, self.radius + 1)
            for x in r:
                self.grid[x] = {}
                for y in r:
                    self.grid[x][y] = self.position(x,y)

    def show(self, prime=False):
        r = range(self.radius * -1 - 1, self.radius + 1)
        for y in reversed(r):
            for x in r:
                if prime:
                    v = 1 if self.prime(self.position(x,y)) else 0
                else:
                    v = self.position(x,y)
                
                print "%d\t" % (v),
            print '\n'
