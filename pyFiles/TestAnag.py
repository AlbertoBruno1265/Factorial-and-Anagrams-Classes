import Anagram

arara = Anagram.Anagram("arara")
alberto = Anagram.Anagram("alberto")

print(f"O total de anagramas para a palavra: '{arara.word}' é: {arara.total}")
print(f"O total de anagramas para a palavra: '{alberto.word}' é: {alberto.total}")

print(arara.all_anagrams_possibles())
print(alberto.all_anagrams_possibles())
