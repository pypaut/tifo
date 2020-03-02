import matplotlib.pyplot as plt

class GreyImage:
    def __init__(self, image = None):
        if image == None:
            self.matrix = []
            self.width = 0
            self.height = 0
            return

        # Matrix image
        self.matrix = []
        for line in image.matrix:
            new_line = []
            for pixel in line:
                new_line.append(int(
                        0.299 * pixel[0]
                        + 0.587 * pixel[1]
                        + 0.114 * pixel[2]
                    )
                )
            self.matrix.append(new_line)

        # Size
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])

    def setHistogram(self):
        self.histogram = [0 for _ in range(256)]
        for line in self.matrix:
            for e in line:
                self.histogram[e] += 1

    def setChistogram(self):
        self.chistogram = [0 for _ in range(256)]
        self.chistogram[0] = self.histogram[0]
        for i in range(1, 256):
            self.chistogram[i] = self.chistogram[i - 1] + self.histogram[i]

    def show(self):
        plt.imshow(self.matrix, cmap='gray')
        plt.show()

    def save(self, filename):
        plt.imshow(self.matrix, cmap='gray')
        plt.savefig(filename)

    def printHistogram(self):
        self.setHistogram()
        s = ""
        for i in range(256):
            s += f"{i} : {self.histogram[i]}\n"
        print(s)

    def printChistogram(self):
        self.setChistogram()
        s = ""
        for i in range(256):
            s += f"{i} : {self.chistogram[i]}\n"
        print(s)

    def showHistogram(self):
        self.setHistogram()
        x = [i for i in range(256)]
        plt.bar(x, self.histogram)
        plt.title('Histogram')
        plt.show()

    def showChistogram(self):
        self.setChistogram()
        x = [i for i in range(256)]
        plt.bar(x, self.chistogram)
        plt.title('Cumulated histogram')
        plt.show()

    def saveHistogram(self, filename):
        self.setHistogram()
        x = [i for i in range(256)]
        plt.bar(x, self.histogram)
        plt.title('Histogram')
        # plt.imshow(h)
        plt.savefig(filename)

    def saveChistogram(self, filename):
        self.setChistogram()
        x = [i for i in range(256)]
        plt.bar(x, self.chistogram)
        plt.title('Cumulated histogram')
        # plt.imshow(h)
        plt.savefig(filename)

    def equalizeHistogram(self):
        self.setHistogram()
        self.setChistogram()
        # Apply function
        for i in range(self.height):
            for j in range(self.width):
                p = self.matrix[i][j]
                height = len(self.matrix)
                width = len(self.matrix[0])
                self.matrix[i][j] = int(255 * self.chistogram[p] / (width * height))

    def convolution(self, mask):
        if len(mask) % 2 != 1:
            print("Error : Image.convolution() : mask must be of odd size.")
            return
        m = len(mask)
        b = m // 2 + 1
        e1 = len(self.matrix) - b + 1
        e2 = len(self.matrix[0]) - b + 1
        # Iterate upon image elements
        new_matrix = []
        for i in range(b, e1 + 1):
            new_line = []
            for j in range(b, e2 + 1):
                conv = 0
                # Iterate upon mask elements
                for k in range(m):
                    for l in range(m):
                        conv += self.matrix[i - b + k][j - b + l] * mask[k][l]
                new_line.append(conv)
            new_matrix.append(new_line)
        self.matrix = new_matrix
