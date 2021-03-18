# I. Варианты хранения графа в памяти

# 1. Матрица смежности
# O(N) на перебор соседей вершины v
# V = ['A', 'B', 'C', 'D']
#
# index = {V[i]: i for i in range(len(V))}

# A = [[0, 1, 0, 1],
#      [0, 0, 0, 1],
#      [0, 0, 0, 1],
#      [0, 0, 1, 0]
#      ]


def graph_adjacency_matrix(N: int, M: int):
    """
    Считывание графа с клавиатуры и представление его в памяти с помощью матрицы смежности
    :param N: Количество вершин графа
    :param M: Количество ребер
    :return: (V,index,A), где V - список вершин, index - словарь соотношения вершины и ее индекса, A - матрица смежности
    """
    V = []
    index = {}
    A = [[0]*N for i in range(N)]
    for i in range(M):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in index:
                V.append(v)
                index[v] = len(V) - 1
        v1_i = index[v1]
        v2_i = index[v2]
        A[v1_i][v2_i] = 1
        A[v2_i][v1_i] = 1

    return V, index, A


# 2. Списки смежности
# O(кол-во соседей) на перебор соседей вершины v
# G = {
#     'A': {'B'},
#     'B': {'A', 'C'},
#     'C': {'B', 'D'},
#     'D': {'C'}
# }


def graph_adjacency_list(N: int, M: int):
    """
    Считывание графа с клавиатуры и представление его в памяти с помощью списков смежности
    :param N: Количество вершин графа
    :param M: Количество ребер
    :return: G - граф представенный с помощью списков смежности
    """
    G = {}
    for i in range(M):
        v1, v2 = input().split()
        for v, u in (v1, v2), (v2, v1):
            if v not in G:
                G[v] = {u}
            else:
                G[v].add(u)
    return G

# 3. Компактное хранение графов (Для неизменяемых графов)
# Представим граф:
# 0: 1
# 1: 0, 2, 3
# 2: 1, 3
# 3: 1, 2, 4
# 4: 3
# Будем хранить все ребра в одном массиве:
# edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
# Также будем хранить список offset - список индексов смещений начала списка для каждой вершины
# offset[i] - начало списка смежности для i-й вершины
# offset = [0, 1, 4, 6, 9, 10]
# Список смежности лежит в срезе edges[offset[i] : offset[i+1]]


# Обход графа в глубину (Deep firt search - DFS)
def dfs(vertex, graph, used):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used)


# Подсчет количества компонент связности графа
def main():
    graph = graph_adjacency_list(4, 5)
    used = set()  # псевдокод used = стартовая вершина
    N = 0  # Количество компонент связности
    for vertex in graph:
        if vertex not in used:
            dfs(vertex, graph, used)
            N += 1

    print(N)

# Топологическая сортировка. Алгоритм Тарьяна
# Если орграф не содержит циклов, то его вершины можно пронумеровать так, что любое ребро идет от вершины
# с меньшим номером к вершине с большим номером

# u - число от 1 до N (индексы вершин)
# visited - [False] * (n+1)
# ans = []


def dfs_1(start, graph, visited, ans):
    visited[start] = True
    for u in graph[start]:
        if not visited[u]:
            dfs_1(u, graph, visited, ans)
    ans.append(start)


def main_1():
    N = 4
    M = N + 1
    graph = graph_adjacency_list(N, M)
    visited = [False] * (N+1)
    ans = []
    for i in range(1, N+1):
        if not visited[i]:
            dfs_1(i, graph, visited, ans)

    ans[:] = ans[::-1]
