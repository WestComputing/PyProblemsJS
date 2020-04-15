import unittest


def reverse_characters(characters, first_index, last_index):
    while first_index < last_index:
        characters[first_index], characters[last_index] \
            = characters[last_index], characters[first_index]
        first_index += 1
        last_index -= 1


def reverse_words(message):
    reverse_characters(message, 0, len(message) - 1)
    word_index = 0
    for i in range(len(message) + 1):
        if i == len(message) or message[i] == ' ':
            reverse_characters(message, word_index, i - 1)
            word_index = i + 1


# def reverse_words(message):
#     temp = ' '.join(list(reversed(''.join(message).split(' '))))
#     for i, char in enumerate(temp):
#         message[i] = char


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
