def z_fun(s: str):
    '''
    Алгоритм нахождения z-функции строки s
    Подстрока, которая совпадает с префиксом строки s называется отрезок совпадения
    z[i] - длина длиннейшего (max) отрезка совпадения, который начинается с позиции i
    '''
    l = 0
    r = 0 
    n = len(s)
    z = [0] * n
    for i in range(1, n):
        if i <= r:
            # Выбираем начальное приближение z[i]
            z[i] = min(r - i + 1, z[i - l])
        # После выбора начального приближения вычисляем z[i] тривиальным алгоритмом
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if (i+z[i]-1 > r):
            l = i
            r = i+z[i]-1

    return z



def search_substring(s: str, sub: str):
    modified_string = sub + '#' + s
    prefix = z_fun(modified_string)
    res = []
    for i in range(len(prefix)):
        if prefix[i] == len(sub):
            res.append(i - len(sub) - 1)
    return res
