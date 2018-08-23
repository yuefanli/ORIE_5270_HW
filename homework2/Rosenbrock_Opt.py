import numpy as np
from scipy.optimize import minimize


class Rosenbrock(object):
    def __init__(self):
        pass

    @staticmethod
    def func(x):
        """
        :param x: np.array([double,double]) x with size nx1
        :return f: double, function value of Rosenbrock
        """
        N = len(x)
        x_i_1 = x[1: N]
        x_i = x[0: (N - 1)]
        f = np.sum(100.0 * (x_i_1 - x_i * x_i) ** 2 + (1 - x_i) ** 2)
        return f

    @staticmethod
    def grad(x):
        """
        :param x: np.array([double,double]) x with size nx1
        :return grad: [double, double] 1xn value of gradient
        """
        N = len(x)
        grad = []
        for i in range(N):
            if i == 0:
                g = 400 * (x[i] ** 3) - 400 * x[i] * x[i + 1] + 2 * x[i] - 2
            elif i > 0 and i < N - 1:
                g = 200 * (x[i] - x[i - 1] ** 2) + 400 * (x[i] ** 3) - 400 * x[i] * x[i + 1] + 2 * x[i] - 2
            elif i == N - 1:
                g = 200 * (x[i] - x[i - 1] ** 2)
            grad.append(g)
        grad = np.array(grad)
        return grad


if __name__ == '__main__':
    x = []
    n_1 = 20
    x_1 = [10 for i in range(n_1)]
    x.append(x_1)
    x_2 = [5, 2, 7, -9, 0, 12]
    x.append(x_2)
    x_3 = [-100 for i in range(n_1)]
    x.append(x_3)
    x_4 = [4, 100, 10000, 0, 20, 40]
    x.append(x_4)
    result_all = []
    for i in range(4):
        result = minimize(Rosenbrock.func, x[i], method='BFGS', jac=Rosenbrock.grad)
        result_all.append(result.fun)
        print(result)
    min_val = np.min(result_all)
    print('Smallest value for Rosenbrock function: ', min_val)
