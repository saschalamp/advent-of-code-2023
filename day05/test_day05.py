import unittest

from day05 import *


example = AlmanacSolver1((
    AlmanacMap([
        CategoryConversion(98, 50, 2),
        CategoryConversion(50, 52, 48),
    ]),
    AlmanacMap([
        CategoryConversion(15, 0, 37),
        CategoryConversion(52, 37, 2),
        CategoryConversion(0, 39, 15),
    ]),
    AlmanacMap([
        CategoryConversion(53, 49, 8),
        CategoryConversion(11, 0, 42),
        CategoryConversion(0, 42, 7),
        CategoryConversion(7, 57, 4),
    ]),
    AlmanacMap([
        CategoryConversion(18, 88, 7),
        CategoryConversion(25, 18, 70),
    ]),
    AlmanacMap([
        CategoryConversion(77, 45, 23),
        CategoryConversion(45, 81, 19),
        CategoryConversion(64, 68, 13),
    ]),
    AlmanacMap([
        CategoryConversion(69, 0, 1),
        CategoryConversion(0, 1, 69),
    ]),
    AlmanacMap([
        CategoryConversion(56, 60, 37),
        CategoryConversion(93, 56, 4),
    ])
))

class CategoryConversionTest(unittest.TestCase):
    def test_in_positive(self):
        subject = CategoryConversion(1, 10, 3)
        self.assertTrue(3 in subject)

    def test_in_negative(self):
        subject = CategoryConversion(1, 10, 3)
        self.assertFalse(4 in subject)
    
    def test_convert(self):
        subject = CategoryConversion(1, 10, 3)
        self.assertEqual(subject(3), 12)

class AlmanacMapTest(unittest.TestCase):
    def test_map_case1(self):
        conversion_list = [
            CategoryConversion(98, 50, 2),
            CategoryConversion(50, 52, 48)
        ]
        map = AlmanacMap(conversion_list)
        self.assertEqual(map(79), 81)

    def test_map_case2(self):
        conversion_list = [
            CategoryConversion(98, 50, 2),
            CategoryConversion(50, 52, 48)
        ]
        map = AlmanacMap(conversion_list)
        self.assertEqual(map(14), 14)

    def test_map_case3(self):
        conversion_list = [
            CategoryConversion(98, 50, 2),
            CategoryConversion(50, 52, 48)
        ]
        map = AlmanacMap(conversion_list)
        self.assertEqual(map(55), 57)

    def test_map_case4(self):
        conversion_list = [
            CategoryConversion(98, 50, 2),
            CategoryConversion(50, 52, 48)
        ]
        map = AlmanacMap(conversion_list)
        self.assertEqual(map(13), 13)

class AlmanacSolver1Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(example(79), 82)

    def test_example2(self):
        self.assertEqual(example(14), 43)

    def test_example3(self):
        self.assertEqual(example(55), 86)

    def test_example4(self):
        self.assertEqual(example(13), 35)

class SolvePart1Test(unittest.TestCase):
    def test_solve_part1(self):
        actual = solve_part1([79, 14, 55, 13], example)
        self.assertEqual(actual, 35)

if __name__ == '__main__':
    unittest.main()
