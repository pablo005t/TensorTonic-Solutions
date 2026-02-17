def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    # Write code here
    powers = []
    for value in values:
        power = [value** i for i in range(degree + 1)]
        powers.append(power)
    return powers