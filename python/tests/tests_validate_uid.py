import unittest, os, sys

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

from src.challenges.validate_uid import validate_string

class TestValidateString(unittest.TestCase):
    def test_validate_string(self):
        self.assertEqual(validate_string('AB12CD34EF'), ('Valid', []))  # Valid UID
        self.assertEqual(validate_string('AB12CD34EFG'), ('Invalid', ['Length is 10']))  # More than 10 characters
        self.assertEqual(validate_string('AB12CD34E'), ('Invalid', ['Length is 10']))  # Less than 10 characters
        self.assertEqual(validate_string('AB12CD34E!'), ('Invalid', ['Only alphanumeric characters']))  # Contains non-alphanumeric character
        self.assertEqual(validate_string('AB12CD34EE'), ('Invalid', ['No repeated characters']))  # Contains repeated character
        self.assertEqual(validate_string('AB12CD34eF'), ('Valid', []))  # Valid with mixed case
        self.assertEqual(validate_string('AB1CHDIjEf'), ('Invalid', ['At least two digits']))  # Only one digit
        self.assertEqual(validate_string('ABcdefghij'), ('Invalid', ['At least two digits']))  # No digits
        self.assertEqual(validate_string('1234567890'), ('Invalid', ['At least two uppercase letters']))  # No uppercase letters
        self.assertEqual(validate_string('ABCDEFGHIJ'), ('Invalid', ['At least two digits']))  # No digits
        self.assertEqual(validate_string('abcdefghij'), ('Invalid', ['At least two uppercase letters', 'At least two digits']))  # No uppercase letters and no digits
        self.assertEqual(validate_string(''), ('Invalid', ['At least two uppercase letters', 'At least two digits', 'Only alphanumeric characters', 'Length is 10']))  # No uppercase letters and no digits

        
    

if __name__ == '__main__':
    unittest.main()