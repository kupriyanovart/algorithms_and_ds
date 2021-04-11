from collections import deque

# Алгоритм поиска в ширину (Breadth First search)
# Нахождение минимального расстояния от исходной вершины графа до всех остальных

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

print(distances)
