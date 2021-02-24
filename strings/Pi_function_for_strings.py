# Функция проверки равенства строк s1==s2
def is_equal(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    for i in range(s1):
        if s1[i] != s2[i]:
            return False
    return True


# Наивный алгоритм поиска подстроки в строке

def substr(s: str, sub: str):
    for i in range(0, len(s) - len(sub) + 1):
        flag = True
        for j in range(len(sub)):
            if s[i+j] != sub[j]:
                flag = False
        if flag:
            print(i)


# Алгоритм Кнута-Мориса-Пратта
# https://brestprog.by/topics/prefixfunction/
# Префикс функция от строки s равна массиву prefix, где prefix[i] обозначает длину максимального префикса
# строки s[0..i], совпадающего с её суффиксом.
# Тривиальные случаи (префикс равен суффиксу и равен всей строке) не учитываются.
def kmp(s: str):
    prefix = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == s[prefix[i-1]]:
            prefix[i] = prefix[i-1] + 1
        else:
            j = prefix[prefix[i-1] - 1]
            while j > 0 and s[i] != s[j]:
                j = prefix[j - 1]
            prefix[i] = j + 1 if s[i] == s[j] else j
    return prefix


# алгоритм поиска подстроки в строке с использованием префикс функции

def search_substring(s: str, sub: str):
    modified_string = sub + '~' + s
    prefix = kmp(modified_string)
    res = []
    for i in range(len(prefix)):
        if prefix[i] == len(sub):
            res.append(i - 2 * len(sub))
    return res


print(search_substring('abcdabcshshabc1231abcdef', 'abc'))
