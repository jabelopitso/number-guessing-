import unittest
from unittest.mock import patch
from number_guessing import guess_number  # Import the function to test

class TestGuessNumber(unittest.TestCase):
    
    @patch('random.randint')
    def test_correct_guess(self, mock_randint):
        # Simulate that the random number is 7
        mock_randint.return_value = 7
        result = guess_number(7)  # User guesses correctly
        self.assertEqual(result, "Correct")
    
    @patch('random.randint')
    def test_too_low_guess(self, mock_randint):
        # Simulate that the random number is 7
        mock_randint.return_value = 7
        result = guess_number(5)  # User guesses too low
        self.assertEqual(result, "Too low")
    
    @patch('random.randint')
    def test_too_high_guess(self, mock_randint):
        # Simulate that the random number is 7
        mock_randint.return_value = 7
        result = guess_number(9)  # User guesses too high
        self.assertEqual(result, "Too high")
    
if __name__ == '__main__':
    unittest.main()
