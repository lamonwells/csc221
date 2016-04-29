import unittest

from year import is_leap_year


class YearTest(unittest.TestCase):
    def test_leap_year(self):
        self.assertTrue(is_leap_year(1996))

    def test_non_leap_year(self):
        self.assertFalse(is_leap_year(1997))

    def test_non_leap_even_year(self):
        self.assertFalse(is_leap_year(1998))


from dna import to_rna

    def test_complement_guanine_to_cytosine(self):
         self.assertEqual('C', to_rna('G'))

    def test_complement_cytosine_to_guanine(self):
          self.assertEqual('G', to_rna('C'))


    def test_complement_thymine_to_adenine(self):
         self.assertEqual('A', to_rna('T'))


    def test_complement_adenine_to_uracil(self):
         self.assertEqual ('U', to_rna('A'))


if __name__=='__main__':
     unittest.main()








