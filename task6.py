import matplotlib.pyplot as plt


def draw_pie_chart(task_num=6, inner_radius=1):
    companies = ['A', 'B', 'C']
    profits = [4523, 9531, 2715]
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    plt.figure(figsize=(8, 8))
    plt.pie(profits, labels=companies, autopct='%1.1f%%', colors=colors, startangle=90, counterclock=False, wedgeprops=dict(width=inner_radius))
    plt.title('Валовий прибуток підприємств, тис. грн.')
    plt.legend(loc="best")
    plt.savefig(f'task{task_num}.png')
    plt.show()


if __name__ == "__main__":
    plt = draw_pie_chart()
