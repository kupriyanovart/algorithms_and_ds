def generate_numbers(N:int, M:int = -1, prefix=None):
    """
    Выводит все числа в N-ричной системе счисления длиной M (с незначащими нулями) начиная с prefix
    :param N: Основание системы счисления
    :param M: Длина числа
    :param prefix: Начальное значение
    """
    M = N if M == -1 else M
    prefix = prefix or []  # Если в ф-ю не передали параметр prefix (используется значение по умолчанию), то prefix = []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
