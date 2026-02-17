def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    chunks = []
    i = 0
    if chunk_size > len(tokens):
        if len(tokens) == 0:
            return []
        else:
            return [[l for l in tokens]]
    while i < len(tokens) - chunk_size + 1:
        chunk = []
        for j in range(chunk_size):
            chunk.append(tokens[i])
            i += 1
        i = i - overlap 
        chunks.append(chunk)
    return chunks