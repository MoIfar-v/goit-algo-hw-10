import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import math

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


def monte_carlo_integral(f, a, b, n=100000):
    # Випадкові точки у [a, b]
    xs = np.random.uniform(a, b, n)
    ys = f(xs)

    # Оцінка інтеграла
    estimate = (b - a) * np.mean(ys)

    # Оцінка похибки (стандартна помилка)
    var_f = np.var(ys, ddof=1)
    std_error = (b - a) * math.sqrt(var_f / n)

    return estimate, std_error


if __name__ == "__main__":
    a = 0  # Нижня межа
    b = 2  # Верхня межа

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

    # Визначте функцію, яку потрібно інтегрувати, наприклад, f(x) = x^2
    def f(x):
        return x**2

    # Визначте межі інтегрування, наприклад, від 0 до 1
    a = 0  # нижня межа
    b = 2  # верхня межа
    
    a, b = 0, 2
    n = 100000

    estimate, std_error = monte_carlo_integral(f, a, b, n)
    exact, error = spi.quad(f, a, b)
    abs_error = abs(estimate - exact)

    print(f"Monte Carlo estimate: {estimate:.10f}")
    print(f"Standard error: {std_error:.10f}")
    print(f"Exact integral: {exact:.10f}")
    print(f"Absolute error: {abs_error:.10f}")