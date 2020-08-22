// const judgeCircle = moves => [...moves.matchAll(/(U)/g)].length === [...moves.matchAll(/(D)/g)].length && [...moves.matchAll(/(L)/g)].length === [...moves.matchAll(/(R)/g)].length;

const judgeCircle = moves => {
    let [x, y] = [0, 0]
    for (let move of moves) {
        if (move === 'U') y++;
        else if (move === 'D') y--;
        else if (move === 'L') x--;
        else if (move === 'R') x++;
    }
    return x === 0 && y === 0;
}


console.log(judgeCircle('UDLR'))