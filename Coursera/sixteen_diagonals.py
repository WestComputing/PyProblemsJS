import copy
import time

BLANK = '•'
SLASH = '/'
BACKSLASH = '\\'

FIND_FIRST_SOLUTION = False
SOLUTIONS = []


def render_board(permutation):
    board = ''
    for row in permutation:
        for col in row:
            board += col
        board += "\n"
    print(board)


def is_viable(permutation, size):
    row = len(permutation) - 1
    if row > -1:
        col = len(permutation[row]) - 1
        if col > -1:
            if permutation[row][col] == SLASH:
                if col:
                    if permutation[row][col - 1] == BACKSLASH:
                        return False
                if row:
                    if permutation[row - 1][col] == BACKSLASH:
                        return False
                    try:
                        if permutation[row - 1][col + 1] == SLASH:
                            return False
                    except IndexError:
                        pass
            if permutation[row][col] == BACKSLASH:
                if col:
                    if permutation[row][col - 1] == SLASH:
                        return False
                    if row:
                        if permutation[row - 1][col - 1] == BACKSLASH:
                            return False
                if row:
                    if permutation[row - 1][col] == SLASH:
                        return False
    return True


def solve(permutation, size, diagonals):
    if is_viable(permutation, size):
        if len(permutation) == size and len(permutation[-1]) == size:
            placed_diagonals = 0
            for row in permutation:
                placed_diagonals += size - row.count(BLANK)
            if placed_diagonals == diagonals:
                if FIND_FIRST_SOLUTION:
                    render_board(permutation)
                    global start
                    runtime = time.perf_counter() - start
                    print(f"{runtime:0.4f} seconds")
                    exit()
                else:
                    global SOLUTIONS
                    SOLUTIONS.append(copy.deepcopy(permutation))
        else:
            generate_permutations(permutation, size, diagonals)


def generate_permutations(permutation, size, diagonals):
    if len(permutation[-1]) == size:
        permutation.append([])
    for symbol in (SLASH, BACKSLASH, BLANK):
        new_permutation = copy.deepcopy(permutation)
        new_permutation[-1].append(symbol)
        solve(new_permutation, size, diagonals)


start = time.perf_counter()
# solve([[]], 3, 6)  # 350ms
# solve([[]], 4, 10)  # 6s
solve([[]], 5, 16)  # 30s first solution, 53m both solutions
runtime = time.perf_counter() - start
for solution in SOLUTIONS:
    render_board(solution)
print(len(SOLUTIONS), f"solutions in {runtime:0.3f} seconds")
