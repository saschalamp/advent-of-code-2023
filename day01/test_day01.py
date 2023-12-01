import unittest

from day01 import solve


class Day01Test(unittest.TestCase):
    def test_solve_empty(self):
        lines = []
        actual = solve(lines, False)
        self.assertEqual(actual, 0)

    def test_solve_single_line_trivial(self):
        lines = ['1']
        actual = solve(lines, False)
        self.assertEqual(actual, 11)

    def test_solve_single_line_trivial_different_number(self):
        lines = ['4']
        actual = solve(lines, False)
        self.assertEqual(actual, 44)

    def test_solve_single_line_2_numbers(self):
        lines = ['34']
        actual = solve(lines, False)
        self.assertEqual(actual, 34)

    def test_solve_single_line_2_numbers_at_both_ends(self):
        lines = ['3abc4']
        actual = solve(lines, False)
        self.assertEqual(actual, 34)

    def test_solve_single_line_2_numbers_left_in_the_middle(self):
        lines = ['gfd9abc2']
        actual = solve(lines, False)
        self.assertEqual(actual, 92)

    def test_solve_single_line_2_numbers_right_in_the_middle(self):
        lines = ['9gfd4abc']
        actual = solve(lines, False)
        self.assertEqual(actual, 94)

    def test_solve_multiple_lines(self):
        lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        actual = solve(lines, False)
        self.assertEqual(actual, 142)

    def test_solve_single_line_word_and_number(self):
        lines = ['one2']
        actual = solve(lines, False)
        self.assertEqual(actual, 22)

    def test_solve_single_line_number_and_word(self):
        lines = ['2one']
        actual = solve(lines, False)
        self.assertEqual(actual, 22)

    def test_solve_part2_first_example(self):
        lines = ['two1nine']
        actual = solve(lines, False)
        self.assertEqual(actual, 11)

    def test_solve_multiple_lines_part2(self):
        lines = [
            'two1nine',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
        actual = solve(lines, False)
        self.assertEqual(actual, 209)


class Day01Test_part2(unittest.TestCase):
    def test_solve_empty(self):
        lines = []
        actual = solve(lines, True)
        self.assertEqual(actual, 0)

    def test_solve_single_line_trivial(self):
        lines = ['1']
        actual = solve(lines, True)
        self.assertEqual(actual, 11)

    def test_solve_single_line_trivial_different_number(self):
        lines = ['4']
        actual = solve(lines, True)
        self.assertEqual(actual, 44)

    def test_solve_single_line_2_numbers(self):
        lines = ['34']
        actual = solve(lines, True)
        self.assertEqual(actual, 34)

    def test_solve_single_line_2_numbers_at_both_ends(self):
        lines = ['3abc4']
        actual = solve(lines, True)
        self.assertEqual(actual, 34)

    def test_solve_single_line_2_numbers_left_in_the_middle(self):
        lines = ['gfd9abc2']
        actual = solve(lines, True)
        self.assertEqual(actual, 92)

    def test_solve_single_line_2_numbers_right_in_the_middle(self):
        lines = ['9gfd4abc']
        actual = solve(lines, True)
        self.assertEqual(actual, 94)

    def test_solve_multiple_lines(self):
        lines = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']
        actual = solve(lines, True)
        self.assertEqual(actual, 142)

    def test_solve_single_line_word_and_number(self):
        lines = ['one2']
        actual = solve(lines, True)
        self.assertEqual(actual, 12)

    def test_solve_single_line_number_and_word(self):
        lines = ['2one']
        actual = solve(lines, True)
        self.assertEqual(actual, 21)

    def test_solve_single_line_single_word_3_letters(self):
        lines = ['one']
        actual = solve(lines, True)
        self.assertEqual(actual, 11)

    def test_solve_single_line_two_words_4_letters(self):
        lines = ['fourfive']
        actual = solve(lines, True)
        self.assertEqual(actual, 45)

    def test_solve_single_line_two_words_5_letters(self):
        lines = ['eightseven']
        actual = solve(lines, True)
        self.assertEqual(actual, 87)

    def test_solve_single_line_2_morphed_words(self):
        lines = ['oneight']
        actual = solve(lines, True)
        self.assertEqual(actual, 18)

    def test_solve_part2_first_example(self):
        lines = ['two1nine']
        actual = solve(lines, True)
        self.assertEqual(actual, 29)

    def test_solve_multiple_lines_part2(self):
        lines = [
            'two1nine',
            'eightwothree',
            'abcone2threexyz',
            'xtwone3four',
            '4nineeightseven2',
            'zoneight234',
            '7pqrstsixteen',
        ]
        actual = solve(lines, True)
        self.assertEqual(actual, 281)

if __name__ == '__main__':
    unittest.main()
