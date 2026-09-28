import json


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def load_from_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    student = {
        "name": "Виктория",
        "group": "221141",
        "variant": 6,
        "grades": [5, 4, 5, 5]
    }

    save_to_json(student, "student.json")
    print("Данные сохранены в student.json")

    loaded = load_from_json("student.json")
    print("Загруженные данные:", loaded)


if __name__ == "__main__":
    main()
    input("Нажмите Enter для выхода...")