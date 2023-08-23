import re

def is_valid(number):
    # Define=ing the regular expression pattern for valid contact numbers
    pattern = r'^(\+\d{1,2}\s?)?(\(\d{1,4}\)|\d{1,4})[\s.-]?\d{3,4}[\s.-]?\d{4}$'
    
    # Using the re.match function to check if the number matches the pattern
    if re.match(pattern, number):
        return True
    else:
        return False

# Test cases
test_numbers = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890",
    "12345",  
    "abc123",  
]

for number in test_numbers:
    if is_valid(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")
