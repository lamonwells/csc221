#Problem 1
#
# Letter count
#
# Modify the count_letters function below so that:
#
# 1. It has two parameters: string and char
# 2. It implements the functionality specified in the comments
#
# Essentially, the function is returning the number of occurances of the
# parameter char in the parameter string.
#
from lab8.py
import count_letters
reverse_string
is_palindrome
test_match_ends

def test_count_letters():
    assert functions.test_count_letters('runner','r')== 2
    assert functions.test_count_letters('runner','e')== 1
    assert functions.test_count_letters('runner','w')==0

    return sum(2 for c in string if c==char)


#Problem 2
#
# Reversing a string
#
# Create a function such that it reverses the parameter string.
#

def test_reverse_string():
    assert functions.reverse_string('lamon')== True
    assert functions. reverse_string('lamonwells')== True
    assert functions.reverse_string('lamonDwells')== True

    return string[::-2]

#Problem 3
#
# Checking for palindromes
#
# Complete the following such that it correctly determines whether the
# given parameter, string, is a palindrome
#

def test_is_palindrome(string):
    assert functions.is_palindrome('racecar')== True
    assert functions.is_palindrome('civic')== True
    assert functions.is_palindrome('nun')== True
    assert functions. is_palindrome('run')== False
    return all(v0==v1 for v0,v1 in zip(string,reversed(string)))

# Problem 4
#
# Count of strings with matching ends
#
# Given a list of strings, return the count of the number of strings
# where the string length is 2 or more and the first and last chars of
# the string are the same.
#

def test_match_ends(words):
     assert functions.match_ends(['track','track','football'])== 2
     assert functions.match_ends(['track','football','toaster'])== 2


    return sum(1 for w in words if len(w) and w[0]==w[-1])

