# F[i] = Длина наибольшей возрастающей подпоследовательности для части списка A: A[0:i], которая заканчивается и
# содержит элемент ai (A[i-1])
# F[i] = max(F[j]) + 1, при j<i, ai > aj
# F[0] = 1


def len_longest_increasing_subsequence(A: list):
    F = [0] * len(A)
    F[0] = 1
    for i in range(1, len(A)):
        m = 0
        for j in range(i):
            if A[j] < A[i] and F[j] > m:
                m = F[j]
        F[i] = m + 1
    return max(F)


a = [1, 2, 4, 2, 11, 12, 13, 15, 19]
print(len_longest_increasing_subsequence(a))
