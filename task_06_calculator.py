def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Неизвестная операция"


def main():
    print("Простой калькулятор")
    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))
    result = calculate(a, b, op)
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")