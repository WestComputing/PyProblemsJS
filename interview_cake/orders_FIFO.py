def check_fifo(q1, q2, out):
    q1index = q2index = 0
    for order in out:
        if q1index < len(q1) and q1[q1index] == order:
            q1index += 1
            continue
        if q2index < len(q2) and q2[q2index] == order:
            q2index += 1
            continue
        return False
    return q1index == len(q1) and q2index == len(q2)


# fail:
print(check_fifo([1, 3, 5], [2, 4, 6],[1, 2, 4, 6, 5, 3]))
print(check_fifo([17, 8, 24], [12, 19, 2], [17, 12, 19, 24, 2]))
print(check_fifo([17, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]))
# pass
print(check_fifo([17, 8, 24], [12, 19, 2], [17, 8, 12, 19, 24, 2]))
