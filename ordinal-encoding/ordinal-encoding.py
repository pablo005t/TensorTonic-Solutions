def ordinal_encoding(values, ordering):
    """
    Encode categorical values using the provided ordering.
    """
    encoding = []
    for val in values:
        encoding.append(ordering.index(val))
    return encoding