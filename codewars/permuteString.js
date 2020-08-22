function permutations(string) {
    if (string.length < 2) {
        return [string];
    }
    const result = [];
    for (let i = 0; i < string.length; i++) {
        const newFirstChar = string[i];
        const remainingChars = string.slice(0, i) + string.slice(i + 1);
        if (string.indexOf(newFirstChar) === i) {
            for (const permutation of permutations(remainingChars)) {
                result.push(newFirstChar + permutation);
            }
        }
    }
    return result.sort();
}

console.log(permutations('aabb'));