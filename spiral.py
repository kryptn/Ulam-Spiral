import sys

class Spiral(object):
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
        
        return rx,ry
        
        
    def position(self, x, y):
        bases = self.base(x,y)
        
        if abs(x) == y and x < 0: # even squares
            r = bases[0]**2
        elif x*-1 == y+1 and x >= 0: # odd squares
            r = bases[0]**2
        elif x*-1 > abs(y) or x >= abs(y):
            r = (abs(bases[0])-2)**2+1 + abs(bases[0])
            if x < 0: # left quadrant
                r = r - y + x - 1
            else: # right quadrant
                r = r + y - x - 3
        elif y*-1 >= abs(x) or y > abs(x): # top and bottom
            lean = bases[1]/abs(bases[1])
            r = bases[1]**2 + abs(bases[1]) - x*lean - y*lean * 3
        else:
            r = -1
            print >> sys.stderr, "Totally shouldn't happen %d,%d" % (x, y)
        
        return r
    
    def __init__(self, radius=None):
        self.radius = radius
      
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

    def show(self):
        for y in reversed(self.radius):
            for x in self.radius:
                print "%d\t" % (self.position(x,y)),
            print '\n'
