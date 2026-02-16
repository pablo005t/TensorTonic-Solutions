def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    gray =[]
    for line in image:
        lg = []
        for pixel in line:
            R = pixel[0]
            G = pixel[1]
            B = pixel[2]
            pg = 0.299*R + 0.587*G + 0.114*B
            lg.append(pg)
        gray.append(lg)
    return gray        
