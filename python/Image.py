from Combine import combine
import matplotlib.pyplot as plt
from GreyImage import GreyImage


class Image:
    def __init__(self, filename = None):
        if filename == None:
            self.matrix = []
            self.width = 0
            self.height = 0
            return
        self.matrix = plt.imread(filename)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def show(self):
        plt.imshow(self.matrix)
        plt.show()

    def ComponentsRGB(self):
        r = GreyImage()
        g = GreyImage()
        b = GreyImage()
        for line in self.matrix:
            r_line = []
            g_line = []
            b_line = []
            for p in line:
                r_line.append(p[0])
                g_line.append(p[1])
                b_line.append(p[2])
            r.matrix.append(r_line)
            g.matrix.append(g_line)
            b.matrix.append(b_line)
        r.width = self.width
        g.width = self.width
        b.width = self.width
        r.height = self.height
        g.height = self.height
        b.height = self.height
        return r, g, b

    def equalizeHistogram(self):
        r, g, b = self.ComponentsRGB()
        r.equalizeHistogram()
        g.equalizeHistogram()
        b.equalizeHistogram()
        self.matrix = combine(r, g, b)
