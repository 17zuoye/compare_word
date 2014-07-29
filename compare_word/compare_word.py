# -*- coding: utf-8 -*-

from etl_utils import ld

class CompareWord:

    def __init__(self, w1):
        self.original_word = w1
        self.clean_word    = ld.lemmatize(self.original_word.lower())

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
