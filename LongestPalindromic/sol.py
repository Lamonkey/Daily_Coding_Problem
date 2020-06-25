import unittest
def bruteForece(input):
    length = len(input)
    length_max = 0
    for i in range(0,length):
        for k in range(i + 1,length+1):
            length_temp = isPalindromic(input[i:k])
            length_max = max(length_temp,length_max)
    return length_max

#return the legnt of a palindromic string, 0 if not palindromic
def isPalindromic(input):
    i = -1
    for char in input:
        if char != input[i]:
            return 0
        i = i - 1
    return len(input)
    

import unittest

class TestStringMethods(unittest.TestCase):
    input1 = "ab"
    input2 = "abc"
    input3 = "aba"
    input4 = "abba"
    input5 = "a"
    input6 = "abcdefedc"
    input7 = "abcbdefedbab"

    def test_brute_force(self):
        input1 = "ab"
        input2 = "abc"
        input3 = "aba"
        input4 = "abba"
        input5 = "a"
        input6 = "abcdefedc"
        input7 = "abcbdefedbab"
        self.assertEqual(bruteForece(input1),1)
        self.assertEqual(bruteForece(input2),1)
        self.assertEqual(bruteForece(input3),3)
        self.assertEqual(bruteForece(input4),4)
        self.assertEqual(bruteForece(input5),1)
        self.assertEqual(bruteForece(input6),7)
        self.assertEqual(bruteForece(input7),7)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()




