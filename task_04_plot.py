import matplotlib.pyplot as plt


def build_plot():
    x_values = list(range(-10, 11))
    y_values = [x ** 2 for x in x_values]

    plt.plot(x_values, y_values, marker="o", color="blue")
    plt.title("График y = x^2")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.savefig("plot.png")
    plt.show()


if __name__ == "__main__":
    build_plot()
    input("Нажмите Enter для выхода...")