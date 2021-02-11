def bubble_sort_v1(A:list):
    N = len(A)
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j+1],  A[j] = A[j], A[j+1]
        print(f'Промежуточный итог: {A}')
            
# Если при проходе списка ничего не менялось, то список уже упорядочен 
# Выполняется намного быстрее на частично упорядоченных данных
def bubble_sort_v2(A:list):
    i = len(A) - 1
    is_not_ordered = True
    
    while is_not_ordered:
        is_not_ordered = False
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j+1],  A[j] = A[j], A[j+1]
                is_not_ordered = True
        j -= 1


L = [3, 1, 5, 4, 2]
print(L)
bubble_sort_v1(L)
print(L, '\n')
L = [3, 1, 5, 4, 2, 11, 15, 45, 111]
print(L)
bubble_sort_v2(L)
print(L)
