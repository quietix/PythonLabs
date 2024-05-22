import matplotlib.pyplot as plt


def compute_y(x):
    return x + 9


if __name__ == "__main__":
    x_values = [1, 2, 3, 4, 5]

    y_values = [compute_y(x) for x in x_values]

    plt.figure(figsize=(10, 6))

    plt.plot(x_values, y_values, label='y = x + 9', color='blue', linestyle='-', linewidth=2)

    plt.title('Лінійний графік: y = x + 9', fontsize=16)

    plt.xlabel('Значення x', fontsize=14)
    plt.ylabel('Значення y', fontsize=14)

    plt.legend(loc='upper left', fontsize=12)

    plt.grid(True, linestyle='--')

    plt.show()