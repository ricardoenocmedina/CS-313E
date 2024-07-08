"""
File: test_wordleHelper.py
Description: The purpose of this program is to test WordleHelper methods
Student Name: Ricardo Medina
Student UT EID: rem3885
Course Name: CS 313E
Unique Number: 50775
"""

import unittest
from wordleHelperFinalProject import *
import os

class TestWordle(unittest.TestCase):
    def setUp(self):
        """"""
        self.t = Trie()
        self.list_of_words = ['still','child','glass','clear','north',
                         'solve','wings','grown','foods','fruit',
                         'bones','wants','apart','touch','angle'
                         'sheep','spend','shoes','broke','style'
                         'empty','score','shore','wheel','quick']
        
        for word in self.list_of_words:
            self.t.insert(word)

    def test_001_search(self):
        """tests for search method functionality"""

        self.assertEqual(self.t.search('sho'), ['shoes','shore'])
           
    def test_002_insert(self):
        """tests for insert method functionality"""

        word = 'happy'
        self.t.insert(word)
        
        self.assertEqual(self.t.search('happy'), ['happy'])

    def test_003_is_empty(self):
        """tests for if a word is not in the list"""

        self.assertAlmostEqual(self.t.search('smash'), [])

    def test_004_is_instance(self):
        """checks if created trie is an instance of trie"""
        
        self.assertIsInstance(self.t,Trie)

    def test_005_find_viable_words(self):
        """checks that root node is created and not None"""
    
        self.assertIsNotNone(self.t.root)
    
    def test_006_print(self):
        """checks if txt file is created properly and if print method works"""

        words = ['still','child','glass','clear','north',
                         'solve','wings','grown','foods','fruit',
                         'bones','wants','apart','touch','angle'
                         'sheep','spend','shoes','broke','style'
                         'empty','score','shore','wheel','quick']
        
        test = Trie()

        for word in words:
            test.insert(word)
        
        txt = test.print_trie()

        with open('test_file.txt', 'w') as file:
            file.write(txt)
        
        self.assertTrue(os.path.exists('test_file.txt'))

if __name__ == '__main__':
    unittest.main()
