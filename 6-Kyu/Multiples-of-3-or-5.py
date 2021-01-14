#Kata Source:
# https://www.codewars.com/kata/514b92a657cdc65150000006
#6-Kyu
#List methods and modulo usage
def solution(number):
    multiples = []
    for i in range(number):
        if i%3 ==0 or i%5 ==0:
            multiples.append(i)
    return sum(multiples)
