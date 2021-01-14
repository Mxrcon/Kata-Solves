#Kata Source:
# https://www.codewars.com/kata/5287e858c6b5a9678200083c
#6-Kyu
#Using simple type casting and a loop for sum
def narcissistic( value ):
    str_value = str(value)
    lenght = len(str_value)
    sum = 0
    for i in str_value:
        sum = sum+int(i)**lenght
    if sum == value:
        return True
    else: return False
