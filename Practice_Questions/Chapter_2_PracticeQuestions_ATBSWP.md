📖 Page 55  
**1. What are the two values of the Boolean data type? How do you write them?**  
True and False. When entered as Python code, the Boolean values True and False lack the quotes you place around strings, and they always start with a capital T or F, with the rest of the word in lowercase.  
**2. What are the three Boolean operators?**  
And, or, and not.  
**3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what the evaluate to).**  
See Table 2-2, Table 2-3 and Table 2-4 in pages 25 and 26 respectively.  
**4. What do the following expressions evaluate to?**  
(5 > 4) and (3 == 5)&nbsp;&nbsp; <- True and False&nbsp;&nbsp; <- False  
not (5 > 4)&nbsp;&nbsp; <- not (True)&nbsp;&nbsp; <- False  
(5 < 4) or (3 == 5)&nbsp;&nbsp; <- False or False&nbsp;&nbsp; <- False  
not ((5 > 4) or (3 == 5))&nbsp;&nbsp; <- not(True or False)&nbsp;&nbsp; <- not(False)&nbsp;&nbsp; <- True  
(True and True) and (True == False)&nbsp;&nbsp; <- True and False&nbsp;&nbsp; <- False  
(not False) or (not True)&nbsp;&nbsp; <- True or False&nbsp;&nbsp; <- False  
**5. What are the six comparison operators?**  
Table 2-1 page 23.  
**6. What is the difference between the equal to operator and the assignment operator?**  
Page 24 explanation.  
**7. Explain what a condition is and where you should use one.**  
Condition is just a more specific name than expression in the context of flow control statements. Conditions should be used in various aspects of programming, from controlling flow and making decisions to handling user interactions and error cases.  
**8. Identify the three blocks in this code:**  
In the given code, there are three distinct blocks of code. Each block is defined by its indentation level. Here's how the code is divided into three blocks:

Block 1:  
```python
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')
```
Block 2:
```python
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
```
Block 3:
```python
    if spam > 5:
        print('bacon')
    else:
        print('ham')
```
Block 1 is the main block that starts with the **if** statement. Blocks 2 and 3 are nested within Block 1 due to their indentation levels. Each block is executed based on the conditions and indentation levels.  
**9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam**  
```python
spam = int(input("Enter a value for spam: "))  # Get input from the user

if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")
```
**10. What keys can you press if your program is stuck in an infinite loop?**  
Ctrl + C.  
**11. What is the difference between break and continue?**  
Like break statements, continue statements are used inside loops. When the program execution reaches a continue statement, the program execution immediately jumps back to the start of the loop and reevaluates the loop's condition while the break statement it immediately exits the while loop's clause.  
**12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?**  
In a `for` loop, `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` essentially produce the same result, which is iterating over the numbers from 0 to 9. However, they use different syntax to achieve the same outcome:

1. `range(10)`:
   This creates a range that starts from 0 (by default) and ends at 10 - 1. It steps through each number with a default step of 1. So, the numbers iterated in the loop will be 0, 1, 2, ..., 8, 9.

2. `range(0, 10)`:
   This explicitly specifies the start and end values of the range. It starts from 0 and ends at 10 - 1, similar to the previous example. Again, it steps through each number with the default step of 1.

3. `range(0, 10, 1)`:
   This is the same as the previous example but explicitly specifies the step value as 1. Since 1 is the default step value, this doesn't change the behavior of the loop. It starts from 0, ends at 10 - 1, and increments by 1 in each iteration.

In summary, all three forms of the `range` function in a `for` loop will produce the same output of iterating over the numbers from 0 to 9 with a step of 1. The difference lies in the syntax used to create the range.  
**13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.**  
```python
for i in range(1, 11):
  print(i)

number = 1
while number < 11:
  print(number)
  number += 1
```
**14. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?**  
You could do `from spam import bacon` or use the dot notation which consists of importing the module and then using the name of the module a point as a prefix and the name of the function, in this case it would result in:
```python
import spam
spam.bacon()
```
Done.