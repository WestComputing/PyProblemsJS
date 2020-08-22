import unittest
from heapq import merge


def merge_lists(*args):
    return list(merge(*args))

# O(n)
# def merge_lists(my_list, alices_list):
#     # Combine the sorted lists into one large sorted list
#     merged_list = [None] * (len(my_list) + len(alices_list))
#     my_index, alices_index, merged_index = 0, 0, 0
#     while my_index < len(my_list) and alices_index < len(alices_list):
#         if my_list[my_index] > alices_list[alices_index]:
#             merged_list[merged_index] = alices_list[alices_index]
#             alices_index += 1
#         else:
#             merged_list[merged_index] = my_list[my_index]
#             my_index += 1
#         merged_index += 1
#     if my_index < len(my_list):
#         merged_list[merged_index:] = my_list[my_index:]
#     elif alices_index < len(alices_list):
#         merged_list[merged_index:] = alices_list[alices_index:]
#     return merged_list



# O(n lg n)
# def merge_lists(my_list, alices_list):
#     my_list.solve(alices_list)
#     my_list.sort()
#     return my_list
#     return sorted(my_list + alices_list)


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
