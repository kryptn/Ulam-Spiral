#!/usr/bin/python

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
        
        return abs(rx),abs(ry)
        
        
    def position(self, x, y):
        bases = self.base(x,y)
        
        if abs(x) == y and x < 0: # even squares
            r = bases[0]**2
        elif x*-1 == y+1 and x >= 0: # odd squares
            r = bases[0]**2
        elif x*-1 > abs(y): # left quadrant
            r = (bases[0]-2)**2+1 + bases[0]-y + x-1
        elif x >= abs(y): # right quadrant
            r = (bases[0]-2)**2+1 + bases[0]+y - x-3
        elif y > abs(x): # top quadrant
            r = bases[1]**2 + bases[1]-x -y*3
        elif y*-1 >= abs(x): # bottom quadrant
            r = bases[1]**2 + bases[1]+x +y*3 
        else:
            r = -1
            print >> sys.stderr, "Totally shouldn't happen %d,%d" % (x, y)
        
        return r
    
    def __init__(self, radius):
        self.radius = range(radius * -1 -1, radius + 1)
        self.grid = {}
        for x in self.radius:
            self.grid[x] = {}
            for y in self.radius:
                self.grid[x][y] = self.position(x,y)
    
    def show(self):
        
        for y in reversed(self.radius):
            for x in self.radius:
                print "%d\t" % (self.position(x,y)),
            print '\n'
