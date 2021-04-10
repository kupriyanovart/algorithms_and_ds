import queue


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
    for i in range(0, N):  # Добавляем для хранения изолированных вершин
        if str(i) not in G:
            G[str(i)] = set()
    return G


def bfs(vertex, graph, used, q: queue.Queue):
    """
    Алгоритм поиска в ширину. Минимальное расстоянием между любыми двумя вершинами простого связного графа РАВНО
    расстоянию между этими же вершинами в остовном дереве (которое получена с помощью алгоритма поиска в ширину
    :param vertex: Начальная вершина
    :param graph: Исходный граф
    :param used: Множество посещенных вершин
    :param q: Очередь вершин
    :return: Остовное дерево с корнем в вершине vertex (а также у которого сохраняется минимальная длина пути между
    любыми двумя вершинами
    """
    res = {}
    q.put(vertex)
    used.add(vertex)

    while not q.empty():  # На каждом шаге пока очередь не пуста
        next_vertex = q.get()  # Вынимаем вершину из очереди и смотрим ее смежные вершины
        used.add(next_vertex)  # Помечаем вершину
        for neighbour in graph[next_vertex]:  # Все смежные вершины с текущей помечаем и кладем в очередь
            if neighbour not in used:  # (если они еще не помечены)
                q.put(neighbour)
                used.add(neighbour)
                for v, u in (next_vertex, neighbour), (neighbour, next_vertex):  # Строим остовное дерево
                    if v not in res:
                        res[v] = {u}
                    else:
                        res[v].add(u)
    return res


# С помощью алгоритма поиска в глубину опеределяем расстояние между каждой из вершин и корнем дерева
def dfs(vertex, graph, used, res, k=0):
    used.add(vertex)
    res[vertex] = k
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs(neighbour, graph, used, res, k+1)


def main():
    """
    На вход программе подаётся описание простого связного графа. Первая строка содержит два числа: число вершин V
    и число рёбер E  графа. Следующие E строк содержат номера пар вершин, соединенных рёбрами.
    Вершины имеют номера от 0 до V-1.
    Выведите список из V чисел — расстояний от вершины 0 до соответствующих вершин графа.
    """
    V, E = map(int, input().split())
    graph = graph_adjacency_list(V, E)
    used = set()
    q = queue.Queue()
    res = bfs('0', graph, used, q)
    used = set()
    result = {}
    dfs('0', res, used, res=result)
    for i in range(V):
        print(result[str(i)], end=' ')


main()
