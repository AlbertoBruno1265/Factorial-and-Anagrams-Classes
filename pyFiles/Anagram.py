from Factorial import Factorial


class Anagram(Factorial):

    def __init__(self, word):
        super().__init__()
        self.word = word.upper()
        self.rept = []

    def total_anagrams(self):
        if self.check_rapetition():
            return super().repetition(len(self.word), self.rept)

        else:
            return super().simple(len(self.word))

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
