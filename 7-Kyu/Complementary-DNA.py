#Kata Source:
# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
#7-Kyu
#String fundament dict usage
 def DNA_strand(dna):
    complementary =[]
    d = {"A":"T","T":"A","C":"G","G":"C"}
    for i in dna:
        complementary.append(d[i])
    return "".join(complementary)
