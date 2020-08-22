def iq_test(numbers):
    numbers_array = list(map(lambda n: int(n), numbers.split(' ')))
    is_odd_array = bool(len(list(filter(lambda n: n % 2, numbers_array))) > 1)
    return next(i for i, n in enumerate(numbers_array) if bool(n % 2) != is_odd_array) + 1


print(iq_test("2 4 7 8 10"), 3)
print(iq_test("1 2 2"), 1)
