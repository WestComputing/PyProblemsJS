
function getPermutations(a) {
    const permutations = [];
    function heaps(a, n = a.length) {
        if (n === 1) {
            permutations.push(a.slice());
            return;
        }
        for (let i = 0; i < (n-1); i++) {
            heaps(a, n - 1);
            if (n % 2) [a[0], a[n - 1]] = [a[n - 1], a[0]]
            else [a[i], a[n - 1]] = [a[n - 1], a[i]];
        }
        heaps(a, n - 1);
    }
    heaps(a);
    return permutations;
}

const test = [1,2,3,4];
permutations = getPermutations(test);
console.log(permutations);
