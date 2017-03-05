import unittest
from trie import Trie


class TrieTests(unittest.TestCase):
    def test_has_word_single_letter_words(self):
        trie = Trie()
        trie.add_word('a')
        trie.add_word('c')
        trie.add_word('1')

        self.assertTrue(trie.has_word('a'))
        self.assertTrue(trie.has_word('c'))
        self.assertTrue(trie.has_word('1'))
        self.assertFalse(trie.has_word('2'))
        self.assertFalse(trie.has_word('aa'))
        self.assertFalse(trie.has_word('ac'))
        self.assertFalse(trie.has_word('ce'))

    def test_get_words_by_prefix(self):
        trie = Trie()
        trie.add_word('self'); trie.add_word('self1'); trie.add_word('selfself'); trie.add_word('selfselfself');

        self.assertCountEqual(trie.get_words_by_prefix('self'),
                              ['self', 'self1', 'selfself', 'selfselfself'])

    def test_get_words_by_prefix_should_return_words_with_prefix(self):
        trie = Trie()
        trie.add_word('byte')
        trie.add_word('bye')
        trie.add_word('goodbye')
        trie.add_word('bbye')
        trie.add_word('be')
        trie.add_word('bb')
        trie.add_word('b')
        print(trie.get_words_by_prefix('by'))
        self.assertCountEqual(trie.get_words_by_prefix('by'),
                              ['byte', 'bye'])

if __name__ == '__main__':
    unittest.main()
