import numpy as np
import matplotlib.pyplot as plt


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        temp_val = x[idx]
        x[idx] = temp_val + h
        fxh1 = f(x)  # f(x + h)

        x[idx] = temp_val -h
        fxh2 = f(x)  # f(x - h)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = temp_val

    return grad
