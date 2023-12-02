import functools
import operator

class Bag:
    def __init__(self, red=0, green=0, blue=0) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def aggregate(self, other: "Bag") -> "Bag":
        self.red = max(self.red, other.red)
        self.green = max(self.green, other.green)
        self.blue = max(self.blue, other.blue)

    def __iter__(self):
        yield self.red
        yield self.green
        yield self.blue
    
    def __repr__(self):
        return str((self.red, self.green, self.blue))

def create_bag(line):
    raw_draws = line.split(', ')
    bag = Bag()
    for raw_draw in raw_draws:
        cubes, color = raw_draw.split(' ')
        setattr(bag, color, int(cubes))
    return bag

class Game:
    def __init__(self, max_red, max_green, max_blue) -> None:
        self.max_red = max_red
        self.max_green = max_green
        self.max_blue = max_blue

    def solve(self, lines):
        return sum(self.solve_game(line.strip()) for line in lines)
    
    def solve_game(self, line):
        raw_game_id, game = line.split(': ')
        bags = [create_bag(raw_draws) for raw_draws in game.split('; ')]
        if not self.is_valid_game(bags):
            return 0

        game_id = raw_game_id[raw_game_id.find(' ')+1:]
        return int(game_id)

    def is_valid_game(self, bags: list[Bag]):
        return all(self.is_valid_bag(bag) for bag in bags)
    
    def is_valid_bag(self, bag: Bag):
        return bag.blue <= self.max_blue \
            and bag.red <= self.max_red \
                and bag.green <= self.max_green

game = Game(max_red=12, max_green=13, max_blue=14)

def solve_line_part2(line):
    _, game = line.split(': ')
    raw_draws = game.split('; ')
    max_bag = Bag()
    for raw_draw in raw_draws:
        this_bag = create_bag(raw_draw)
        max_bag.aggregate(this_bag)
    return functools.reduce(operator.mul, max_bag, 1)

def solve_part2(lines):
    return sum(solve_line_part2(line.strip()) for line in lines)

def main(file_name: str):
    with open(file_name, "r") as f:
        print(game.solve(f))
    with open(file_name, "r") as f:
        print(solve_part2(f))

if __name__ == '__main__':
    main('day02/input')
