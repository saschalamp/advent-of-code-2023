import functools

def solve_part1(cards):
    if len(cards) == 0:
        return 0 
    return sum(solve_card(card) for card in cards)

def solve_card(card):
    this_points = 0
    for your_number in card.your_numbers:
        if your_number in card.winning_numbers:
            this_points = 1 if this_points == 0 else this_points * 2
    return this_points

class Card:
    def __init__(self, winning_numbers, your_numbers):
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers

def build_cards(lines):
    cards = []
    for line in lines:
        card_number, card_data = line.strip().split(': ')
        raw_winning_numbers, raw_your_numbers = card_data.split(' | ')
        winning_numbers = [n for n in raw_winning_numbers.split(' ') if n != '']
        your_numbers = [n for n in raw_your_numbers.split(' ') if n != '']
        cards.append(Card(winning_numbers, your_numbers))
    return cards

def main(file_name: str):
    with open(file_name, "r") as f:
        cards = build_cards(f)
        print(solve_part1(cards))


if __name__ == '__main__':
    main('day04/input')
