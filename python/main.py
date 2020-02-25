from Image import Image
from GreyImage import GreyImage


def main():
    print("Open image")
    filename = 'media/20140712_163729.tga'
    im = Image(filename)

    im.show()

    im.equalizeHistogram()
    im.show()
    # print("Get components")
    # r, g, b = im.ComponentsRGB()

    # print("Combine components")
    # new_im = Image()
    # new_im.matrix = combine(r, g, b)

    # im.show()
    # new_im.show()

    # print("Convert to grayscale")
    # gray = GreyImage(im)

    # print("Save gray image")
    # # gray.save("gray.png")
    # gray.show()

    # print("Save histogram")
    # # gray.saveHistogram("histo_gray.png")
    # gray.showHistogram()

    # print("Equalize")
    # gray.equalizeHistogram()

    # print("Save equalized image")
    # # gray.save("equal_gray.png")
    # gray.show()

    # print("Save equalized histogram")
    # # gray.saveHistogram("histo_equal_gray.png")
    # gray.showHistogram()



if "__name__ == __main__":
    main()
