import math


def RgbToHsv(pixel):
    r, g, b = pixel[0]/255, pixel[1]/255, pixel[2]/255
    mx = max(r, g, b)
    mn = min(r, g, b)
    diff = mx - mn

    # Hue
    if mx == mn:
        h = 0
    elif mx == r:  # More red
        h = (60 * ((g-b)/diff) + 360) % 360
    elif mx == g:  # More green
        h = (60 * ((b-r)/diff) + 120) % 360
    elif mx == b:  # More blue
        h = (60 * ((r-g)/diff) + 240) % 360

    # Saturation
    if mx == 0:
        s = 0
    else:
        s = (diff/mx)*100

    # Value
    v = mx*100

    return (h, s, v)


def HsvToRgb(pixel):
    h, s, v = pixel[0], pixel[1], pixel[2]
    new_h = math.floor(h/60) % 6
    f = h/60 - new_h
    l = v * (1 - s)
    m  = v * (1 - f * s)
    n = v * (1 - (1 - f) * s)
    if new_h == 0:
        return (v, n, l)
    elif new_h == 1:
        return (m, v, l)
    elif new_h == 2:
        return (l, v, n)
    elif new_h == 3:
        return (l, m, v)
    elif new_h == 4:
        return (n, l, v)
    elif new_h == 5:
        return (v, l, m)
