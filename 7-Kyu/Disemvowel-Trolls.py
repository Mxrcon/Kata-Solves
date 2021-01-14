#Kata Source:
# https://www.codewars.com/kata/52fba66badcd10859f00097e
#7-Kyu
#String fundament and compreension list
def disemvowel(string):
    vowels =["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    List= [i for i in string if i not in vowels]
    return "".join(List)
