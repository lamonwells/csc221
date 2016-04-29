#Final Project Exercises

# Problem 1
# Write a program that will take a year and report if it is a leap year.
#
# The tricky thing here is that a leap year in the Gregorian calendar occurs:
#
#```
# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#    unless the year is also evenly divisible by 400
#```


# For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap
# year, but 2000 is.

# Implement a function `is_leap_year(year)` that takes one parameter,
# `year` (an integer), and returns `True` if the year is a leap year and
# `False` otherwise.

# A complete set of unit tests for this function shall be included,
# using both the `unittest` and `doctest` modules.

def is_leap_year(year):
    '''
    >>> is_leap_year(1996)
    True
    >>> is_leap_year(1997)
    False
    >>> is_leap_year(2001)
    False
    >>> is_leap_year(2004)
    True
     '''
    if year % 400==0:
        return True

    if year % 100==0:
        return False
    if year % 4==0:
        return True
    else:
        return False



# Problem 2
### RNA Transcription

#Both DNA and RNA strands are a sequence of nucleotides.

#The four nucleotides found in DNA are adenine (A), cytosine (C),
#guanine (G) and thymine (T).

#The four nucleotides found in RNA are adenine (A), cytosine (C),
#guanine (G) and uracil (U).

#Given a DNA strand, its transcribed RNA strand is formed by replacing
#each nucleotide with its complement:

# - RNA Transcription
#-  G -> C
# - C -> G
# - T -> A
# - A -> U

#Implement a function `to_rna(dna)` that takes one parameter, `dna` (a
#string), and returns its RNA complement (per RNA transcription) as a
#string.

#The function shall meet these conditions:

# - `to_rna` should be able to handle DNA nucleotides in either upper or
#  lowercase form and return them in the same form they were given
# - `to_rna` should also be robust to whitespace, preserving whatever
#  whitespace contained in the `dna` parameter

# A complete set of unit tests for this function shall be included,
# using both the `unittest` and `doctest` modules.
def to_rna(dna):
    inverse = { G : C,
                C : G,
                T : A,
                A : T}

    return (inverse[nucleotide] for nucleotide in dna )

#Implement a function `rna_count(dna)` that takes one parameter, `dna`
#(a string), and returns a dictionary with the RNA nucleotides (`'A'`,
#`'C'`, `'G'`, and `'U'`) as keys and the number of occurances of each
#nucleotide as the the value, after transcribing the original DNA
#strand to its RNA complement.

def rna_count(dna):
    d={}
    ' count apperance of letters'
    for l in dna:
        d[w] = dna.count(w)





