from collections import deque


# Алгоритм поиска в ширину (Breadth First search)
# Нахождение минимального расстояния от исходной вершины графа до всех остальных
def bfs():
    N, M = map(int, input().split())  # Считываем количество вершин и количество ребер
    graph = {i: set() for i in range(N)}  # Граф будем хранить в виде словаря со множествами
    for i in range(M):
        v1, v2 = map(int, input().split())  # Считываем ребро
        graph[v1].add(v2)  # Добавляем смежность двух вершин
        graph[v2].add(v2)

    distances = [None] * N  # Массив расстояний (они заранее неизвестны)
    start_vertex = 0  # Начинаем с 0 вершины
    distances[start_vertex] = 0  # Расстояние до себя же равно 0
    queue = deque([start_vertex])  # Создаем очередь

    while queue:  # Пока очередь не пуста
        cur_v = queue.popleft()  # Достаем первый элемент
        for neigh_v in graph[cur_v]:  # Проходим всех его соседей
            if distances[neigh_v] is None:  # Если сосед еще не посещен (Расстояние => None)
                distances[neigh_v] = distances[cur_v] + 1  # Считаем расстояние
                queue.append(neigh_v)  # Добавляем в очередь, чтобы проверить и его соседей


# https://www.youtube.com/watch?v=S-hjsamsK8U&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=37
# Приложения к алгоритму поиска в ширину
# 1. Выделение компонент связности
# 1.1 Полагаем количество компонент связности равное 0
# 1.2 Начинаем обход в ширину произвольной вершины
# 1.3 Когда обход завершается увеличиваем кол-во компонент связности на 1
# 1.4 Если остались не посещенные вершины, повторяем шаги 2-3, сохраняя при этом массив посещенных used
# 1.5 Если все вершины посещены, то завершаем алгоритм
# Время данного алгоритма O(N+M)


# 2. Восстановление кратчайшего пути
def bfs_shortest_way():
    N, M = map(int, input().split())  # Считываем количество вершин и количество ребер
    graph = {i: set() for i in range(N)}  # Граф будем хранить в виде словаря со множествами
    for i in range(M):
        v1, v2 = map(int, input().split())  # Считываем ребро
        graph[v1].add(v2)  # Добавляем смежность двух вершин
        graph[v2].add(v2)

    distances = [None] * N  # Массив расстояний (они заранее неизвестны)
    start_vertex = 0  # Начинаем с 0 вершины
    distances[start_vertex] = 0  # Расстояние до себя же равно 0
    queue = deque([start_vertex])  # Создаем очередь

    parents = [None] * N  # Будем запоминать для каждой вершины ее предка

    while queue:  # Пока очередь не пуста
        cur_v = queue.popleft()  # Достаем первый элемент
        for neigh_v in graph[cur_v]:  # Проходим всех его соседей
            if distances[neigh_v] is None:  # Если сосед еще не посещен (Расстояние => None)
                distances[neigh_v] = distances[cur_v] + 1  # Считаем расстояние
                queue.append(neigh_v)  # Добавляем в очередь, чтобы проверить и его соседей
                parents[neigh_v] = cur_v  # Добавляем потомка для каждой вершины

    end_vertex = int(input())  # Получаем вершину путь от корня до которой необходимо восстановить
    path = [end_vertex]  # Путь до вершины
    parent = parents[end_vertex]  # Берем родителя вершины
    while parent is not None:  # Пока не дошли до корневой вершины (родитель корневой вершины - None)
        path.append(parent)  # Добавляем предка в путь
        parent = parents[parent]  # Предком становиться предок текущего предка

    print(parents)
    print(f'path from {end_vertex} to 0 is: ', path[::-1])


# 3. Восстановление траектории шахматного коня
# По каким клеткам должен пройти конь, чтобы попасть из клетки А(например d4) в клетку Б(например f7) наиболее быстро
# 3.1 Сводим задачу к графу
# 3.2 Обход в ширину из одной точки в другую

def create_chess_graph():
    letters = 'abcdefgh'
    numbers = '12345678'
    graph = dict()
    graph = {l+n: set() for l in letters for n in numbers}


    # Заполнение графа ребрами (для каждой ячейки смежными считаются ребра в которые конь может дойти за 1 ход)
    for i in range(len(letters)):
        for j in range(len(numbers)):
            v1 = letters[i] + numbers[j]
            for i_modified, j_modified in (i + 2, j + 1), (i - 2, j + 1), (i + 1, j + 2), (i - 1, j + 2):
                if 0 <= i_modified < len(letters) and 0 <= j_modified < len(numbers):
                    v2 = letters[i_modified] + numbers[j_modified]
                    graph[v1].add(v2)  # Добавляем смежность двух вершин
                    graph[v2].add(v2)
    return graph


def chess_horse(start_vertex, end_vertex):
    graph = create_chess_graph()
    parents = {v: None for v in graph}
    distances = {v: None for v in graph}

    distances[start_vertex] = 0
    queue = deque([start_vertex])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] is None:
                distances[v] = distances[u] + 1
                parents[v] = u
                queue.append(v)

    path = [end_vertex]
    parent = parents[end_vertex]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    print(path[::-1])


chess_horse('d4', 'f7')