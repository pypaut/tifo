from Image import Image
from GreyImage import GreyImage
from Hsv import *


def main():
    # filename = 'media/20140712_163729.tga'
    filename = 'media/20140712_163729.tga'
    im = Image(filename)
    id_mask = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    edge_mask = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]

    im.laplacien()
    im.show()


if "__name__ == __main__":
    main()
