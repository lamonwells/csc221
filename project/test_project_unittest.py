import unittest

from project import is_leap_year

class YearTest(unittest.TestCase):

  def test_is_leap_year(self):
        self.assertTrue(is_leap_year(1996));
        self.assertFalse(is_leap_year(1997));
        self.assertFalse(is_leap_year(1998));




from project import to_rna

class ProjectTests(unittest.TestCase):
    def test_transcribes_guanine_to_cytosine(self):
         self.assertEqual('C', to_rna('G'))
         self.assertEqual('c', to_rna('g'))

    def test_transcribes_cytosine_to_guanine(self):
         self.assertEqual('G', to_rna('C'))
         self.assertEqual('g', to_rna('c'))


    def test_transcribes_thymine_to_adenine(self):
         self.assertEqual('A', to_rna('T'))
         self.assertEqual('a', to_rna('c'))

    def test_transcribes_adenine_to_uracil(self):
         self.assertEqual('U', to_rna('A'))
         self.assertEqual('u', to_rna('a'))

    def test_transcribes_all(self):
         self.assertEqual('GGGG', to_rna('CCCC'))
         self.assertEqual('gggg', to_rna('cccc'))


from project import rna_count

class PROJECTTests(unittest.TestCase):
    def test_rna_count(self):
        self.assertEqual(
            {'letter': 1},
            rna_count('letter')
    )
