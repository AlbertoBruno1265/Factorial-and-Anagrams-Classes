import Anagram

ana = Anagram.Anagram("abc")

print(f"O total de anagramas para a palavra: '{ana.word}' é: {ana.total_anagrams()}")

print(ana.generation_anagram())
