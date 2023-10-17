# Regex Version of the strip() Method
import re

def custom_strip(input_str, chars_to_strip=None):
    if chars_to_strip is None:
        # If no chars_to_strip specified, strip whitespace from both ends
        return re.sub(r'^\s+|\s+$', '', input_str)
    else:
        # Otherwise, strip specified characters from both ends
        pattern = f'^[{re.escape(chars_to_strip)}]+|[{re.escape(chars_to_strip)}]+$'
        return re.sub(pattern, '', input_str)

# Test the function
original_str = "   Hello, World!   "
chars_to_remove = " !"

stripped_str1 = custom_strip(original_str)
stripped_str2 = custom_strip(original_str, chars_to_remove)

print("Original String:", original_str)
print("Stripped (Whitespace):", stripped_str1)
print("Stripped (Custom):", stripped_str2)

