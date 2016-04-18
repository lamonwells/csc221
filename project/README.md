# Final Project Exercises
## Leap
Write a program that will take a year and report if it is a leap year.

The tricky thing here is that a leap year in the Gregorian calendar occurs:

```
on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
        unless the year is also evenly divisible by 400
```
  
    
For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap
year, but 2000 is.

Implement a function `is_leap_year(year)` that takes one parameter,
`year` (an integer), and returns `True` if the year is a leap year and
`False` otherwise.

A complete set of unit tests for this function shall be included,
using both the `unittest` and `doctest` modules.

## RNA Transcription

Both DNA and RNA strands are a sequence of nucleotides.

The four nucleotides found in DNA are adenine (A), cytosine (C),
guanine (G) and thymine (T).

The four nucleotides found in RNA are adenine (A), cytosine (C),
guanine (G) and uracil (U).

Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

- G -> C
- C -> G
- T -> A
- A -> U

Implement a function `to_rna(dna)` that takes one parameter, `dna` (a
string), and returns its RNA complement (per RNA transcription) as a
string.

The function shall meet these conditions:

- `to_rna` should be able to handle DNA nucleotides in either upper or
  lowercase form and return them in the same form they were given
- `to_rna` should also be robust to whitespace, preserving whatever
  whitespace contained in the `dna` parameter

A complete set of unit tests for this function shall be included,
using both the `unittest` and `doctest` modules.

## RNA Nucleotide Count

Implement a function `rna_count(dna)` that takes one parameter, `dna`
(a string), and returns a dictionary with the RNA nucleotides (`'A'`,
`'C'`, `'G'`, and `'U'`) as keys and the number of occurances of each
nucleotide as the the value, after transcribing the original DNA
strand to its RNA complement.

The function shall meet these conditions:

- `rna_count` should be able to handle DNA strings in either upper or
  lowercase form and return the dictionary with uppercase keys
- `rna_count` should also be robust to whitespace, ignoring it

A complete set of unit tests for this function shall be included,
using both the `unittest` and `doctest` modules.

## RNA Nucleotide Strand Count

Implement a function `rna_strand_count(dna, strands)` that takes two
parameters, `dna` (a string) and `strands` (a list of strings), and
returns a dictionary whose keys are the individual strings in
`strands` and values are the number of occurances of those strings in
the RNA complement transcribed from the original DNA.

All matching strands should be counted, not just disjoint
(non-overlapping) strands. E.g.

```
>>> rna_strand_count('AAAA', ['AA'])
{'AA': 3}
```

The function shall meet these conditions:

- `rna_count` should be able to handle DNA strings in either upper or
  lowercase form and return the dictionary with keys in the form given
- `rna_count` should also be robust to whitespace:
  - Whitespace can be assumed not to be part of a strand
  - For the purpose of counting strands, whitespace in the DNA string
    can be stripped

A complete set of unit tests for this function shall be included,
using both the `unittest` and `doctest` modules.

