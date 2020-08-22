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


const countDiagonals = permutation => {
    let numberDiagonals = 0;
    permutation.forEach(row => {
        row.forEach(square => {
            if (square !== BLANK) {
                numberDiagonals++;
            }
        });
    });
    return numberDiagonals;
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


const solve = (permutation, size, diagonals) => {
    if (isViable(permutation, size)) {
        if ((permutation.length === size) && (permutation[permutation.length - 1].length === size)) {
            const placedDiagonals = countDiagonals(permutation);
            // const placedDiagonals = permutation.flat().filter(square => square !== BLANK).length; // 7x slower
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


console.time("runtime");
// solve([[]], 3, 6);  // 6.7ms 28 solutions
// solve([[]], 4, 10);  // 82ms 108 solutions
solve([[]], 5, 16);  // 354ms first solution; 29.5s both solutions
console.timeEnd("runtime");
SOLUTIONS.forEach(solution => renderBoard(solution));
console.log(SOLUTIONS.length, "solutions");
