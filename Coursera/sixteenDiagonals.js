const BLANK = "•";
const SLASH = "/";
const BACKSLASH = "\\";

const FIND_FIRST_SOLUTION = false;
const SOLUTIONS = [];


const copyPermutation = original => {
    const copy = [];
    original.forEach(element => copy.push(element.slice()));
    return copy;
};


const renderBoard = permutation => {
    console.log(permutation.reduce((board, row) => board + row.join("") + "\n", ""));
};


const isViable = (permutation, size) => {
    const row = permutation.length - 1;
    if (row > -1) {
        const col = permutation[row].length - 1;
        if (col > -1) {
            if (permutation[row][col] === SLASH) {
                if (col) {
                    if (permutation[row][col - 1] === BACKSLASH) return false;
                }
                if (row) {
                    if (permutation[row - 1][col] === BACKSLASH) return false;
                    if (permutation[row - 1][col + 1] === SLASH) return false;
                }
            }
            if (permutation[row][col] === BACKSLASH) {
                if (col) {
                    if (permutation[row][col - 1] === SLASH) return false;
                    if (row) {
                        if (permutation[row - 1][col - 1] === BACKSLASH) return false;
                    }
                }
                if (row) {
                    if (permutation[row - 1][col] === SLASH) return false;
                }
            }
        }
    }
    return true;
};

const solve = (permutation, size, diagonals) => {
    if (isViable(permutation, size)) {
        if ((permutation.length === size) && (permutation[permutation.length - 1].length === size)) {
            let placedDiagonals = 0;
            permutation.forEach(row => {
                placedDiagonals += size - row.filter(col => col === BLANK).length;
            });
            if (placedDiagonals === diagonals) {
                if (FIND_FIRST_SOLUTION) {
                    renderBoard(permutation);
                    console.timeEnd("runtime");
                    process.exit(0);
                } else {
                    SOLUTIONS.push(copyPermutation(permutation));
                }
            }
        } else {
            generatePermutations(permutation, size, diagonals);
        }
    }
};


const generatePermutations = (permutation, size, diagonals) => {
    if (permutation[permutation.length - 1].length === size) {
        permutation.push([]);
    }
    [SLASH, BACKSLASH, BLANK].forEach(symbol => {
        const newPermutation = copyPermutation(permutation);
        newPermutation[newPermutation.length - 1].push(symbol);
        solve(newPermutation, size, diagonals);
    });
};

console.time("runtime");
// solve([[]], 3, 6);  // 7.5ms
// solve([[]], 4, 10);  // 111ms
solve([[]], 5, 16);  // 426ms first solution; 36s both solutions
console.timeEnd("runtime");
SOLUTIONS.forEach(solution => renderBoard(solution));
console.log(SOLUTIONS.length, "solutions");
