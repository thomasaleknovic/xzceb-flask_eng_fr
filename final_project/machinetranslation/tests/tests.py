import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(), 'Please, insert a text.')


class TestFrenchToEnglish(unittest.TestCase):

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(), 'Please, insert a text.')


unittest.main()
