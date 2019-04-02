import OneStringReturn
import DataReturn
import unittest


'''
b. Write a test which verifies the example case below:
Example Case
Input:
[‘g’, ‘gh’, ‘ghj’, ‘g’], [‘j’, ‘ju’, ‘gh’, ‘gk’, ‘gn’]
Output:
Strings appearing in multiple lists: ‘gh’
Number of unique strings: 7
Total number of strings processed: 9
'''

class TestThingReturns(unittest.TestCase):
    processedStrings = 0
    uniqueStrings = 0
    StringsInMoreThanOne = []
    temp = []
    
    #Complicated way, multiple tests, does not work.

    def setUp(self): #mental note, camel case is important...
        temp = DataReturn.StringAnalyzer([['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']])
        self.processedStrings = temp[2]
        self.uniqueStrings = temp[1]
        self.StringsInMoreThanOne = temp[0]
        
    def test_processedStrings(self):
        self.assertEqual(self.processedStrings, 9)
    
    def test_uniqueStrings(self):
        self.assertEqual(self.uniqueStrings, 7)

    def test_StringsInMoreThanOne(self):
        self.assertEqual(self.StringsInMoreThanOne, ['gh'])

    #OneStringReturn
    #Literally matches the returnString, making it tempermental.
    def test_allStrings(self):#This compares with one output string that's been pre-crafting, but feels janky as it ignores the 3 subprocesses of the function.
        self.assertEqual(OneStringReturn.StringAnalyzer([['g', 'gh', 'ghj', 'g'], ['j', 'ju', 'gh', 'gk', 'gn']]),
        'Strings that appear in more than one list: "gh"\nTotal number of unique strings across all lists: 7\nTotal number of strings that were processed: 9')
    
if __name__ == '__main__':
    unittest.main()
 