import unittest
from src.trie import *


class TestTrie(unittest.TestCase):
    def test_default(self):
        patterns = ["brawlstars", "leagueoflegends", "apple", "cucumber", "watermelon"]
        trie = create_trie_from_patterns(patterns)
        self.assertEqual(trie.search_word("brablsas"), False)
        self.assertEqual(trie.search_for_prefix("leag"), True)

    def test_empty_trie_1(self):
        patterns = [" "]
        trie = create_trie_from_patterns(patterns)
        self.assertEqual(trie.search_word(" "), True)
        self.assertEqual(trie.search_for_prefix(" "), True)

    def test_empty_trie_2(self):
        patterns = []
        trie = create_trie_from_patterns(patterns)
        self.assertEqual(trie.search_word(" "), False)
        self.assertEqual(trie.search_for_prefix(" "), False)

    def test_all_same(self):
        patterns = ["brawlstars", "brawlstars", "brawlstars", "brawlstars", "brawlstars"]
        trie = create_trie_from_patterns(patterns)
        self.assertEqual(trie.search_word("brawlstars "), False)
        self.assertEqual(trie.search_for_prefix("stars"), False)

