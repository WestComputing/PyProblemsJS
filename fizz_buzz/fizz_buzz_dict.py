def fizz_buzz(start=1, stop=101, trigger_values={3: 'Fizz', 5: 'Buzz'}):  # Mutable is OK here
    for i in range(start, stop):
        result = ''
        for k, v in trigger_values.items():
            result += '' if i % k else v
        yield result if result else i


print([i for i in fizz_buzz(stop=16)])
print([i for i in fizz_buzz(trigger_values={3: 'Fizz', 5: 'Buzz', 10: 'Bang'})])
