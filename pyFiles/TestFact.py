import Factorial

fat = Factorial.Factorial(want_show=False)
fat2 = Factorial.Factorial(want_show=True)
print("--------------------------------------------")
print(fat.simple(5))
print(fat.simple(7))
print("--------------------------------------------")
print(fat.repetition(7, (3, 2, 2)))
print("--------------------------------------------")
print(fat.circular(5))
