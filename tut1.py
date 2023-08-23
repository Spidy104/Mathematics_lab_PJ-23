import matplotlib.pyplot as plt
from math import exp
import numpy as np

def main():
    x = [i for i in range(20)]
    y = list(map(lambda i: exp(-i), x))
    plt.bar(x, y, color='k', label='All Devs')
    # graph.xlabel('X - axis')
    # graph.ylabel('Y - axis')
    plt.title("Exponential Graph")
    # plt.legend()
    plt.show()
    print(np.random.rand(2))


if __name__ == '__main__':
    main()
