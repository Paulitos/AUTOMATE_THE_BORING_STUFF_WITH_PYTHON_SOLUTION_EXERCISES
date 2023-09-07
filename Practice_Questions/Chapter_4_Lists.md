📖 Page 106  
**1. What is []**  
A list.  
**2. How would you assign the value 'hello' as the third value in a list stored in a variable spam? (Assume spam contains [2, 4, 6, 8, 10].)**  
`spam[2] = 'hello'`  

For the following three questions, let's say `spam` contains the list ['a', 'b', 'c', 'd'].  
**3. What does spam[int('3' * 2) // 11)] evaluate to?**  
Here, int('3' * 2) is equivalent to int('33'), which converts the string '33' into an integer, resulting in the value 33. Then, 33 // 11 performs integer division, resulting in 3. So, spam[3] will evaluate to 'd' because it's the element at index 3 in the list.  
**4. What does spam[-1] evaluate to?**  
spam[-1] accesses the last element of the list, which is 'd'.  
**5. What does spam[:2] evaluate to?**  
spam[:2] is a slice of the list that includes all elements from the beginning (index 0) up to, but not including, index 2. So, it evaluates to ['a', 'b'].  

For the following three questions, let's say `bacon` contains the list [3.14, 'cat', 11, 'cat', True].  
**6. What does `bacon.index('cat')` evaluate to?**  
bacon.index('cat') returns the index of the first occurrence of the string 'cat' in the list. In this case, it evaluates to 1 because the first occurrence of 'cat' is at index 1 (lists use zero-based indexing).  
**7. What does `bacon.append(99)` make the list value in `bacon` look like?**  
After bacon.append(99), the list bacon will look like this: [3.14, 'cat', 11, 'cat', True, 99]. It appends the integer 99 to the end of the list.  
**8. What does `bacon.remove('cat')` make the list value in `bacon` look like?**
bacon.remove('cat') removes the first occurrence of the string 'cat' from the list. After this operation, the list bacon will look like this: [3.14, 11, 'cat', True, 99]. The first occurrence of 'cat' has been removed from the list.  
**9. What are the operators for list concatenation and list replication?**  
The `+` operator combines two lists to create a new list value and the `*` operator can be used with a list and an integer value to replicate the list.  
**10. What is the difference between `append()` and `insert()` list methods?**  
The `append()` method call adds the argument to the end of the list. The `insert()` method can insert a value at any index in the list.  
**11. What are two ways to remove values from a list?**  
The `del` statement and the `remove()` method.  
**12. Name a few ways that list values are similar to string values.**  
List values and string values in Python have some similarities:

1. **Sequential Data:** Both lists and strings are sequential data types. They store a sequence of elements where each element has a specific position (index) within the sequence.

2. **Indexing:** You can access individual elements within a list or a string using indexing. Lists and strings both support positive indexing (starting from 0) and negative indexing (starting from -1, which represents the last element).

3. **Slicing:** Both lists and strings support slicing operations. You can extract a portion of the sequence by specifying a range of indices.

4. **Iteration:** You can iterate over the elements of a list and the characters of a string using loops like `for` or `while`. This allows you to process each element or character one at a time.

5. **Concatenation:** Lists and strings can be concatenated to create longer sequences. For strings, concatenation means combining two strings into a new one. For lists, concatenation means extending one list with the elements of another.

6. **Length:** You can find the length (number of elements or characters) of a list or a string using the `len()` function.

7. **Membership Testing:** Both lists and strings support membership testing using the `in` and `not in` operators. You can check if a specific element or character exists within the sequence.

Despite these similarities, it's important to note that lists and strings are distinct data types with their own unique methods and behaviors. Strings are immutable (cannot be changed after creation), while lists are mutable (can be modified). Lists can store elements of different data types, while strings store characters. These differences make them suitable for different types of tasks.  
**13. What is the difference between lists and tuples?**  
Among other differences, one is mutable and the other is inmutable. Lists syntax are typed with `[]` and tuples with `()`.  
**14. How do you type the tuple value that has just the integer value `42` in it?**  
To create a tuple with just the integer value `42`, you can enclose `42` in parentheses `( )`. Here's how you type it:

```python
my_tuple = (42,)
```

The comma after `42` is necessary to indicate that you're creating a tuple with one element. Without the comma, Python would interpret `(42)` as an integer in parentheses, not as a tuple. Adding the comma makes it clear that you're defining a single-element tuple containing the integer `42`.  
**15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?**  
You can convert a list to a tuple using the `tuple()` constructor, and you can convert a tuple to a list using the `list()` constructor in Python.

1. Converting a list to a tuple:

```python
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
```

In this example, `my_list` is converted to a tuple, and `my_tuple` will contain the elements as a tuple.

2. Converting a tuple to a list:

```python
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
```

Here, `my_tuple` is converted to a list, and `my_list` will contain the elements as a list.

These conversions allow you to switch between the two data structures when needed, depending on your programming requirements.  
**16. Variables that "contain" list values don't actually contain lists directly. What do they contain instead?**  
In Python, variables that "contain" list values do not actually store the list itself directly. Instead, they store a reference or pointer to the list in memory. This means that when you assign a list to a variable, you're storing the memory address where the list is located in the computer's memory.

Here's a simple way to understand it:

1. You create a list: `my_list = [1, 2, 3, 4, 5]`
2. The variable `my_list` doesn't store the actual list elements directly. Instead, it stores a reference to the memory location where the list `[1, 2, 3, 4, 5]` is stored.
3. If you assign the same list to another variable, both variables will reference the same list in memory:

```python
my_list = [1, 2, 3, 4, 5]
another_list = my_list  # Now both variables point to the same list
```

This behavior has some implications when working with mutable objects like lists. If you modify the list through one variable, the changes will be reflected in the other variable because they both point to the same list in memory.  
**17. What is the difference between `copy.copy()` and `copy.deepcopy()`?**  
`copy.copy()` can be used to make a duplicate copy of a mutable value like a list or a dictionary, not just a copy of reference. The `deepcopy()` function will copy these inner lists as well.  