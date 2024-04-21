def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)


def check_gas_supply(cities, gas_storages, pipelines):
    graph = {city: [] for city in cities}

    for storage in gas_storages:
        graph[storage] = []

    for pipeline in pipelines:
        graph[pipeline[0]].append(pipeline[1])

    result = []

    for storage in gas_storages:
        visited = set()
        dfs(graph, storage, visited)
        unsupplied_cities = [city for city in cities if city not in visited]
        if unsupplied_cities:
            result.append([storage, unsupplied_cities])
    return result
