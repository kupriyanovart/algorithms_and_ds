from time import time


# Первый вариант декоратора для измерения времени выполнения рекурсивной функции
def fun_exec_time_v1(function, currently_evaluating=None):
    if currently_evaluating is None:
        currently_evaluating = set()

    def wrapper_function(*args, **kwargs):
        if function in currently_evaluating:
            return function(*args, **kwargs)

        t1 = time()
        currently_evaluating.add(function)
        try:
            value = function(*args, **kwargs)
        finally:
            currently_evaluating.remove(function)
        t2 = time()
        print('time taken', t2 - t1)
        return value
    return wrapper_function


# Второй вариант декоратора для измерения времени выполнения рекурсивной функции
def fun_exec_time_v2(function):
    is_evaluating = False

    def wrapper_function(*args, **kwargs):
        nonlocal is_evaluating
        if is_evaluating:
            return function(*args, **kwargs)

        t1 = time()
        is_evaluating = True
        try:
            value = function(*args, **kwargs)
        finally:
            is_evaluating = False
        t2 = time()
        print(f'time taken for function {function.__name__}:', t2 - t1)
        return value
    return wrapper_function


@fun_exec_time_v2
def fib_rec(n: int):
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)


@fun_exec_time_v2
def fib_dynamic(n: int):
    if n <= 1:
        return n
    x = y = 1
    for i in range(3, n+1):
        x, y = x + y, x
    return x


print(fib_rec(30))
print(fib_dynamic(35000))