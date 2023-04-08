import Anagram

abc = Anagram.Anagram("abc")
eed = Anagram.Anagram("eed")

print(abc)
print(eed)

print("-=" * 25 + "-")

print(abc.generation_anagram())
print(eed.generation_anagram())

print("-=" * 25 + "-")

print(abc.all_anagrams_possibles())
print(eed.all_anagrams_possibles())

print("-=" * 25 + "-")

if abc.check_rapetition():
    print("Have repetition!")
else:
    print("Don't have repetition!")

if eed.check_rapetition():
    print("Have repetition!")
else:
    print("Don't have repetition")
