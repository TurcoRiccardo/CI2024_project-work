# Copyright © 2024 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computational-intelligence
# Free under certain conditions — see the license for details.

import numpy as np

# All numpy's mathematical functions can be used in formulas
# see: https://numpy.org/doc/stable/reference/routines.math.html


def f0(x: np.ndarray) -> np.ndarray:
    return x[0] + np.sin(x[1]) / 5

def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray:
    return (x[1]**(x[0] + 11)) / (x[1]**(-(x[0] - x[2])))

def f3(x: np.ndarray) -> np.ndarray:
    return np.exp(4) + (-((12 + 4) * x[0]) / (x[1] + 1)) - np.exp(np.abs(x[1])) / x[2]

def f4(x: np.ndarray) -> np.ndarray:
    return np.cos(np.exp(x[1]*x[0])) + np.exp(np.exp(((x[1] - 3) / (3 * x[0])) - 2))

def f5(x: np.ndarray) -> np.ndarray:
    return x[0] - x[0]

def f6(x: np.ndarray) -> np.ndarray:
    return (np.sin(x[1]) * x[0]) + (np.cos((x[1] / x[1])) - 5)

def f7(x: np.ndarray) -> np.ndarray:
    return np.sqrt(3 / 4) + x[1] + np.sqrt(x[0] * 8) + x[1]

def f8(x: np.ndarray) -> np.ndarray:
    return (np.exp(x[0] - np.sin(5)) + ((x[5] + np.sin(x[2])) / np.cos(x[0])) - (12*6*(x[4] + 7) + 11**x[5])) / (- np.sin(np.sin(np.sin(x[4])) + x[5] - (np.sin(x[2]) / x[0])))