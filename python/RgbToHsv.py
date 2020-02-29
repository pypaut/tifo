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
