import itertools

SPACE = '• '
QUEEN = 'Q '


def render_board(permutation):
    size = len(permutation)
    board = ''
    for column in permutation:
        board += SPACE * column + QUEEN + SPACE * (size - column - 1) + "\n"
    return board


def is_solution(permutation):
    for (i1, i2) in itertools.combinations(permutation, 2):
        if abs(i1 - i2) == abs(permutation[i1] - permutation[i2]):
            return False
    return True


def find_solutions(size):
    solutions = []
    for permutation in itertools.permutations(range(size)):
        if is_solution(permutation):
            solutions.append(render_board(permutation))
    return solutions


solutions = find_solutions(8)
for solution in solutions:
    print(solution)
print(len(solutions), "solutions")
