def fizz_buzz(start=1, stop=101):
    for i in range(start, stop):
        s = '' if i % 3 else 'Fizz'
        s += '' if i % 5 else 'Buzz'
        yield s if s else i


print([i for i in fizz_buzz()])
