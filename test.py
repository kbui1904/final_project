import spacy
import keywords as kw
import unittest

text = '''Python is one of the most popular programming languages today 
and is easy for beginners to learn because of its readability.
It is a free, open-source programming language with extensive support modules 
and community development, easy integration with web services, user-friendly 
data structures, and GUI-based desktop applications. '''

# String to perform the assessment in the 'extract_words' test   
s = 'programming, language, easy'

# Dictionary to perform the assessment in the 'test_count' test   
d = {'popular': 1, 'programming': 2, 'language': 2, 'today': 1, 'easy': 2, 'beginner': 1, 'readability': 1, 'free': 1, 'open': 1, 'source': 1, 'extensive': 1, 'support': 1, 'module': 1, 'community': 1, 'development': 1, 'integration': 1, 'web': 1, 'service': 1, 'user': 1, 'friendly': 1, 'datum': 1, 'structure': 1, 'gui': 1, 'desktop': 1, 'application': 1}


class TestStringMethods(unittest.TestCase):
    
 
    def test_hotwords(self):
        # This function tests the 'kw.extract_words(text)' function
        # Do not modify the function name
        # Insert your code here:
        self.assertEqual(s, kw.extract_words(text))

    def test_count(self):
        # This function tests the 'kw.words_count' function
        # Requires to use 'kw.extract_all_words(text)' as an intermediate step to get the words list        
        # Do not modify the function name
        # Insert your code here:
        x = kw.extract_all_words(text)
        self.assertEqual(d, kw.words_count(x))

if __name__ == '__main__':
    unittest.main()