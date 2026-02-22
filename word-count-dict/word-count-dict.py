def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    cont = {}
    if len(sentences) == 0:
        return cont
    else:
        voc = []
        for sentence in sentences:
            for w in sentence:
                voc.append(w)
        for sentence in sentences:
            for w in sentence:
                if w not in list(cont.keys()):
                    cont[w] = 1
                else:
                    cont[w] = cont[w]+1
        return cont