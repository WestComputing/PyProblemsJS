function getPermutations(permutee) {
    if (typeof permutee === 'string') {
        permutee = permutee.split('');
    } else {
        permutee = permutee.slice();
    }
    const permutations = new Set();
    permutations.add(permutee.join(''));
    const call = Array(permutee.length).fill(0);
    let i = 0;
    while (i < permutee.length) {
        if (call[i] < i) {
            if (i % 2) {
                [permutee[call[i]], permutee[i]] = [permutee[i], permutee[call[i]]];
            } else {
                [permutee[0], permutee[i]] = [permutee[i], permutee[0]];
            }
            permutations.add(permutee.join(''));
            call[i]++;
            i = 0;
        } else {
            call[i] = 0;
            i++;
        }
    }
    return Array.from(permutations);
}

const testData = ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'];
console.log(testData);
console.log(getPermutations('aabb').sort());
