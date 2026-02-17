def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    import numpy as np
    if mode == "user":
        for user in ratings_matrix:
            if len([l for l in user if l!= 0]) == 0:
                mean = 0
            else:
                mean = np.mean(np.array([l for l in user if l!= 0]))
            for i in range(len(user)):
                if user[i] == 0:
                    user[i] = mean
        return ratings_matrix
    elif mode == "item":
        for i in range(len(ratings_matrix[0])):
            l_item = [ratings_matrix[l][i] for l in range(len(ratings_matrix)) if ratings_matrix[l][i] != 0]
            if len(l_item) == 0:
                mean = 0
            else:
                mean = np.mean(np.array(l_item))
            for j in range(len(ratings_matrix)):
                if ratings_matrix[j][i] == 0:
                    ratings_matrix[j][i] = mean
        return ratings_matrix
                