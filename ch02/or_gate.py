import numpy as np


def OR(x1, x2):
    w = np.array([0.5, 0.5])
    x = np.array([x1, x2])
    b = -0.2
    temp = np.sum(w * x) + b

    if temp <= 0:
        return 0
    else:
        return 1
