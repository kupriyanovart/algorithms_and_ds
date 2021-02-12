def factorial(n:int):
    assert n > 0, 'Факториал для отрицательных чисел не определен'
    if n == 1:
        return 1
    return factorial(n-1) * n
