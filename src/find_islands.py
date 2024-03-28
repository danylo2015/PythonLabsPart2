from typing import List


def count_islands(graph: List[List[str]]) -> int:
    if not graph:
        return 0

    visited_coordinates = {}
    count = 0
    row = len(graph)
    col = len(graph[0])

    for i in range(row):
        for j in range(col):
            if graph[i][j] == '1' and (i, j) not in visited_coordinates:
                bfs(graph, i, j, row, col, visited_coordinates)
                count += 1

    return count


def bfs(graph, i, j, row, col, visited):
    queue = [(i, j)]

    while queue:
        next_queue = []

        for coord in queue:
            if tuple(coord) not in visited:
                visited[tuple(coord)] = 1

                # right
                if coord[1] + 1 < col and graph[coord[0]][coord[1] + 1] == '1':
                    next_queue.append((coord[0], coord[1] + 1))

                # left
                if coord[1] - 1 >= 0 and graph[coord[0]][coord[1] - 1] == '1':
                    next_queue.append((coord[0], coord[1] - 1))

                # up
                if coord[0] - 1 >= 0 and graph[coord[0] - 1][coord[1]] == '1':
                    next_queue.append((coord[0] - 1, coord[1]))

                # down
                if coord[0] + 1 < row and graph[coord[0] + 1][coord[1]] == '1':
                    next_queue.append((coord[0] + 1, coord[1]))

                # up-right
                if coord[0] - 1 >= 0 and coord[1] + 1 < col and graph[coord[0] - 1][coord[1] + 1] == '1':
                    next_queue.append((coord[0] - 1, coord[1] + 1))

                # up-left
                if coord[0] - 1 >= 0 and coord[1] - 1 >= 0 and graph[coord[0] - 1][coord[1] - 1] == '1':
                    next_queue.append((coord[0] - 1, coord[1] - 1))

                # down-right
                if coord[0] + 1 < row and coord[1] + 1 < col and graph[coord[0] + 1][coord[1] + 1] == '1':
                    next_queue.append((coord[0] + 1, coord[1] + 1))

                # down-left
                if coord[0] + 1 < row and coord[1] - 1 >= 0 and graph[coord[0] + 1][coord[1] - 1] == '1':
                    next_queue.append((coord[0] + 1, coord[1] - 1))
        queue = next_queue
