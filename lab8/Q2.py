# Write a Python program that matches a string that has an “a” followed by zero or more “b”’s.
import re
def text_match(text):
    patterns = '^a(b*)$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'
print(text_match("abbbb"))