# -*- coding: utf-8 -*-

import os, sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

import unittest
from compare_word import CompareWord


class TestCompareWord(unittest.TestCase):
    def test_compare(self):
        self.assertEqual(CompareWord("Python"), CompareWord("python"))
        self.assertEqual(CompareWord("desk"), CompareWord("desks"))
        self.assertEqual(CompareWord("Goods"), CompareWord("good"))

        self.assertTrue(CompareWord("desk") in CompareWord.load(["Desk", "marry"]))

if __name__ == '__main__': unittest.main()
