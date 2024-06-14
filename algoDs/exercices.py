### DATA TYPES 
## Make a number given negative
def make_negative( number ):
    if number > 0:
        return -number
    else :
        return number
make_negative(-12)
# the abs function gives the absolute value of a number
def makeNegative(num):
    return -abs(num)
makeNegative(42)
## remove the first and last charachter from string
def remove_char(s):
    return s[1:-1]
## remove spaces in the string 
def noSpace(x):
    word = ""
    for char in x:
        if char != " " :
            word = word + char
    return word
noSpace("Hello wolrd")


### STRINGS
## reverse a string
def solution(string):
    return string[::-1]
## check string ending with a function
def solution(text, ending):
    return text.endswith(ending)
## concatenation
def bonus_time(salary, bonus):
    figure = 0
    if bonus == True :
        figure = salary * 10
        return "$" + str(figure)
    else :
        return "$" + str(salary)
## abrreveiate
def abbrev_name(name):
    abv = ""
    abv = abv + name[0]
    for x in range(len(name)) :
        if name[x] == " ":
            abv = abv + "." + name[x+1]
        else:
            continue
    return abv.upper()
## turn DNA into RNA 
def dna_to_rna(dna):
    rna = ""
    for x in dna :
        if x == "T":
            rna = rna + "U"
        else :
            rna = rna + x
    return rna


### Arrays
## counting specific elements in a list
def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x == True:
            count += 1
        else :
            continue
    return count
## turn array of numbers into binary
# first one nut completed using functions
def binary_array_to_number(arr):
    zero = "0o"
    one = "0b"
    if arr[0] == 1 :
        for x in arr :
            one = one + x
            print(one)
    else :
        for y in arr :
            zero = zero + y
            print(zero)
binary_array_to_number([0, 0, 0, 1])
# second one using based math
def binary_array_to_number(arr):
    total = 0
    i = 1
    for num in arr[::-1]:
        total += (i*num)
        i *= 2
    return total
binary_array_to_number([1, 1, 1, 1])
## needle in haystack 
def find_needle(haystack):
    index = 0
    for x in haystack :
        if x == "needle":
            return f"found the needle at position {index}"
        index += 1
## remove the smallest number even if it repeats
def remove_smallest(numbers):
    com = numbers.copy()
    if len(com) == 0 :
        return com
    else :
        min = com[0]
        for x in com :
            if x < min :
                min = x
        index = com.index(min)
        del com[index]
        return com
## Convert number to reversed array of digits
def digitize(n):
    res = []
    s = str(n)
    for x in s[::-1]:
        res.append(int(x))
    return res