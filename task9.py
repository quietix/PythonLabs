import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    quarters = ['1 кв.', '2 кв.', '3 кв.', '4 кв.']
    sales_A = [780, 964, 550, 807]
    sales_B = [985, 736, 780, 674]
    sales_C = [570, 804, 630, 500]

    bar_width = 0.25
    bar_height = 0.25
    index = np.arange(len(quarters))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 9))

    bars_A_h = ax1.barh(index - bar_height, sales_A, bar_height, label='A', color='#ff9999')
    bars_B_h = ax1.barh(index, sales_B, bar_height, label='B', color='#66b3ff')
    bars_C_h = ax1.barh(index + bar_height, sales_C, bar_height, label='C', color='#99ff99')

    ax1.set_ylabel('Квартали')
    ax1.set_xlabel('Об’єми продажу, тис. грн.')
    ax1.set_title('Горизонтальна групова діаграма об’ємів продажу підприємств')
    ax1.set_yticks(index)
    ax1.set_yticklabels(quarters)
    ax1.legend()

    bars_A = ax2.bar(index, sales_A, bar_width, label='A', color='#ff9999')
    bars_B = ax2.bar(index, sales_B, bar_width, bottom=sales_A, label='B', color='#66b3ff')
    bars_C = ax2.bar(index, sales_C, bar_width, bottom=np.array(sales_A) + np.array(sales_B), label='C',
                     color='#99ff99')

    ax2.set_xlabel('Квартали')
    ax2.set_ylabel('Об’єми продажу, тис. грн.')
    ax2.set_title('Складена групова діаграма об’ємів продажу підприємств')
    ax2.set_xticks(index)
    ax2.set_xticklabels(quarters)
    ax2.legend()

    plt.tight_layout()
    plt.savefig('task9.png')

    plt.show()