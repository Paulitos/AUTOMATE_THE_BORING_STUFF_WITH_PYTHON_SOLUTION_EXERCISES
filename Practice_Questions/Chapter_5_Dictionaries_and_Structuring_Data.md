📖 Page 126  
**1. What does the code for an empty dictionary look like?**  
{}  
**2. what does a dictionary value with a key 'foo' and a value '42' look like?**  
{'foo' : '42'}  
**3. What is the main difference between a dictionary and a list?**  
That a dictionary is unordered and a list is ordered.  
**4. What happens if you try to access `spam['foo']` if `spam` is `{'bar' : 100}`?**  
`KeyError` message.  
**5. If a dictionary is stored in `spam`, what is the difference between the expressions 'cat' in `spam` and 'cat' in `spam.keys()`?**  
Both `'cat' in spam` and `'cat' in spam.keys()` check whether the string `'cat'` is a key in the dictionary stored in the variable `spam`. However, there is a subtle difference:

1. `'cat' in spam`: This expression checks if `'cat'` is a key in the dictionary `spam`. If `'cat'` is a key in the dictionary, it returns `True`; otherwise, it returns `False`. This is a direct check for the existence of a key in the dictionary.

2. `'cat' in spam.keys()`: This expression first extracts all the keys from the dictionary `spam` using the `keys()` method, which returns a list-like view of the dictionary's keys. Then, it checks if `'cat'` is in that list of keys. If `'cat'` is in the list of keys, it returns `True`; otherwise, it returns `False`. This approach involves creating an intermediate list of keys and then performing the check.

In most cases, the first approach `'cat' in spam` is preferred because it directly checks for the presence of a key in the dictionary without the need to create an intermediate list of keys. It is more efficient for large dictionaries. The `in` operator, when used with a dictionary, checks for the existence of keys by directly accessing the dictionary's internal data structure, which is optimized for key lookups.  
**7. What is a shortcut for the following code?**  
```python
# Original code
if 'color' not in spam:
  spam['color'] = 'black'

# Corrected code
spam.setdefault('color', 'black')
```
**8. What module and function can be used to "pretty print" dictionary values?**  
The module is `pprint` and the function is either `pprint()` or `pformat()` depending if your dictionary contains nested lists or dictionaries or rather you want to obtain a prettified text as a *string value* instead of playing it on the screen.  