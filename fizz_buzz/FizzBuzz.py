class FizzBuzz:
    def __init__(self, start=1, stop=101):
        self.__i = start - 1
        self.__stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i == self.__stop: raise StopIteration
        s = ('' if self.__i % 3 else 'Fizz')
        s += ('' if self.__i % 5 else 'Buzz')
        return s if s else self.__i


for i in FizzBuzz(stop=16):
    print(i)

print([i for i in FizzBuzz(stop=16)])
