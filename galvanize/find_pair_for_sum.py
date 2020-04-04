""" var pair = findPairForSum([3, 34, 4, 12, 5, 2], 9);
console.log(pair); // --> [4, 5]
*/

function findPairForSum(integers, target) {
// your solution here
}"""


def find_pair_for_sum(integers, target):
    # prune zero, negative numbers, numbers > target
    for i in integers[:]:
        if i < 0 or i > target:
            integers.remove(i)

    length = len(integers) - 1
    for i in range(length - 1):
        for j in range(length, i, -1):
            result = (integers[i], integers[j])
            if sum(result) == target: return list(result)
    return None


pair = find_pair_for_sum([3, 34, 4, 12, 5, 2], 9)
print(pair)
