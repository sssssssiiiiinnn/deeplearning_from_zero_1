import numpy as np
import matplotlib.pyplot as plt


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)


if __name__ == "__main__":
    f = lambda x: 0.01*x**2 + 0.1*x
    x = np.arange(0.0, 20.0, 0.1)
    print(numerical_diff(f, 5))
    print(numerical_diff(f, 10))
    # plt.xlabel("x")
    # plt.ylabel("f(x")
    # plt.plot(x, f(x))
    # plt.show()