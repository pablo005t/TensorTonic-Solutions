def frequency_encoding(values):
    """
    Replace each value with its frequency proportion.
    """
    counter = []
    total = len(values)
    for val in values: 
        cont = 0
        for i in values:
            if val == i:
                cont += 1
        freq = cont / total
        counter.append(freq)
    return counter
    # Write code here