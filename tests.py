import nose
import json
from spiral import Spiral


def setup():
    with open('static.txt') as f:
        static_data = json.loads(f.read)

def testSpiralCoordinate():
    c = Spiral()
    assert c.position(-4,0) is 40 # left quadrant
    assert c.position(-4,4) is 64 # even squares
    assert c.position(2,-3) is 49 # odd squares
    assert c.position(-1,3) is 34 # top quadrant
    assert c.position(0,-2) is 24 # bottom quadrant
    assert c.position(2,-1) is 27 # right quadrant
