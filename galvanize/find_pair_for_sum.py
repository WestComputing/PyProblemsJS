from typing import Optional, List, Tuple


def find_pair_for_sum(integers: List[int], target: int) -> Optional[Tuple[int, int]]:
    """
    :param: List[int], int
    :rtype: Tuple[int, int] or None
    """
    # prune zero, negative numbers, numbers > target
    numbers = list(filter(lambda num: 0 < num < target, integers))

    for i, num1 in enumerate(numbers[:-1]):
        for num2 in numbers[i:]:
            if num1 + num2 == target:
                return num1, num2
    return None


pair = find_pair_for_sum([3, 34, 4, 12, 5, 2], 9)
print(f"{pair} {'pass' if pair == (4, 5) else 'fail'}")
