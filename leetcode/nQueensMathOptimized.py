import time


def render_board(permutation):
    space = '• '
    queen = '♕ '
    size = len(permutation)
    board = ''
    for column in permutation:
        board += space * column + queen + space * (size - column - 1) + "\n"
    return board


def is_viable_to_solve(permutation):
    i = len(permutation) - 1
    for j in range(i):
        if i - j == abs(permutation[i] - permutation[j]):
            return False
    return True


def solve(permutation, n):
    if len(permutation) == n:
        global solutions
        solutions.append(permutation[:])
        # print(f"Solution #{len(solutions)}: {permutation}")
        return

    for k in range(n):
        if k not in permutation:
            permutation.append(k)
            if is_viable_to_solve(permutation):
                solve(permutation, n)
            permutation.pop()


solutions = []
start = time.perf_counter()
# solve([], 4)  # 0s
# solve([], 8)  # 0.007s
# solve([], 12)  # 4.4s
# solve([], 13)  # 26.6s
# solve([], 14)  # 365,596 solutions in 174 seconds
# solve([], 15)  #
solve([], 16)  #

stop = time.perf_counter()
for solution in solutions:
    print(render_board(solution))
print(f"{len(solutions)} solutions in {stop - start:0.3f} seconds")
