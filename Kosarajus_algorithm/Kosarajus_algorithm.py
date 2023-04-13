# Алгоритм Касарайю
# 1. Инвертируем дуги исходного ориентированного графа.
# 2. Запускаем поиск в глубину на этом обращённом графе,
# запоминая, в каком порядке выходили из вершин.
# 3. Запускаем поиск в глубину на исходном графе, в очередной
# раз выбирая непосещённую вершину с максимальным номером
# в векторе, полученном в п.2.
# 4. Полученные из п.3 деревья и являются сильно связными компонентами.

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices  # Число вершин в графе
        self.graph = defaultdict(list)  # Словарь для хранения графа

    # Метод для добавления ребра в граф
    def add_edge(self, n, v):
        self.graph[n].append(v)

    # Метод для прохода графа в глубину
    def dfs(self, v, visited):
        visited[v] = True
        # print(v)
        for vertex in self.graph[v]:
            if visited[vertex] is False:
                self.dfs(vertex, visited)

    # Метод для прохода по графу и наполнение стека
    def fill_stack(self, v, visited, stack):
        visited[v] = True
        for vertex in self.graph[v]:
            if visited[vertex] is False:
                self.fill_stack(vertex, visited, stack)
        stack.append(v)

    # Метод для смены направления в ориентированном графе
    def get_reverse_graph(self):
        gr = Graph(self.vertices)
        # для каждой вершины графа
        for vertex in self.graph:
            # для каждой смежной вершины
            for neighbour in self.graph[vertex]:
                gr.add_edge(neighbour, vertex)
        return gr

    # Метод для нахождения сильно связанных компонент
    def get_scc(self):
        stack = []
        # По умолчанию все вершины не посещённые
        visited = [False] * self.vertices
        # Кладём вершину в стэк, если вершина не посещена
        for vertex in range(self.vertices):
            if visited[vertex] is False:
                self.fill_stack(vertex, visited, stack)
        # Меняем направление в графе
        rg = self.get_reverse_graph()
        # Снова маркеруем все вершины как непосещённые
        visited = [False] * self.vertices

        # Достаём вершины из стека
        component = []
        while stack:
            vertex = stack.pop()
            if visited[vertex] is False:
                rg.dfs(vertex, visited)
                component.append(vertex)
        print(f'Strongly connected components in the graph:\n{component}')


if __name__ == "__main__":
    # Example 1
    g = Graph(7)
    g.add_edge(3, 0)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 5)
    g.add_edge(5, 4)
    g.get_scc()

    # Example 2
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.get_scc()

    # Example 3
    g = Graph(8)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 4)
    g.get_scc()
