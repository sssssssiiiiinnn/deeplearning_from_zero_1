import numpy as np


def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x - np.maximum(x))  # Prevent oveflow
    return exp_x / sum_exp_x
