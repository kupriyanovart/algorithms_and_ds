def generate_permutations(N:int, M:int = -1, prefix=None):
    """
    Генерация всех перестановок N чисел в M позициях с префиксом prefix
    :param N: Количество чисел для перестановки
    :param M: Длина числа
    :param prefix: Префикс
    """
    assert N >= M, 'Чисел для перестановки необходимо не меньше чем позиций в которых надо переставлять (N >= M)'
    M = N if M == -1 else M
    prefix = prefix or []  # Если в ф-ю не передали параметр prefix (используется значение по умолчанию), то prefix = []
    if M == 0:
        print(prefix)
        return
    for digit in range(1, N + 1):
        if digit not in prefix:
            prefix.append(digit)
            generate_permutations(N, M-1, prefix)
            prefix.pop()


if __name__ == '__main__':
    generate_permutations(3)
