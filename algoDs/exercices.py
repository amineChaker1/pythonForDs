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