import unittest
from src.main import boyer_moore_search

class TestBoyerMooreSearch(unittest.TestCase):

    def test_single_occurrence(self):
        haystack = "ababcababcabcabc"
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [2, 7, 10, 13])

    def test_multiple_occurrences(self):
        haystack = "abcabcabc"
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [0, 3, 6])

    def test_no_occurrence(self):
        haystack = "abcdefgh"
        needle = "xyz"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_needle(self):
        haystack = "abcabcabc"
        needle = ""
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack(self):
        haystack = ""
        needle = "abc"
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

    def test_empty_haystack_and_needle(self):
        haystack = ""
        needle = ""
        result = boyer_moore_search(haystack, needle)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
