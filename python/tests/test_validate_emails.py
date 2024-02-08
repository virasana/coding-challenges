import sys, os, unittest

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(project_root)

import src.challenges.validate_emails as validate_emails

class TestEmails(unittest.TestCase):
    def test_filter_mail(self):
        # Test case 1: Empty list of emails
        emails = []
        expected = []
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 2: List of valid emails
        emails = ['3', 'lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com']
        expected = ['lara@hackerrank.com', 'brian-23@hackerrank.com', 'britts_54@hackerrank.com']
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 3: List of invalid emails
        emails = ['test@example', 'user@gmail', 'hello@world']
        expected = []
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 4: List of mixed valid and invalid emails
        emails = ['test@example.com', 'user@gmail', 'hello@world.com']
        expected = ['test@example.com', 'hello@world.com']
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 5: List with duplicate emails
        emails = ['test@example.com', 'test@example.com', 'user@gmail.com']
        expected = ['test@example.com', 'test@example.com', 'user@gmail.com']
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 6: List of emails with a mixture of upper case and lower case
        emails = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM']
        expected = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM']
        actual = validate_emails.filter_mail(emails)
        assert actual == expected

        # Test case 7: Email with 255 characters
        email_255 = 'a' * 64 + '@' + 'b' * 186 + '.com'
        emails = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM', email_255]
        # expected does not contain email_255
        expected = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM'] 
        actual = validate_emails.filter_mail(emails)
        self.assertEqual(actual, expected)

        # Test case 8: Email with 254 characters
        email_254 = 'a' * 64 + '@' + 'b' * 185 + '.com'
        emails = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM', email_254]
        # expected contains email_254
        expected = ['Test@Example.com', 'USER@gmail.com', 'Hello@World.COM', email_254]
        actual = validate_emails.filter_mail(emails)
        self.assertEqual(actual, expected)