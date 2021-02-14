def merge_v1(a: list, b: list):
    """
    Слияние двух отсортированных массивов
    """
    c = [0] * (len(a) + len(b))
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            n += 1
            i += 1
        else:
            c[n] = b[k]
            n += 1
            k += 1
    while i < len(a):
        c[n] = a[i]
        n += 1
        i += 1
    while k < len(b):
        c[n] = b[k]
        n += 1
        k += 1
    return c


def merge_v2(a: list, left: int, middle: int, right: int):
    """
    Слияние части массива начиная с индекса left до индекса middle (не включая)
    c частью массива начиная с middle до right (не включая)
    """
    tmp = []
    i, k = left, middle
    while i < middle and k < right:
        if a[i] <= a[k]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[k])
            k += 1
    while i < middle:
        tmp.append(a[i])
        i += 1
    while k < right:
        tmp.append(a[k])
        k += 1
    for j in range(left, right):
        a[j] = tmp[j - left]


def merge_sort(a: list, left=0, right=None):
    """
    Сортировка массива слиянием
    :param a: Сортируемый массив
    :param left: Левая граница сортировки
    :param right: Правая граница сортировки
    """
    right = right or len(a)
    if right - left <= 1:
        return

    middle = (left + right) // 2
    merge_sort(a, left, middle)
    merge_sort(a, middle, right)
    merge_v2(a, left, middle, right)


if __name__ == '__main__':
    mas = [15, 1, 14, 5, 99, 100, 10, 15, 34, 2, 2, 2, 3, 13, 48, 55, 66]
    print(mas)
    merge_sort(mas)
    print(mas)