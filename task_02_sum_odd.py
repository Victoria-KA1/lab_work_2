def sum_odd_numbers(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total


def main():
    n = int(input("Введите N: "))
    print(f"Сумма нечётных чисел от 1 до {n}: {sum_odd_numbers(n)}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")