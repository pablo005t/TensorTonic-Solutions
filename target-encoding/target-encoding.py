def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    target = []
    for cat in categories:
        mean_cat = 0
        counter = 0
        for i in range(len(categories)):
            if categories[i] == cat:
                mean_cat += targets[i]
                counter += 1
        mean_cat = mean_cat / counter
        target.append(mean_cat)
    return target