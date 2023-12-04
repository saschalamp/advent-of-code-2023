def solve_part1(cards):
    if len(cards) == 0:
        return 0 
    return sum(solve_winning_numbers(card) for card in cards)

def solve_winning_numbers(card):
    n = count_winning_numbers(card)
    return 0 if n == 0 else 2**(n - 1)

def count_winning_numbers(card):
    n = 0
    for your_number in card.your_numbers:
        if your_number in card.winning_numbers:
            n += 1
    return n

def solve_part2(cards):
    total_cards = len(cards)
    scores = [1] * total_cards
    for i in range(len(cards)):
        card = cards[i]
        n = count_winning_numbers(card)
        j = i + 1
        while j < i + n + 1 and j < total_cards:
            scores[j] += scores[i]
            j += 1
    return sum(scores)

class Card:
    def __init__(self, winning_numbers, your_numbers):
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers

def build_cards(lines):
    cards = []
    for line in lines:
        _, card_data = line.strip().split(': ')
        raw_winning_numbers, raw_your_numbers = card_data.split(' | ')
        winning_numbers = [n for n in raw_winning_numbers.split(' ') if n != '']
        your_numbers = [n for n in raw_your_numbers.split(' ') if n != '']
        cards.append(Card(winning_numbers, your_numbers))
    return cards

def main(file_name: str):
    with open(file_name, "r") as f:
        cards = build_cards(f)
        print(solve_part1(cards))
        print(solve_part2(cards))


if __name__ == '__main__':
    main('day04/input')
