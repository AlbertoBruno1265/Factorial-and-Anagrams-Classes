from Anagram import Anagram


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
