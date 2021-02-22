

def traj_num(n: int):
    """
    Задача о кузнечике. Кузнечик находится на числовой прямой в точке 1.
    Кузнечик может прыгать только вперед на расстояние +1 и +2.
    Сколько различных траекторий допрыгать из точки 1 в точку N.
    """
    # Пусть k(n) - количество траекторий для попадания в точку N
    # Так как в точку N мы можем попасть только из точек N-1 (прыжком на +1) и N-2 (прыжком на +2)
    # То k(n) = k(n-1) + k(n-2) - получили рекуррентную формулу
    # Крайний случай - В точку 1 можно попасть 1 способом, в точку 2 также одним
    # Также можно завести барьерный элемент - точку 0 в которую можно попасть 0 способов
    k = [0, 1] + [0] * n
    for i in range(2, n+1):
        k[i] = k[i-2] + k[i-1]
    return k[n]


def count_trajectories(n: int, allowed: list):
    """
    Задача о кузнечике №2.
    Кузнечик находится на числовой прямой в точке 1.
    Кузнечик может прыгать только вперед на расстояние +1, +2 и +3.
    Сколько различных траекторий допрыгать из точки 1 в точку N, при том что некоторые точки запрещены.
    Массив разрешенных точек хранится в списке allowed
    """
    # Пусть k(n) - количество траекторий для попадания в точку N
    # Так как в точку N мы можем попасть только из точек N-1 (прыжком на +1), N-2 (прыжком на +2) и N-3 (прыжком на +3)
    # То k(n) = k(n-1) + k(n-2) + k(n-3) - получили рекуррентную формулу
    # Крайний случай - В точку 1 можно попасть 1 способом, в точку 2 также одним (при условии что она разрешена)
    # Также можно завести барьерный элемент - точку 0 в которую можно попасть 0 способов
    k = [0, 1, int(allowed[2])] + [0] * (n-2)
    for i in range(3, n+1):
        if allowed[i]:
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[n]


# Минимальная стоимость достижения клетки N
# price[i] - цена за посещение клетки i
# C[i] - минимально возможная стоимость достижения клетки i
def count_min_cost(n: int, price: list):
    """
    Задача о кузнечике №3.
    Кузнечик может прыгать по числовой оси на +1 и +2
    :param n: Ноер точки в которую необходимо попасть
    :param price: список, в котором указаны стоимости посещения i-х клеток
    :return: Минимальная стоимость посещения клетки n
    """
    # Рекуррентная формула -  C[i] = price[i] + min(C[i-1], C[i-2])
    # C[1] = price[1]
    # C[2] = price[1] + price[2]
    C = [None, price[1], price[1] + price[2]] + [0] * (n-2)
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]