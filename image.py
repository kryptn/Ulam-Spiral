from spiral import Spiral
from PIL import Image

class SpiralImage(Spiral):
    
    def spiral_generator(self, radius):
        for y in xrange(radius,radius*-1,-1):
            for x in xrange(radius*-1,radius):
                v = self.position(x, y)
                d = self.tempprime(v)
                d = 1 if d else 0
                yield str(d)

    def spiral_list(self, radius):
        r = []
        for y in xrange(radius,radius*-1,-1):
            for x in xrange(radius*-1,radius):
                v = self.position(x,y)
                d = self.tempprime(v)
                d = 1 if d else 0
                r.append(str(d))
        return r

    def make_image(self, radius):
        imagedata = self.spiral_list(radius)
        i = Image.new('1',(radius*2,radius*2))
        i.putdata(''.join(imagedata))
        i.save('static/%dpxr.png' % radius,'PNG')


#something something image.putdata(generator)
