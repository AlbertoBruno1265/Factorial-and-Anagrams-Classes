from Factorial import Factorial
from random import choice


class Anagram(Factorial):

    def __init__(self, word):
        super().__init__()
        self.word = word.upper()
        self.rept = []
        self.total = 0
        self.total_anagrams()

    def total_anagrams(self):
        if self.check_rapetition():
            self.total = super().repetition(len(self.word), self.rept)

        else:
            self.total = super().simple(len(self.word))

    def generation_anagram(self):
        letters = []
        new_word = ""

        for letter in self.word:
            letters.append(letter)

        for n in range(len(self.word)):
            new_letter = choice(letters)
            letters.remove(new_letter)
            new_word += new_letter

        return new_word

    def all_anagrams_possibles(self):
        count = 0

        all_anagrams = []

        while count < self.total:
            anagram = self.generation_anagram()
            if anagram not in all_anagrams:
                all_anagrams.append(anagram)
                count += 1

        all_anagrams.sort()
        return all_anagrams

    def check_rapetition(self):
        repetition = {}

        for letter in self.word:

            if letter not in repetition:
                repetition[letter] = 1

            else:
                repetition[letter] += 1

        for value in repetition.values():
            if value > 1:
                self.rept.append(value)

        return bool(self.rept)
