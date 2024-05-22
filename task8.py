import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    quarters = ['1 кв.', '2 кв.', '3 кв.', '4 кв.']
    sales_A = [780, 964, 550, 807]
    sales_B = [985, 736, 780, 674]
    sales_C = [570, 804, 630, 500]

    bar_width = 0.25
    index = np.arange(len(quarters))

    fig, ax = plt.subplots(figsize=(10, 6))
    bars_A = ax.bar(index - bar_width, sales_A, bar_width, label='A', color='#ff9999')
    bars_B = ax.bar(index, sales_B, bar_width, label='B', color='#66b3ff')
    bars_C = ax.bar(index + bar_width, sales_C, bar_width, label='C', color='#99ff99')

    ax.set_xlabel('Квартали')
    ax.set_ylabel('Об’єми продажу, тис. грн.')
    ax.set_title('Об’єми продажу підприємств, тис. грн.')
    ax.set_xticks(index)
    ax.set_xticklabels(quarters)
    ax.legend()

    plt.tight_layout()
    plt.savefig('task8.png')

    plt.show()