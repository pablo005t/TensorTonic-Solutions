import numpy as np

def one_hot(y, num_classes=None):  
    classes = set(y)
    encode = []

    for x in y:
        encoded_x = []
        for i in classes:
            if i == x:
                encoded_x.append(1)
            elif i > x:
                encoded_x = encoded_x + [0]
            else:
                encoded_x = [0] +  encoded_x
        if num_classes!= None:
            while len(encoded_x) != num_classes:
                if len(encoded_x) <= x:
                    encoded_x = [0]+ encoded_x
                else:
                    encoded_x.append(0)
        encode.append(encoded_x)
    return encode