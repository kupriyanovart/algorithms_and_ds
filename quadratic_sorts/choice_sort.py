def choice_sort_v1(A:list):
    N = len(A)
    # Среди элементов A[i:] выбираем наименьший 
    # Сохраняем его индекс в переменной min_id
    for i in range(0, N-1):
        min_id = i
        for k in range(i + 1, N):
            if A[k] < A[min_id]:
                min_id = k
        # Теперь поставим A[min_idx] на место A[i] 
        print(f'i = {i}, min_id = {min_id}')
        A[i], A[min_id] = A[min_id], A[i]
        print('промежуточный итог: ', A)


def choice_sort_v2(A:list):
    N = len(A)
    # Среди элементов A[i:] выбираем наименьший 
    for i in range(0, N-1):
        min_id = i
        for k in range(i+1, N):
            # Не запоминая индекс минимального элемента
            # меняем местами очередной элемент A[k],
            # если A[k] < A[min_id]
            if A[k] < A[min_id]:
                print(f'i = {i}, min_id = {min_id}')
                A[min_id], A[k] = A[k], A[min_id]
                print('промежуточный итог: ', A)

L = [1, 3, 3, 2, 5, 1]
print('Начальное состояние: ', L, '\n\n')
choice_sort_v1(L)
print(L)
print()        
L = [1, 3, 3, 2, 5, 1]
print('Начальное состояние: ', L, '\n\n')
choice_sort_v2(L)
print(L)
