import serial
import numpy as np

from main import *
from utils import *


class Lidar():
    def __init__(self, **kwargs):
        self.device = kwargs.get('device')
        self.baudrate = kwargs.get('baudrate', 115200)
        self.serial = serial.Serial(self.device, self.baudrate)

    def read(self):
        """
        collect full turn data and yield it
        """

        block = []
        wait_header = True
        while True:
            if wait_header:
                b = self.serial.read(1).encode('hex')
                if b == 'fa':
                    wait_header = False
            else:
                a = self.serial.read(21).encode('hex')
                line = "fa"+a
                wait_header = True

        # with open('test.log', 'r') as f:

        #     for i, line in enumerate(f.readlines()):
        #         line = line.rstrip('\n')

                # convert line  
                n = 2
                line = [int(line[i:i+n], 16) for i in range(0, len(line), n)]

                p = LidarPacket(line)

                if p.index == 0:
                    block.sort(key=lambda x:x.index)
                    yield block
                    block = []

                # print p.index
                for d in p.data:
                    block.append(d)

    def draw(self):
        import matplotlib.pyplot as plt

        fig = plt.figure()
        ax = fig.add_subplot(111)

        # some X and Y data
        x = np.random.randn(360)
        y = np.random.randn(360)

        li, = ax.plot(x, y, 'ro')
        m = 400
        ax.axis([-m, m, -m, m])

        # draw and show it
        fig.canvas.draw()
        plt.show(block=False)

        for block in self.read():

            x = []
            y = []
            for e in block:
                v = Vector(angle=int(e.index))
                print '{}: {} => {}'.format(e.index, e.distance, v)
                x.append(v.vx * e.distance)
                y.append(v.vy * e.distance)
                # x.append(e.index)
                # y.append(e.distance)

            li.set_xdata(x)
            li.set_ydata(y)

            fig.canvas.draw()