import unittest

from day04 import Card, solve_part1, build_cards

class Day04Part1(unittest.TestCase):

    def test_trivial(self):
        cards = []
        result = solve_part1(cards)
        self.assertEqual(result, 0)

    def test_one_winning_number(self):
        cards = [
            Card([2], [2])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 1)

    def test_one_winning_number_different_number(self):
        cards = [
            Card([2], [4])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 0)

    def test_multiple_your_numbers_with_one_singular_winning_number(self):
        cards = [
            Card([2], [3, 4, 1, 2])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 1)

    def test_multiple_your_numbers_with_one_in_list_of_winning_numbers(self):
        cards = [
            Card([1, 2, 6, 8], [3, 4, 5, 2])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 1)

    def test_multiple_your_numbers_with_multiple_in_list_of_winning_numbers(self):
        cards = [
            Card([1, 2, 6, 8], [3, 4, 5, 2, 1, 8])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 4)

    def test_example(self):
        cards = [
            Card([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),
            Card([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]),
            Card([1, 21, 53, 59, 44], [69, 82, 63, 72, 16, 21, 14, 1]),
            Card([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),
            Card([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]),
            Card([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11])
        ]
        result = solve_part1(cards)
        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()
