from Combine import combine
from GreyImage import GreyImage
from Hsv import *
import matplotlib.pyplot as plt


class Image:
    def __init__(self, filename=None):
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

    def ComponentsHSV(self):
        h = GreyImage()
        s = GreyImage()
        v = GreyImage()
        for line in self.matrix:
            h_line = []
            s_line = []
            v_line = []
            for p in line:
                h_line.append(int(p[0]))
                s_line.append(int(p[1]))
                v_line.append(int(p[2]))
            h.matrix.append(h_line)
            s.matrix.append(s_line)
            v.matrix.append(v_line)
        return h, s, v

    def equalizeHistogram(self):
        r, g, b = self.ComponentsRGB()
        r.equalizeHistogram()
        g.equalizeHistogram()
        b.equalizeHistogram()
        self.matrix = combine(r, g, b)

    def matrixHsv(self):
        hsv_matrix = []
        for line in self.matrix:
            new_line = []
            for p in line:
                new_line.append(RgbToHsv(p))
                # new_line.append(colorsys.rgb_to_hsv(p[0], p[1], p[2]))
            hsv_matrix.append(new_line)
        return hsv_matrix

    def equalizeHistogramHsv(self):
        # Convert image to HSV
        self.matrix = self.matrixHsv()

        # Get H, S, and V components as grey scale
        h, s, v = self.ComponentsHSV()

        # Equalize histogram on V
        v.equalizeHistogram()

        # Combine back to HSV image
        new_matrix = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                new_pix = (
                    h.matrix[i][j] / 255,
                    s.matrix[i][j] / 255,
                    v.matrix[i][j] / 255,
                )
                new_line.append(new_pix)
            new_matrix.append(new_line)
        self.matrix = new_matrix

        # Convert to RGB
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = HsvToRgb(self.matrix[i][j])

    def scaleSaturation(self, coef):
        # Convert to HSV image
        matrixHsv = self.matrixHsv()

        # Scale the saturation field
        matrixRgb = []
        for i in range(self.height):
            new_line = []
            for j in range(self.width):
                p = matrixHsv[i][j]
                # Convert to RGB
                new_line.append(HsvToRgb((p[0], coef * p[1], p[2])))
            matrixRgb.append(new_line)
        self.matrix = matrixRgb
