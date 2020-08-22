class RomanNumerals:
    @staticmethod
    def to_roman(number: int) -> str:
        TABLE = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        def arabic(number: int) -> int:
            for key in TABLE.keys():
                if number - key >= 0:
                    return key

        roman_number = ''
        while number:
            value = arabic(number)
            number -= value
            roman_number += TABLE[value]
        return roman_number

    @staticmethod
    def from_roman(numerals: str) -> int:
        TABLE = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for index, numeral in enumerate(numerals[:-1]):
            arabic = TABLE[numeral]
            if TABLE[numerals[index + 1]] > arabic:
                result -= arabic
            else:
                result += arabic
        return result + TABLE[numerals[-1]]


print(RomanNumerals.to_roman(1000), 'M', '1000 should == "M"')
print(RomanNumerals.to_roman(1990), 'MCMXC', '1990 should == "MCMXC"')

print(RomanNumerals.from_roman('XXI'), 21, 'XXI should == 21')
print(RomanNumerals.from_roman('MMVIII'), 2008, 'MMVIII should == 2008')
