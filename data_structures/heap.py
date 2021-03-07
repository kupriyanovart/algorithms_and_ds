class Heap:
    """
    Структура данных Куча (Heap)
    Элементы в куче хранятся с помощью двоичного дерева, у элементов есть не более двух потомков - левый и правый
    Уровни заполняются в порядке увеличения номера уровня, а сам уровень заполняется слева направо.
    У элементов последнего уровня нет ни одного потомка, возможно, что и у некоторых элементов предпоследнего уровня
    нет потомков. Также в куче может быть один элемент, у которого только один потомок (левый).
    Индексы потомков i-го элемента - 2*i+1 и 2*i+2
    Индекс родителя элемента (i-1) // 2
    Для элементов кучи верно следующее свойство - каждый из элементов кучи меньше (или равен) всех своих потомков.
    В частности это означает, что в вершине кучи хранится наименьший элемент.
    """

    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.sift_up(self.size - 1)

    def extract_min(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_up(self, idx):
        while idx != 0 and self.values[idx] < self.values[(idx - 1) // 2]:
            self.values[idx], self.values[(idx - 1) // 2] = self.values[(idx - 1) // 2], self.values[idx]
            idx = (idx - 1) // 2

    def sift_down(self, idx):
        while 2 * idx + 1 < self.size:
            j = idx
            if self.values[2 * idx + 1] < self.values[idx]:
                j = 2 * idx + 1
            if 2 * idx + 2 < self.size and self.values[2 * idx + 2] < self.values[j]:
                j = 2 * idx + 2
            if idx == j:
                break
            self.values[idx], self.values[j] = self.values[j], self.values[idx]
            idx = j


def heapify(arr: list):
    """
    Функция, создающая кучу на основе списка
    return heap: Heap
    скорость работы O(n*log(n))
    """
    heap = Heap()
    for x in arr:
        heap.insert(x)
    return heap


def heapify_fast(arr: list):
    """
    Функция, создающая кучу на основе списка
    Работает корректно только если одновременно не вытаскиваются элементы из кучи, а дан готовый список данных
    return heap: Heap
    Скорость работы O(n)
    """
    heap = Heap()
    heap.values = arr[:]
    heap.size = len(arr)
    for i in reversed(range(heap.size // 2)):
        heap.sift_down(i)
    return heap


def heap_sort(arr: list):
    """
    Функция сортировки списка с помощью кучи
    Скорость работы O(n*log(n))
    """
    res = []
    h = heapify_fast(arr)
    while h.size:
        res.append(h.extract_min())
    return res


numbers = [15, 46, 2, 13, 11, 14, 15, 87, 0, 40, 19]
print(heap_sort(numbers))

