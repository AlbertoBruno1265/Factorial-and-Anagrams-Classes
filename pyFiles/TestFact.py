import Factorial

fat = Factorial.Factorial(want_show=False)
print("-=" * 25 + "-")
print(fat.simple(5))
print("-=" * 25 + "-")
print(fat.repetition(7, (3, 2, 2)))
print("-=" * 25 + "-")
print(fat.circular(5))
