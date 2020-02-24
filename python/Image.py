import matplotlib.pyplot as plt


class Image:
    def __init__(self, filename):
        self.matrix = plt.imread(filename)
        self.width = len(self.matrix)
        self.height = len(self.matrix[0])

    def show(self):
        plt.imshow(self.matrix)
        plt.show()
