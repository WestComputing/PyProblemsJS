/**
 * @param {number} n
 * @return {number}
 */
const totalNQueens = n => {

    const QUEEN = "Q";
    const BLANK = " ";
    const ATTACKED = "•";
    let numberSolutions = 0;

    const copyBoard = board => board.slice().map(row => row.slice());

    const processRow = (board, row = 0) => {

        if (row === n) {
            numberSolutions++;
            return;
        }

        const placeQueen = (board, row, col) => {

            board[row][col] = QUEEN;

            for (let c = 0; c < board[row].length; c++) {
                if (c === col) continue;
                board[row][c] = ATTACKED;
            }
            let negDiag, posDiag, offset;
            for (let r = row + 1; r < board.length; r++) {
                board[r][col] = ATTACKED;
                offset = r - row;
                negDiag = col - offset;
                posDiag = col + offset;
                if (negDiag >= 0) {
                    board[r][negDiag] = ATTACKED;
                }
                if (posDiag < board[r].length) {
                    board[r][posDiag] = ATTACKED;
                }
            }
        }

        let col = 0;
        let nextSpace;
        while ((nextSpace = board[row].indexOf(BLANK, col)) > -1) {
            const thisBoard = copyBoard(board);
            placeQueen(thisBoard, row, nextSpace);
            processRow(thisBoard, row + 1);
            col = nextSpace + 1;
        }

    }

    const blankBoard = [...Array(n)].map(() => Array(n).fill(BLANK));
    processRow(blankBoard);
    return numberSolutions;

};

console.time('Runtime')
// console.log(totalNQueens(8), "solutions"); // 10ms
// totalNQueens(12); // 12 => 350ms
// totalNQueens(13); // 13 => 1877ms
// totalNQueens(14); // 14 => 11.6s
// totalNQueens(15); // 15 => 75.8s
console.log(totalNQueens(16), "solutions"); // 14,772,512 solutions  565s
console.timeEnd('Runtime')