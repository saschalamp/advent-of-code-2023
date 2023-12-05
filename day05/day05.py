class CategoryConversion:
    def __init__(self, source, target, length):
        self.source = source
        self.target = target
        self.length = length
    
    def __contains__(self, number):
        return number in range(self.source, self.source + self.length)
    
    def __call__(self, number):
        diff = number - self.source
        return self.target + diff

class AlmanacMap:
    def __init__(self, conversion_list):
        self.conversion_list = conversion_list
    
    def __call__(self, source):
        conversion = next((c for c in self.conversion_list if source in c), lambda x: x)
        return conversion(source)

class AlmanacSolver1:
    def __init__(self, list_of_almanac_maps):
        self.list_of_almanac_maps = list_of_almanac_maps

    def __call__(self, seed):
        return self.call(seed, 0)
    
    def call(self, source, n):
        if n < len(self.list_of_almanac_maps):
            target = self.list_of_almanac_maps[n](source)
            return self.call(target, n + 1)
        return source

def solve_part1(seeds, solver):
    return min(solver(seed) for seed in seeds)

def build_solver1(input):
    _, seeds_raw = input.readline().strip().split(': ')
    seeds = [int(seed) for seed in seeds_raw.split(' ')]

    maps = []
    while True:
        line = input.readline()
        if not line:
            break
        line = line.strip()
        if line.endswith('map:'):
            maps.append(AlmanacMap([]))
        elif len(line) > 0:
            target, source, length = line.split(' ')
            conversion = CategoryConversion(int(source), int(target), int(length))
            maps[-1].conversion_list.append(conversion)
    return seeds, AlmanacSolver1(maps)


def main(file_name: str):
    with open(file_name, "r") as f:
        seeds, solver = build_solver1(f)
        print(solve_part1(seeds, solver))

if __name__ == '__main__':
    main('day05/input')
