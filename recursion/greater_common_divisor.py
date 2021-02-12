# Медленный вариант из-за возможной слишком высокой глубины вложенности
# Нахождение НОД методом вычитания
def gcd_v1(a:int, b:int):
    if a == b:
        return a
    elif a > b:
        return gcd_v1(a-b, b)
    else: # b > a
        return gcd_v1(b-a, a)


# Нахождение НОД делением
def gcd_v2(a:int, b:int):
    # крайний случай
    if b == 0:
        return a
    # рекуррентный случай
    return gcd_v2(b, a % b)
