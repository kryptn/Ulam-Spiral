import nose
import json
from spiral import Spiral


def setup():
    with open('static.txt') as f:
        static_data = json.loads(f.read())

def testSpiralCoordinate():
    c = Spiral()
    assert c.position(-4,1) is 39 # left quadrant
    assert c.position(-4,4) is 64 # even squares
    assert c.position(2,-3) is 49 # odd squares
    assert c.position(-1,3) is 34 # top quadrant
    assert c.position(1,-3) is 48 # bottom quadrant
    assert c.position(2,-1) is 27 # right 

def testPrimeNumberChecker():
    c = Spiral()
    assert c.prime(2)  is True
    assert c.prime(3)  is True
    assert c.prime(4)  is False
    assert c.prime(5)  is True
    assert c.prime(79) is True
