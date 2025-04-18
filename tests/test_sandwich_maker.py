import unittest
from sandwich_maker import make_sandwich

class TestSandwichMaker(unittest.TestCase):
    
    def test_make_sandwich(self):
        # Test with default values
        self.assertEqual(make_sandwich('wheat', 'ham'), 'Sandwich with wheat bread, ham filling.')
        
        # Test with toast
        self.assertEqual(make_sandwich('white', 'turkey', toasted=True), 'Toasted sandwich with white bread, turkey filling.')
        
        # Test with cheese and toast
        self.assertEqual(make_sandwich('rye', 'bacon', cheese='swiss', toasted=True), 'Toasted sandwich with rye bread, bacon filling, and swiss cheese.')
        
        # Test without cheese but with toast
        self.assertEqual(make_sandwich('whole wheat', 'peanut butter', toasted=False), 'Sandwich with whole wheat bread, peanut butter filling, no cheese.')

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
