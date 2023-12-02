import unittest

from day02 import game, solve_part2


class Day02Test(unittest.TestCase):
    def test_solve_one_blue_draw (self):
        lines = ["Game 1: 1 blue"]
        sum = game.solve(lines)
        self.assertEqual(sum, 1)

    def test_solve_one_blue_draw_different_game_id (self):
        lines = ["Game 4: 1 blue"]
        sum = game.solve(lines)
        self.assertEqual(sum, 4)

    def test_solve_one_blue_draw_too_big(self):
        lines = ["Game 4: 15 blue"]
        sum = game.solve(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_red_draw_too_big(self):
        lines = ["Game 42: 13 red"]
        sum = game.solve(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_red_draw_too_big(self):
        lines = ["Game 42: 14 green"]
        sum = game.solve(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_bag_valid(self):
        lines = ["Game 42: 3 blue, 4 red, 1 green"]
        sum = game.solve(lines)
        self.assertEqual(sum, 42)

    def test_solve_one_bag_invalid_red(self):
        lines = ["Game 42: 3 blue, 42 red, 1 green"]
        sum = game.solve(lines)
        self.assertEqual(sum, 0)

    def test_solve_multiple_bags(self):
        lines = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"]
        sum = game.solve(lines)
        self.assertEqual(sum, 1)

    def test_solve_multiple_games(self):
        lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        sum = game.solve(lines)
        self.assertEqual(sum, 8)

    def test_solve_game_99(self):
        lines = [
            "Game 99: 4 green, 3 red; 3 green; 1 red, 2 green; 2 red, 1 green, 2 blue; 2 red, 4 green; 1 green, 2 blue, 1 red"
        ]
        sum = game.solve(lines)
        self.assertEqual(sum, 99)


class Day02Part2Test(unittest.TestCase):

    def test_solve_one_blue_draw (self):
        lines = ["Game 1: 1 blue"]
        sum = solve_part2(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_red_draw (self):
        lines = ["Game 1: 5 red"]
        sum = solve_part2(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_green_draw (self):
        lines = ["Game 1: 5 green"]
        sum = solve_part2(lines)
        self.assertEqual(sum, 0)

    def test_solve_one_of_each (self):
        lines = ["Game 1: 1 green, 1 red, 1 blue"]
        sum = solve_part2(lines)
        self.assertEqual(sum, 1)

    def test_solve_any_of_each (self):
        lines = ["Game 1: 2 green, 3 red, 4 blue"]
        sum = solve_part2(lines)
        self.assertEqual(sum, 24)

    def test_solve_any_of_each_multiple_draws_in_game(self):
        lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
        ]
        sum = solve_part2(lines)
        self.assertEqual(sum, 48)

    def test_solve_any_of_each_multiple_games(self):
        lines = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
        ]
        sum = solve_part2(lines)
        self.assertEqual(sum, 2286)


if __name__ == '__main__':
    unittest.main()
