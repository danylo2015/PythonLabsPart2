class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for symbol in word:
            if symbol not in node.children:
                node.children[symbol] = TrieNode()
            node = node.children[symbol]
        node.end_of_word = True

    def search_word(self, word):
        node = self.root
        for symbol in word:
            if symbol not in node.children:
                return False
            node = node.children[symbol]
        return node.end_of_word

    def search_for_prefix(self, prefix):
        node = self.root
        for symbol in prefix:
            if symbol not in node.children:
                return False
            node = node.children[symbol]
        return True


def create_trie_from_patterns(patterns):
    trie = Trie()
    for pattern in patterns:
        trie.insert(pattern)
    return trie
