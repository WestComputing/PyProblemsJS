function nextBigger(number) {
    function getPermutations(array) {
        const permutations = new Set();
        const call = Array(array.length).fill(0);
        let currentNumber;
        let i = 0;
        while (i < array.length) {
            if (call[i] < i) {
                if (i % 2) {
                    [array[call[i]], array[i]] = [array[i], array[call[i]]];
                } else {
                    [array[0], array[i]] = [array[i], array[0]];
                }
                currentNumber = Number(array.join(''));
                if (currentNumber > number) {
                    permutations.add(currentNumber);
                }
                call[i]++;
                i = 0;
            } else {
                call[i] = 0;
                i++;
            }
        }
        return Math.min(...permutations);
    }

    const digits = String(number).split('');
    const smallestPermutation = getPermutations(digits);
    if (smallestPermutation > number) {
        return smallestPermutation;
    } else {
        return -1;
    }
}


console.log(nextBigger(12), 21)
console.log(nextBigger(513), 531)
console.log(nextBigger(2017), 2071)
console.log(nextBigger(414), 441)
console.log(nextBigger(144), 414)