def solve_part1(schematic: list[list[str]]) -> int :
    result = 0
    for row_index in range(len(schematic)):
        row = schematic[row_index]
        numbers_coords = number_coords(row)
        for left, right in numbers_coords:
            if is_adjacent(schematic, row_index, left, right):
                result += as_int(row[left:right+1])
    return result

def number_coords(schematic: list[str]) -> list[tuple[int]]:
    i = 0
    current_number_start: int = None
    numbers = []
    while i < len(schematic):
        if schematic[i].isdigit() and current_number_start is None:
            current_number_start = i
        elif not schematic[i].isdigit() and current_number_start is not None:
            numbers.append((current_number_start, i - 1))
            current_number_start = None
        i += 1
    if current_number_start is not None:
        numbers.append((current_number_start, i - 1))
    return numbers

def is_adjacent(schematic, row_index, left, right):
    if left > 0 and schematic[row_index][left - 1] != '.':
        return True
    if right + 1 < len(schematic[row_index]) and schematic[row_index][right + 1] != '.':
        return True
    if row_index > 0 and is_symbol_in_row(schematic[row_index - 1], left, right):
        return True
    if row_index < len(schematic) - 1 and is_symbol_in_row(schematic[row_index + 1], left, right):
        return True
    return False

def is_symbol_in_row(row, left, right) -> bool:
    if left > 0:
        left -= 1
    if right < len(row) - 1:
        right += 1
    for i in range(left, right + 1):
        if is_symbol(row[i]):
            return True
    return False

def is_symbol(p):
    return p != '.'

def solve_part2(schematic: list[list[str]]) -> int :
    result = 0
    for row_index in range(len(schematic)):
        row = schematic[row_index]
        for field_index in range(len(row)):
            if row[field_index] == '*':
                result += calculate_gear(schematic, row_index, field_index)
    return result

def calculate_gear(schematic, row_index, field_index):
    numbers = collect_numbers(schematic, row_index, field_index)
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0

def collect_numbers(schematic, row_index, field_index):
    this_row = schematic[row_index]
    numbers = []
    numbers.append(get_number_to_the_left(this_row, field_index - 1))
    numbers.append(get_number_to_the_right(this_row, field_index + 1))
    if row_index > 0:
        numbers += get_number(schematic[row_index - 1], field_index)
    if row_index < len(schematic) - 1:
        numbers += get_number(schematic[row_index + 1], field_index)
    return [int(n) for n in numbers if n is not None]

def get_number(row, index):
    center = row[index]
    right = get_number_to_the_right(row, index + 1)
    left = get_number_to_the_left(row, index - 1)

    if center.isdigit():
        number = center
        if right is not None:
            number += right
        if left is not None:
            number = left + number
        return [number]
    return [left, right]

def get_number_to_the_left(row, right_most_index):
    number = None
    i = right_most_index
    while i >=0 and row[i].isdigit():
        if number is None:
            number = row[i]
        else:
            number = row[i] + number
        i -= 1
    return number

def get_number_to_the_right(row, left_most_index):
    number = None
    i = left_most_index
    while i < len(row) and row[i].isdigit():
        if number is None:
            number = row[i]
        else:
            number = number + row[i]
        i += 1
    return number

def as_int(partial_list):
    return int(''.join(partial_list))

def build_schematic(lines):
    schematic = []
    for line in lines:
        schematic.append([*line.strip()])
    return schematic

def main(file_name: str):
    with open(file_name, "r") as f:
        schematic = build_schematic(f)
        print(solve_part1(schematic))
        print(solve_part2(schematic))

if __name__ == '__main__':
    main('day03/input')

