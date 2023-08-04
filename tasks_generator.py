import random
import fractions
import math
from sympy import *


def generator_random_point():
    random_point = random.randint(1, 10)
    return random_point

"Задача № 13274"
def derivative_of_tangent_in_random_point():
    random_point = generator_random_point()
    x = Symbol('x')
    expr = (1 + (tan(2*x))**2)**3
    prime = expr.diff(x)
    result = simplify(prime)
    answer = result.subs(x, pi/random_point)
    task = f'Вычислите: \(diff_{expr}; x={pi/random_point}\)'
    return answer, task

"Задача № 42911"
def derivative_of_sqrt_in_random_point():
    random_point = generator_random_point()
    x = Symbol('x')
    expr = sqrt(x)
    prime = expr.diff(x)
    answer = prime.subs(x, random_point)
    task = f'Вычислите: \(diff_{expr}; x={random_point}\)'
    return answer, task

"Задача № 3034"
def critical_point():
    x = Symbol('x')
    expr = x**2 + 4*x + 5
    prime = expr.diff(x)
    answer = solveset(Eq(prime, 0), x)
    task = f'Вычислите: \(critical_point_{expr}\)'
    return answer, task

task_1 = derivative_of_tangent_in_random_point()
task_2 = derivative_of_sqrt_in_random_point()
task_3 = critical_point()

stack_of_functions = [task_1, task_2, task_3]

def derivative_tasks_generator():
    answer = random.choice(stack_of_functions)
    return answer


if __name__ == "__main__":
    ...





