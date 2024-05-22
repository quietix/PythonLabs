import numpy as np

if __name__ == "__main__":
    array = np.random.randint(0, 10, size=(4, 6))
    print("Оригінальний масив:")
    print(array)

    with open('task1.txt', 'w') as file:
        file.write("Оригінальний масив:\n")
        file.write(np.array_str(array) + "\n\n")

        sorted_array = np.sort(array, axis=1)
        print("Відсортований масив по рядках:")
        print(sorted_array)
        file.write("Відсортований масив по рядках:\n")
        file.write(np.array_str(sorted_array) + "\n\n")

        min_value = np.min(array)
        print(f"Мінімальне значення в масиві: {min_value}")
        file.write(f"Мінімальне значення в масиві: {min_value}\n\n")

        sum_value = np.sum(array)
        print(f"Сума всіх елементів масиву: {sum_value}")
        file.write(f"Сума всіх елементів масиву: {sum_value}\n\n")

        mean_value = np.mean(array)
        print(f"Середнє значення всіх елементів масиву: {mean_value}")
        file.write(f"Середнє значення всіх елементів масиву: {mean_value}\n\n")
