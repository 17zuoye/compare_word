# -*- coding: utf-8 -*-

from nltk.stem.wordnet import WordNetLemmatizer
lmtzr = WordNetLemmatizer()

class CompareWord:
    """
    Compare words in normalize format, includes cases, tenses, etc.
    """

    def __init__(self, w1):
        self.original_word = w1
        self.clean_word    = lmtzr.lemmatize(self.original_word.lower())

    def __eq__(self, another):
        if type(another) in [str, unicode]: another = CompareWord(another)
        if not isinstance(another, CompareWord): raise Exception("%s should be CompareWord.class" % another)

        return self.clean_word == another.clean_word

    def __repr__(self): return self.original_word
    def __str__(self):  return self.original_word
    def __hash__(self): return hash(self.clean_word)

    @classmethod
    def load(cls, words):
        return [CompareWord(w1) for w1 in words]


if __name__ == '__main__':
    import unittest

    class TestCompareWord(unittest.TestCase):
        def test_compare(self):
            self.assertEqual(CompareWord("Python"), CompareWord("python"))
            self.assertEqual(CompareWord("desk"), CompareWord("desks"))
            self.assertEqual(CompareWord("Goods"), CompareWord("good"))

            self.assertTrue(CompareWord("desk") in CompareWord.load(["desk", "marry"]))

    unittest.main()
