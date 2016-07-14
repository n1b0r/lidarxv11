import math
from unittest import TestCase


class Vector():

    def __init__(self, **kwargs):

        angle = kwargs.get('angle')
        if not angle is None:
            print "angle", angle
            self.vx, self.vy = self.from_angle(angle)
            print "vx", self.vx
        else:
            self.vx = kwargs.get('vx')
            self.vy = kwargs.get('vy')

    def from_angle(self, angle):
        angle = math.radians(angle)

        x = math.cos(angle)
        y = math.sin(angle)

        return float(x), float(y)

    def normalize(self):
        speed_vector_width = math.sqrt(self.vx**2 + self.vy**2)
        if speed_vector_width == 0:
            normalized_speed_vector = Vector(vx=0, vy=0)
        else:
            normalized_speed_vector = Vector(vx=self.vx / speed_vector_width,
                                             vy=self.vy / speed_vector_width)
        return normalized_speed_vector

    def angle(self, radian=True):
        a = (math.atan2(self.vy, self.vx) + math.pi/2.0) * 180 / math.pi
        if radian:
            return math.radians(a)
        else:
            return a

    def __str__(self):
        return 'Vector[vx:{} vy:{}]'.format(self.vx, self.vy)


class VectorTest(TestCase):

    def test_vector_from_angle(self):

        v = Vector(angle=0)
        assert v.vx == 1
        assert v.vy == 0

        v = Vector(angle=90)
        assert v.vx == 0
        assert v.vy == 1

        v = Vector(angle=180)
        assert v.vx == -1
        assert v.vy == 0

        v = Vector(angle=270)
        assert v.vx == 0
        assert v.vy == -1

        v = Vector(angle=360)
        assert v.vx == 1
        assert v.vy == 0

        v = Vector(angle=358)
        assert v.vx == 0
        assert v.vy == 0