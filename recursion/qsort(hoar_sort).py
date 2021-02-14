def hoar_sort(a: list):
    if len(a) <= 1:
        return
    barrier = a[0]
    L = []
    M = []
    R = []
    for x in a:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L+M+R:
        a[k] = x
        k += 1


if __name__ == '__main__':
    mas = [15, 1, 14, 5, 99, 100, 10, 15, 34, 2, 2, 2, 3, 13, 48, 55, 66]
    print(mas)
    hoar_sort(mas)
    print(mas)