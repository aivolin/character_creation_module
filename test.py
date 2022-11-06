from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculateSquareRoot(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number) -> float:
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    print("Мы вычислили квадратный корень"
          " из введённого вами числа. "
          f"Это будет: {calculateSquareRoot(your_number)}")


print(message)
calc(25.5)
