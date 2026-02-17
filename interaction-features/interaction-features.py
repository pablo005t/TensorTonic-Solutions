def interaction_features(X):
    """
    Generate pairwise interaction features and append them to the original features.
    """
    interactions = []
    for feature in X:
        feature_interaction = [f for f in feature]
        for i in range(len(feature)):
            for j in [x for x in range(len(feature)) if x > i]:
                feature_interaction.append(feature[i]*feature[j])
        interactions.append(feature_interaction)
    return interactions