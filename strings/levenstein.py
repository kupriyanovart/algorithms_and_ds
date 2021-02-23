# Функция нахождения минимального редакционного расстояния
# Расстояние Левенштейна
from pprint import pprint


def levenstein(s1: str, s2: str):
    # F[i][j] - минимальное редакционное растояние между s1[:i] и s2[:j]
    # Созадим массив F сразу с крайними случаями (если i или j == 0, то F[i][j] = i+j
    F = [[i+j if i*j == 0 else 0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1 + min(F[i-1][j-1], F[i][j-1], F[i-1][j])
    pprint(F)

    return F[-1][-1]


print(levenstein('avc233', 'avc123c'))

