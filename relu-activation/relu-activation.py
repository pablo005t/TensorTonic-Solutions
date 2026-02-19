import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.array(x)
    relu =  np.where(x>0 ,x , 0)
    return relu