import unittest

from .trie import insert_look_in_trie, get_all_leaves_for_trie, get_all_looks_for_partial_name

class TrieTest(unittest.TestCase):

    def test_trie_add(self):
        root = {}
        insert_look_in_trie(root, "abc", "look")
        self.assertEqual(root, {'a': {'b': {'c': {'abc': 'look'}}}})

    def test_trie_add_long_name(self):
        root = {}
        insert_look_in_trie(root, "abc def", "look")
        self.assertEqual(root, {'a': {'b': {'c': {'abc': 'look'}}},
                                'd': {'e': {'f': {'def': 'look'}}}})

    def test_get_all_leave_for_single_trie_entry(self):
        root = {}
        insert_look_in_trie(root, "abc", "look")
        result = get_all_leaves_for_trie(root)
        self.assertEqual({"look"}, result)

    def test_get_all_leave_for_multiple_trie_entries(self):
        root = {}
        insert_look_in_trie(root, "abc def", "look")
        result = get_all_leaves_for_trie(root)
        self.assertEqual({"look"}, result)

    def test_get_all_leave_for_multiple_different_trie_entries(self):
        root = {}
        insert_look_in_trie(root, "abc def", "look")
        insert_look_in_trie(root, "ghi", "another")
        insert_look_in_trie(root, "abd", "thing")
        result = get_all_leaves_for_trie(root)
        self.assertEqual({"look", "another", "thing"}, result)

    def test_lookup_single_look_in_trie(self):
        root = {}
        insert_look_in_trie(root, "abc def", "look")
        insert_look_in_trie(root, "ghi", "another")
        insert_look_in_trie(root, "abd", "thing")
        result = get_all_looks_for_partial_name(root, "gh")
        self.assertEqual({"another"}, result)

