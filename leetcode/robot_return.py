def judge_circle(moves: str) -> bool:
    # return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
    x = y = 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1
    return x == y == 0


print(judge_circle('UDLR'))
