import enchant

class WordleBot:

    def __init__(self):
        self.valid_letters = list("abcdefghijklmnopqrstuvwxyz")
        self.tried_words = [[]]
        self.known_letters = [None, None, None, None, None]
        self.include_letters = []
        self.word_threshold = 0.8
        self.ench = enchant.Dict("en_US")

    def set_known_letter(self, letter, position):
        self.known_letters[position] = letter

    def set_include_letters(self, letters):
        self.include_letters = letters

    def remove_invalid_letters(self, letters):
        for letter in letters:
            if letter in self.valid_letters:
                self.valid_letters.remove(letter)

    def is_valid_word(self, word):
            return self.ench.check(word)

    def find_all_valid_words(self):
        """
        This function runs through all the combinations of available letters in valid_letters combined with
        the known letters in known_letters, and returns all the words that are valid English words
        """
        valid_words = []
        spaces_to_be_filled = self.known_letters.count(None)

        if spaces_to_be_filled == 0:
            # If no spaces are left to fill, check if the known_letters form a valid word
            word = ''.join(self.known_letters)
            if self.is_valid_word(word):
                return [word]
            return []

        # Generate all possible combinations of letters for the unknown positions
        from itertools import product

        for combination in product(self.valid_letters, repeat=spaces_to_be_filled):
            word = self.known_letters[:]
            combination_index = 0

            # Fill the unknown positions with the current combination
            for i in range(len(word)):
                if word[i] is None:
                    word[i] = combination[combination_index]
                    combination_index += 1

            word_str = ''.join(word)
            if self.is_valid_word(word_str):
                if self.include_letters:
                    if all(letter in word_str for letter in self.include_letters):
                        valid_words.append(word_str)
                else:
                    valid_words.append(word_str)

        # # filter out words that do not include the include_letters
        # if self.include_letters:
        #     for word in valid_words:
        #         if not all(letter in word for letter in self.include_letters):
        #             valid_words.remove(word)

        return valid_words


if __name__ == '__main__':
    bot = WordleBot()
    # bot.set_known_letter('e', 1)
    # bot.set_known_letter('c', 3)
    # bot.set_known_letter('s', 3)
    bot.set_include_letters(list('ih'))
    bot.remove_invalid_letters(list('eroasgcn'))
    valid_words = bot.find_all_valid_words()
    print(valid_words)