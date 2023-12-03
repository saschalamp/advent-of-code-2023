import unittest

from day03 import solve_part1, solve_part2


class Day03Part1Test(unittest.TestCase):
    def test_trivial(self):
        schematic = []
        actual = solve_part1(schematic)
        self.assertEqual(actual, 0)

    def test_single_number_with_symbol_right(self):
        schematic = [
            ['1', '$']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_single_number_with_period_right(self):
        schematic = [
            ['1', '.']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 0)

    def test_single_number_with_symbol_left(self):
        schematic = [
            ['#', '4']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 4)

    def test_single_number_with_symbol_left_and_number_right(self):
        schematic = [
            ['$', '5', '4']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 54)

    def test_multiple_numbers_with_singular_symbol_in_between(self):
        schematic = [
            ['1', '2', '$', '3', '4', '5']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 357)

    def test_multiple_singular_number_with_symbol_in_second_row(self):
        schematic = [
            ['.', '.'],
            ['1', '$']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_multiple_singular_number_with_symbol_above(self):
        schematic = [
            ['$'],
            ['1']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_multiple_two_digit_number_with_symbol_above_second(self):
        schematic = [
            ['.', '$'],
            ['1', '2']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 12)

    def test_multiple_three_digit_number_with_symbol_above_the_middle(self):
        schematic = [
            ['.', '$', '.'],
            ['1', '2', '3']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 123)

    def test_multiple_three_digit_number_with_symbol_diag_above_left(self):
        schematic = [
            ['#', '.'],
            ['.', '1']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_multiple_three_digit_number_with_symbol_diag_above_right(self):
        schematic = [
            ['.', '%'],
            ['1', '.']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_multiple_three_digit_number_with_symbol_diag_below_right(self):
        schematic = [
            ['1', '.'],
            ['.', '%']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 1)

    def test_numbers_in_multiple_rows(self):
        schematic = [
            ['1', '.', '.'],
            ['.', '%', '.'],
            ['.', '4', '2']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 43)

    def test_example(self):
        schematic = [
            ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
            ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
            ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
            ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
            ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
        ]
        actual = solve_part1(schematic)
        self.assertEqual(actual, 4361)


class Day03Part2Test(unittest.TestCase):
    def test_trivial(self):
        schematic = []
        actual = solve_part2(schematic)
        self.assertEqual(actual, 0)

    def test_singular_gear_in_single_row(self):
        schematic = [
            ['4', '*', '2']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 8)

    def test_singular_gear_in_single_row_larger_number_left(self):
        schematic = [
            ['4', '1', '*', '2']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 82)

    def test_singular_gear_in_single_row_larger_number_right(self):
        schematic = [
            ['4', '*', '1', '2']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 48)

    def test_single_line_not_a_gear(self):
        schematic = [
            ['4', '.', '1', '2']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 0)
    

    def test_singular_gear_in_column(self):
        schematic = [
            ['4'],
            ['*'],
            ['5']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 20)
    

    def test_singular_gear_in_column_top_to_the_right(self):
        schematic = [
            ['4', '5'],
            ['*', '.'],
            ['2', '.']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 90)
    

    def test_singular_gear_in_column_bottom_to_the_left(self):
        schematic = [
            ['.', '4'],
            ['.', '*'],
            ['1', '2']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 48)
    

    def test_singular_gear_in_column_above_only(self):
        schematic = [
            ['2', '.', '4'],
            ['.', '*', '.']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 8)
    

    def test_singular_gear_in_column_too_many(self):
        schematic = [
            ['2', '*', '.'],
            ['2', '.', '4']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 0)
    

    def test_singular_gear_multiple_gears(self):
        schematic = [
            ['2', '*', '.', '8', '*', '4'],
            ['.', '.', '4', '.', '.', '.']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 40)
    

    def test_example(self):
        schematic = [
            ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.'],
            ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.'],
            ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
            ['6', '1', '7', '*', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '+', '.', '5', '8', '.'],
            ['.', '.', '5', '9', '2', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '7', '5', '5', '.'],
            ['.', '.', '.', '$', '.', '*', '.', '.', '.', '.'],
            ['.', '6', '6', '4', '.', '5', '9', '8', '.', '.']
        ]
        actual = solve_part2(schematic)
        self.assertEqual(actual, 467835)


if __name__ == '__main__':
    unittest.main()
