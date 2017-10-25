# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Bonus requirements:
#   - Optimise the code for fast retrieval
#   - Write more tests
#   - Thread safe implementation

import unittest
from collections import defaultdict

#Implementation hinges on the idea that sorted characters of words that are anagrams are equal. 
#So input words can be indexed by same character-sorted key.
#It is thread safe, because data is only read, not modified, after anagram object creation.

class Anagrams:
    """Map of anagrams for a set of words."""

    def __init__(self, words):
        self._anagram_index = self._build_anagram_index(words)

    def get_anagrams(self, word):
        return self._anagram_index[self._make_key(word)]

    def _build_anagram_index(self, words):
        index = defaultdict(lambda: [], {})
        for w in words:
            index[self._make_key(w)].append(w)
        return index

    def _make_key(self, word):
        return ''.join(sorted(word.lower()))


class TestAnagrams(unittest.TestCase):

    def test_all_input_words_can_be_looked_up(self):
        a = Anagrams(['one', 'two', 'three'])
        self.assertTrue(a.get_anagrams('one') == ['one'])
        self.assertTrue(a.get_anagrams('two') == ['two'])
        self.assertTrue(a.get_anagrams('three') == ['three'])

    def test_only_same_lenght_words_returned_as_anagrams(self):
        a = Anagrams(['eat', 'tea', 'tear'])
        self.assertTrue(set(a.get_anagrams('eat')) == set(['eat', 'tea']))
        self.assertTrue(a.get_anagrams('tear') == ['tear'])

    def test_empty_list_returned_when_no_anagrams_found(self):
        a = Anagrams(['plate', 'state', 'great'])
        self.assertTrue(a.get_anagrams('greet') == [])
        
    def test_anagrams(self):
        with open('words.txt') as w:
            anagrams = Anagrams(w.read().splitlines())
        self.assertEqual(set(anagrams.get_anagrams('plates')), set(['palest', 'pastel', 'petals', 'plates', 'staple']))
        self.assertEqual(set(anagrams.get_anagrams('eat')), set(['ate', 'eat', 'tea']))

if __name__ == '__main__':
    unittest.main()
