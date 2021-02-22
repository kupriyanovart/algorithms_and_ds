# A, B - Массивы чисел, где len(A) == N, len(B) == M
# Подпоследовательность A - Список C, содержащий элементы A в исходном порядке, но, возможно, не все
# F[i][j] - длина наибольшей возможной подпоследовательности частей A и B - A[0:i], B[0:j]


def largest_common_subsequence(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    sub_seq = []
    i = len(A)
    j = len(B)
    while i > 0 and j > 0:
        if A[i - 1] == B[j - 1]:
            sub_seq.append(A[i - 1])
            i -= 1
            j -= 1
        elif F[i - 1][j] == F[i][j]:
            i -= 1
        else:
            j -= 1
    sub_seq.reverse()
    return sub_seq


A = [1, 2, 3, 4, 5, 6, 11, 12, 12]
B = [2, 4, 6, 13]
print(largest_common_subsequence(A, B))
