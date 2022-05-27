import numpy as np
import matplotlib.pyplot as plt


def progon_method(A, B, C, F):


    if A[0] != 0:
        alpha = np.zeros(len(F) - 1)
        gamma = np.zeros(len(F) - 1)
        Y = np.zeros(len(F))
        alpha[0]  = C[0] / B[0]
        gamma[0] = F[0] / B[0]

        for i in range(1, len(F) - 1):
            coeff = B[i] - alpha[i - 1] * A[i]
            assert coeff != 0
            alpha[i] = C[i] / coeff
            gamma[i] = (F[i] - A[i] * gamma[i - 1]) / coeff

        Y[-1] = (F[-1] - A[-1] * gamma[-1]) / (B[-1] - A[-1] * alpha[-1])
        for i in range(len(F) - 2, -1, -1):
            Y[i] = gamma[i] - alpha[i] * Y[i + 1]
        return Y
    else:
        print('A[0] == 0')


coef, g = 20, 2
a, b, d1, d2 = 1, 3, 0, 4


# з врахуванням заміни функції u(x) (крайові умови повинні бути 0)

def f(x):
    return 2 * x + np.tanh(x ** 2) - 2 * p(x) * (x - 1) + 2 * x ** 3 / 5


def p(x):
    return 2 * x / (x ** 2 + 2)


def r(x):
    return 0


def k(x):
    return (coef + x ** (2 * g)) / coef


h = 0.025  # h / 2
X = np.arange(a, b + 2 * h, 2 * h)  # точка t є одним із вузлів

A = (-k(X[1:-2] - h) - h * r(X[1:-2] - h) + h ** 2 * p(X[1:-2] - h)) / 2 / h  # під діагоналлю
B = (
        (k(X[1:-1] - h) + k(X[1:-1] + h) + h * (r(X[1:-1] - h) - r(X[1:-1] + h)) +
         h ** 2 * (p(X[1:-1] - h) + p(X[1:-1] + h))) / 2 / h
)  # головна діагональ
C = (-k(X[1:-2] + h) + h * r(X[1:-2] + h) + h ** 2 * p(X[1:-2] + h)) / 2 / h  # над діагоналлю
F = h * (f(X[1:-1] - h) + f(X[1:-1] + h))

Y = progon_method(A, B, C, F)
Y = np.hstack([[0], Y, [0]]) + 12 * (1 - X)

plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
