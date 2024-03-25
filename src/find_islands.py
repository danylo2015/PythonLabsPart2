def count_islands(grid):
    if not grid:
        return 0

    count = 0
    num_rows = len(grid)
    num_cols = len(grid[0])

    for row in range(0, num_rows):
        for col in range(0, num_cols):
            if grid[row][col] == "1":
                count += 1
                bfs(row, col, grid)

    return count


def bfs(row, col, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = [(row, col)]

    while queue:
        cur_row, cur_col = queue.pop(0)

        for dr, dc in directions:
            new_row, new_col = cur_row + dr, cur_col + dc

            if is_valid(new_row, new_col, grid):
                queue.append((new_row, new_col))
                grid[new_row][new_col] = "0"


def is_valid(row, col, grid):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
        return False

    return True
