import numpy as np


def AND(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -0.7
    temp = np.sum(w * x) + b

    if temp <= 0:
        return 0
    else:
        return 1