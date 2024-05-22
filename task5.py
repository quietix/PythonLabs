import matplotlib.pyplot as plt
import numpy as np


def setup_axs(axs, index, position: tuple):
    row = position[0]
    col = position[1]
    axs[row, col].set_title(f'Function {index}')
    axs[row, col].set_xlabel('x')
    axs[row, col].set_ylabel('y')
    axs[row, col].grid(True)
    axs[row, col].legend()


if __name__ == "__main__":
    x1 = np.linspace(-3, 3, 400)
    y1 = 2**x1 * np.sin(10 * x1)

    x2 = np.linspace(0, 5, 400)
    y2 = np.sqrt(x2) * np.sin(10 * x2)

    x3 = np.linspace(-2, 2, 400)
    y3 = (x3**3) * np.cos(x3**2)

    x4 = np.linspace(-2, 2, 400)
    y4 = (x4**3) + np.cos(15 * x4)

    x5 = np.linspace(0, 5, 400)
    y5 = -5 * np.cos(10 * x5) * np.sin(3 * x5) / (x5**x5)

    x6 = np.linspace(0, 8, 400)
    y6 = 5 * np.sin(10 * x6) * np.sin(3 * x6) / (x6**x6)

    fig, axs = plt.subplots(3, 2, figsize=(12, 7))

    axs[0, 0].plot(x1, y1, 'r', label='$y = 2^x \cdot \sin(10x)$')
    setup_axs(axs, 1, (0, 0))

    axs[0, 1].plot(x2, y2, 'g', label='$y = x^{1/2} \cdot \sin(10x)$')
    setup_axs(axs, 2, (0, 1))

    axs[1, 0].plot(x3, y3, 'b', label='$y = x^3 \cdot \cos(x^2)$')
    setup_axs(axs, 3, (1, 0))

    axs[1, 1].plot(x4, y4, 'y', label='$y = x^3 + \cos(15x)$')
    setup_axs(axs, 4, (1, 1))

    axs[2, 0].plot(x5, y5, 'm', label='$y = -5 \cdot \cos(10x) \cdot \sin(3x) / (x^x)$')
    setup_axs(axs, 5, (2, 0))

    axs[2, 1].plot(x6, y6, 'c', label='$y = 5 \cdot \sin(10x) \cdot \sin(3x) / (x^x)$')
    setup_axs(axs, 6, (2, 1))

    plt.tight_layout()

    plt.show()
