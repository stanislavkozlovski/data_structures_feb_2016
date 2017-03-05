class TrieNode:
    def __init__(self, end_of_word: bool=False):
        self.words = {}
        self.end_of_word = end_of_word

    def add_word(self, word: str, index: int=0):
        """ Recursively adds a word to our TrieNode structure"""
        if index == len(word):
            self.end_of_word = True
        elif word[index] not in self.words:
            self.words[word[index]] = TrieNode()
        if index + 1 <= len(word):
            self.words[word[index]].add_word(word, index+1)

    def has_word(self, word, index: int=0) -> bool:
        if index == len(word):
            return self.end_of_word
        if word[index] not in self.words:
            return False
        return self.words[word[index]].has_word(word, index+1)

    def get_node_with_prefix(self, word, index=0) -> 'TrieNode' or None:
        if index == len(word):
            return self
        if word[index] not in self.words:
            return None
        return self.words[word[index]].get_node_with_prefix(word, index+1)

    def get_words(self, words: list, prefix: str):
        """ Returns a list of all the words this Node contains"""
        new_words = []
        if self.end_of_word:
            words.append(prefix)
        for key, trie in self.words.items():
            new_words.extend(trie.get_words([], prefix + key))

        words.extend(new_words)
        return words


class Trie:
    """ A simple user-friendly wrapper around the TrieNode structure"""
    def __init__(self):
        self.words = {}

    def add_word(self, word: str):
        index = 0
        f_char = word[index]
        if f_char not in self.words:
            self.words[f_char] = TrieNode()
        self.words[f_char].add_word(word, index+1)

    def has_word(self, word):
        index = 0
        f_char = word[index]
        if f_char not in self.words:
            return False
        return self.words[f_char].has_word(word, index+1)

    def get_words_by_prefix(self, prefix):
        """ Get all the words in the trie that start with the given prefix"""
        first_char = prefix[0]
        if first_char in self.words:
            # Through our first trie_node, get the Node object that goes up to the prefix.
            trie_node = self.words[first_char].get_node_with_prefix(prefix, index=1)
            if trie_node is not None:
                # Once we get it, we want all its children's words
                return trie_node.get_words([], prefix)

        return []


# END_WORD_NODE = TrieNode(end_of_word=True)
# string = 'dream'
# trie = Trie()
# trie.add_word(string)
# trie.add_word(string + 's')
# trie.add_word('d')
# trie.add_word('da')
# print(trie.has_word('d'))
trie = Trie()
# trie = TrieNode()
trie.add_word('dr')
trie.add_word('dream')
trie.add_word('dreams')
print(trie.get_words_by_prefix('dre'))
# print(trie.get_node_with_prefix('dr', 0).get_words([], 'dr'))