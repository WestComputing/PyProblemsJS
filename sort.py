import random

m = int(input("How many numbers? ")) + 1
reference_numbers = []

for n in range(1, m):
    reference_numbers.append(n)
random.shuffle(reference_numbers)

numbers = reference_numbers[:]
print(numbers, end=3 * "\n")
length = len(numbers)
width = len(str(m))
for i in range(length // 2):
    j = length - i - 1
    print("%*d <->" % (width, numbers[i]), end=" ")
    numbers[i], numbers[j] = numbers[j], numbers[i]
    print("%*d" % (width, numbers[i]))

print(2 * "\n", numbers, sep="")

checks = swaps = 0
swapped = True
while swapped:
    swapped = False
    for i in range(length - 1):
        j = i + 1
        checks += 1
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swapped = True
            swaps += 1
print("\nWhile:\nChecks: ", checks, "\nSwaps: ", swaps, sep="")

numbers = reference_numbers[:]
checks = swaps = 0
for i in range(length - 1):
    for j in range(i + 1, length):
        checks += 1
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            swaps += 1
print("\nNested For:\nChecks: ", checks, "\nSwaps: ", swaps, sep="")
