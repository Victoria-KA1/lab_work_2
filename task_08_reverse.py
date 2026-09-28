def reverse_string(text):
    return text[::-1]


def main():
    text = input("Введите строку: ")
    print(f"Перевёрнутая строка: {reverse_string(text)}")


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")