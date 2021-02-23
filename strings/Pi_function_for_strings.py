# Функция проверки равенства строк s1==s2
def is_equal(s1: str, s2: str):
    if len(s1) != len(s2):
        return False
    for i in range(s1):
        if s1[i] != s2[i]:
            return False
    return True

