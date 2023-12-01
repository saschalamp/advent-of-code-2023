import functools

number_words = {
    'one': 1,
    'two': 2,
    'six': 6,
    'four': 4,
    'five': 5,
    'three': 3,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def solve(lines: list[str], use_number_words: bool):
    return functools.reduce(lambda sum, line: sum + solve_single_line(line, use_number_words), lines, 0)

def solve_single_line(line: str, use_number_words: bool):
    lexer = Lexer(line, use_number_words)
    return int(lexer.left() + lexer.right())

class Lexer:
    def __init__(self, line: str, use_number_words: bool) -> None:
        self.use_number_words = use_number_words
        self.line = line
        self.left_ptr = 0
        self.right_ptr = len(line) - 1

    def left(self) -> str:
        while self.left_ptr < len(self.line):
            if self.single_digit(self.left_ptr):
                return self.line[self.left_ptr]
            if self.number_word(self.left_ptr, self.left_ptr + 3):
                return self.word_to_number(self.left_ptr, self.left_ptr + 3)
            if self.number_word(self.left_ptr, self.left_ptr + 4):
                return self.word_to_number(self.left_ptr, self.left_ptr + 4)
            if self.number_word(self.left_ptr, self.left_ptr + 5):
                return self.word_to_number(self.left_ptr, self.left_ptr + 5)
            self.left_ptr += 1

    def right(self) -> str:
        while self.right_ptr >= 0:
            if self.single_digit(self.right_ptr):
                return self.line[self.right_ptr]
            if self.number_word(self.right_ptr - 2, self.right_ptr + 1):
                return self.word_to_number(self.right_ptr - 2, self.right_ptr + 1)
            if self.number_word(self.right_ptr - 3, self.right_ptr + 1):
                return self.word_to_number(self.right_ptr - 3, self.right_ptr + 1)
            if self.number_word(self.right_ptr - 4, self.right_ptr + 1):
                return self.word_to_number(self.right_ptr - 4, self.right_ptr + 1)
            self.right_ptr -= 1
    
    def single_digit(self, ptr):
        return self.line[ptr].isdigit()
    
    def word(self, l, r):
        return self.line[l:r]
    
    def word_to_number(self, l, r):
        return str(number_words[self.line[l:r]])
    
    def number_word(self, l, r):
        if not self.use_number_words:
            return False
        word = self.word(l, r)
        if word in number_words:
            return True
        return False

def main(file_name: str):
    with open(file_name, "r") as f:
        print(solve(f, False))
    with open(file_name, "r") as f:
        print(solve(f, True))

if __name__ == '__main__':
    main('day01/input')
