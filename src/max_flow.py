from collections import defaultdict


def max_flow(input_file):
    maximum_flow = 0
    try:
        farms, stores, lines = read_data_from_file(input_file)
        lines = [[line[0], line[1], int(line[2])] for line in lines]
        if not lines or len(farms) == 0 or len(stores) == 0:
            return
    except Exception:
        return

    for farm in farms:
        lines.append(["F", farm, float('inf')])
    for store in stores:
        lines.append([store, "S", float('inf')])

    graph = defaultdict(dict[int])

    for line in lines:
        start_city, end_city, weight = line

        graph[start_city][end_city] = weight
    graph = dict(graph)

    while True:
        path = dfs(graph)
        if not path:
            break
        maximum_flow += decrease_weight_on_path(graph, path)

    return maximum_flow


def decrease_weight_on_path(graph, path):
    min_weight = float('inf')
    for i in range(len(path) - 1):
        start_city = path[i]
        end_city = path[i + 1]
        min_weight = min(graph[start_city][end_city], min_weight)

    for i in range(len(path) - 1):
        start_city = path[i]
        end_city = path[i + 1]
        if graph[start_city][end_city] == min_weight:
            del graph[start_city][end_city]
        else:
            graph[start_city][end_city] -= min_weight

    return min_weight


def dfs(graph):
    if not graph:
        return None
    queue = ['F']
    previous_vertex = {
        'F': None,
    }
    visited = set()

    while queue:
        vertex = queue.pop()
        if vertex in visited:
            continue

        if vertex == 'S':
            return get_path(previous_vertex, vertex, 'F')

        visited.add(vertex)
        for neighbour in graph[vertex]:
            queue.append(neighbour)
            previous_vertex[neighbour] = vertex

    return None


def get_path(from_dict, last_vertex, start_vertex):
    path = []
    while last_vertex != start_vertex:
        path.append(last_vertex)
        last_vertex = from_dict[last_vertex]
    path.append(start_vertex)
    return path[::-1]


def read_data_from_file(file_name):
    with open(f"../resources/{file_name}", "r") as file:
        lines = file.readlines()
        start_vertexes = lines[0].strip().split()
        destination_vertexes = lines[1].strip().split()
        edges = [line.strip().split() for line in lines[2:]]
    return start_vertexes, destination_vertexes, edges
