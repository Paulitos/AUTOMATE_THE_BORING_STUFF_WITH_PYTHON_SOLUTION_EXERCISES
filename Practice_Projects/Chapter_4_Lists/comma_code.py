# Comma code Page 107 Chapter 4
def list_to_string(input_list):
    if len(input_list) == 0:
        return ""
    elif len(input_list) == 1:
        return input_list[0]
    else:
        last_item = input_list[-1]
        other_items = ", ".join(input_list[:-1])
        return f"{other_items}, and {last_item}"

# Test cases
spam = ['apples', 'bananas', 'tofu', 'cats']
result = list_to_string(spam)
print(result)  # Output: 'apples, bananas, tofu, and cats'

empty_list = []
result = list_to_string(empty_list)
print(result)  # Output: ''

