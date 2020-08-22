const RomanNumerals = {
    toRoman: function (number) {
        if (number < 1 || number > 3999) return 'NVLLA'

        const [VALUE, DIGIT] = [0, 1];
        const TABLE = [
            [1000, 'M'],
            [900, 'CM'],
            [500, 'D'],
            [400, 'CD'],
            [100, 'C'],
            [90, 'XC'],
            [50, 'L'],
            [40, 'XL'],
            [10, 'X'],
            [9, 'IX'],
            [5, 'V'],
            [4, 'IV'],
            [1, 'I']
        ];
        let result = '';
        do {
            let lookup = TABLE.findIndex(e => number - e[VALUE] >= 0);
            result += TABLE[lookup][DIGIT];
            number -= TABLE[lookup][VALUE];
        } while (number);
        return result;
    },
    fromRoman: function (numerals) {
        const table = {I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000}
        return numerals.split('').reduce((r, e, i, a) => r += table[a[i + 1]] > table[e] ? -table[e] : table[e], 0);
    }
}
