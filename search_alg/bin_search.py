from random import randint

def left_bound(A: list, key: float):
    """
    Реализация бинарного поиска индекса левой границы вхождения ключевого элемента key в предварительно отсортированном массиве A (по неубыванию)
    """ 
    left = -1
    right = len(A)
    
    while right - left > 1:
        middle = (right + left) // 2
        if key > A[middle]:
            left = middle
        else:
            right = middle
    return left
    
    
def right_bound(A: list, key: float):
    """
    Реализация бинарного поиска индекса правой границы вхождения ключевого элемента key в предварительно отсортированном массиве A (по неубыванию)
    """ 
    left = -1
    right = len(A)
    
    while right - left > 1:
        middle = (right + left) // 2
        if key >= A[middle]:
            left = middle
        else:
            right = middle
    return right


def bin_search(A: list, key: float):
    """
    Реализация бинарного поиска индекса первого вхождения элемента key в список A, если искомого элемента в списке нет, то вывод -1
    Требование: Список предварительно отсортированный (по неубыванию)
    """
    left = -1
    right = len(A)
    
    while right - left > 1:
        middle = (right + left) // 2
        if key > A[middle]:
            left = middle
        else:
            right = middle
    if A[left] != key:
        return -1
    return left

