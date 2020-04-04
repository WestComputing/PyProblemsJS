def visit_island(row, col):
    if not(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[row]) or grid[row][col] != 1):
        grid[row][col] = 2
        visit_island(row - 1, col)
        visit_island(row, col - 1)
        visit_island(row + 1, col)
        visit_island(row, col + 1)


def count_islands():
    island_count = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                island_count += 1
                visit_island(row, col)
    return island_count


maps = [
    [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1]
    ]
]

for grid in maps:
    print(count_islands())
