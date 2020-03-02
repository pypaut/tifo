import math


def RgbToHsv(pixel):
    r, g, b = pixel[0] / 255, pixel[1] / 255, pixel[2] / 255
    mx = max(r, g, b)
    mn = min(r, g, b)
    diff = mx - mn

    # Hue
    if mx == mn:
        h = 0
    elif mx == r:  # More red
        h = (60 * ((g - b) / diff) + 360) % 360
    elif mx == g:  # More green
        h = 60 * ((b - r) / diff) + 120
    elif mx == b:  # More blue
        h = 60 * ((r - g) / diff) + 240

    # Saturation
    if mx == 0:
        s = 0
    else:
        s = 1 - mn / mx

    # Value
    v = mx

    return (h, s, v)


def HsvToRgb(pixel):
    h, s, v = pixel[0], pixel[1], pixel[2]
    h_i = math.floor(h / 60) % 6
    f = h / 60 - h_i
    l = v * (1 - s)
    m = v * (1 - f * s)
    n = v * (1 - (1 - f) * s)

    v = int(v * 255)
    l = int(l * 255)
    m = int(m * 255)
    n = int(n * 255)

    if h_i == 0:
        return (v, n, l)
    elif h_i == 1:
        return (m, v, l)
    elif h_i == 2:
        return (l, v, n)
    elif h_i == 3:
        return (l, m, v)
    elif h_i == 4:
        return (n, l, v)
    elif h_i == 5:
        return (v, l, m)
