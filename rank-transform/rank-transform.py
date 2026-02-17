def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    positions = []
    for value in values:
        position = 1 
        equals = 0
        for i in values:
            if value > i:
                position += 1
            if value == i:
                equals += 1
        if equals != 1:
            positionf = position + equals -1
            sum_pos = (positionf * (positionf +1)) - (position * (position -1))
            sum_pos = sum_pos / 2
            position = sum_pos / equals
        positions.append(position)
    return positions