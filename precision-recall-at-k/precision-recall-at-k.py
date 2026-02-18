def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """

    precision = len(set(recommended[0:k]) & set(relevant)) / k
    recall = len(set(recommended[0:k]) & set(relevant)) / len(relevant)
    return [precision, recall]

    # Write code here