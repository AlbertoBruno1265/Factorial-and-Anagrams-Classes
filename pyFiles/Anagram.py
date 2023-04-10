from Permutation import Permutation
from random import choice


class Anagram(Permutation):

    def __init__(self, word):
        super().__init__()
        self.word = word.upper()
        self._rept = []
        self.total = 0
        self._total_anagrams()

    def _total_anagrams(self):
        if self.check_rapetition():
            self.total = super().repetition(len(self.word), self._rept)

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
        all_anagrams = []

        while len(all_anagrams) < self.total:
            anagram = self.generation_anagram()
            if anagram not in all_anagrams:
                all_anagrams.append(anagram)

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
                self._rept.append(value)

        return bool(self._rept)

    def __str__(self):
        return f'The total number of anagrams for "{self.word}" is: {self.total}'


class Game:

    def __init__(self):
        self.word = ""
        self.attempt = ""
        self._answer = ""
        self._round = 1

    def start_game(self):
        print("=============================================")
        print("============   ANAGRAM GAME    ==============")
        while True:
            print("=============================================")
            self.word = str(input("Input a word: "))
            self._answer = Anagram(self.word).generation_anagram()
            while True:
                self.new_round()

                if self.check_result():
                    break

                self._round += 1

            self.end_game()

            if self.restart_game():
                break

    def new_round(self):
        print(f"==============   Round {self._round}   ==================")
        while True:
            self.attempt = str(input("Input your attempt: ")).upper()
            if len(self.attempt) == len(self._answer):
                break
            print("INVALID! The attempt needs to be the same length as the original word")

        self.show_attempt()

    def show_attempt(self):

        for n in range(len(self._answer)):
            if self.attempt[n] == self._answer[n]:
                print(f"\033[32m{self.attempt[n]}\033[m", end="")
            else:
                print(f"\033[31m{self.attempt[n]}\033[m", end="")
        print()

    def check_result(self):
        return self.attempt == self._answer

    def restart_game(self):
        print("=============================================")
        while True:
            ans = str(input("Restart? [Y/N]: ")).upper()
            if ans in "YN":
                break
            print("Invalid! Try again:")

        if ans == "Y":
            self._round = 1
            return False
        else:
            print("==============   GAME OVER    ===============")
            return True

    def end_game(self):
        print("=============================================")
        print("You found the anagram!")
        print(f"You complete the game in {self._round} rounds")

