class Permutation:

    def __init__(self, want_show=False):
        self.want_show = want_show

    def simple(self, num):
        result = 1
        for number in range(num, 0, -1):
            if self.want_show:
                if number != 1:
                    print(f"{number} x", end=" ")
                else:
                    print(f"{number}")

            result *= number

        return result

    def repetition(self, n, r):
        numerator = self.simple(n)
        denominator = 1
        for number in r:
            denominator *= self.simple(number)

        return int(numerator/denominator)

    def circular(self, n):
        return self.simple(n-1)
