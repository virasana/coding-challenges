import re

def fun(s):
    pattern = "^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{1,3}$"
    result = bool(re.search(pattern, s)) and len(s) <= 254
    return result

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = 3
    emails = [
        "lara@hackerrank.com", 
        "brian-23@hackerrank.com", 
        "britts_54@hackerrank.com"
    ]

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)