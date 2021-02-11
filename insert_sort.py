def insert_sort(A:list):
    N = len(A)
    for i in range(1, N):
        j = i - 1
        # В new_elem сохранили значение A[i]
        new_elem = A[i]
        # Все элементы находящиеся до A[i], 
        # значение которых больше чем new_elem
        while j >= 0 and A[j] > new_elem:
            # сдвигаем вправо на 1       
            A[j+1] = A[j]
            j -= 1
        # На свободное место записывем new_elem
        A[j+1] = new_elem
        print(f'Промежуточный итог - {A}')

L = [3, 1, 5, 4, 2]
print(L)
insert_sort(L)
print(L)
