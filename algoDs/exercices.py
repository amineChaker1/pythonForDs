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