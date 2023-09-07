📖 Page 75  
**1. Why are functions advantageous to have in your programs?**  
Functions are advantageous to have in your programs for several reasons:

1. `Modularity:` Functions allow you to break down a complex program into smaller, manageable parts. Each function can perform a specific task, making the code more organized and easier to understand.

2. `Reusability:` Once you define a function, you can reuse it in different parts of your program or even in different programs. This saves time and effort by eliminating the need to rewrite the same code.

3. `Readability:` Using functions allows you to give meaningful names to different parts of your code, making it more readable and self-explanatory. This makes it easier for you and others to understand the purpose of each part.

4. `Debugging:` When an error occurs in your code, having functions makes it easier to locate the issue. You can isolate the problematic function and focus on debugging that specific part without affecting the rest of the program.

5. `Testing:` Functions can be tested individually, making it easier to identify errors and ensure that each function works correctly before integrating them into the entire program.

6. `Abstraction:` Functions allow you to abstract away the implementation details of a certain task. You can use a function without needing to know how it's implemented, making it easier to work with complex logic.

7. `Collaboration:` Functions facilitate collaboration among developers. Different team members can work on different functions simultaneously, improving productivity and efficiency.

8. `Scalability:` Functions make it easier to scale your program. You can add new features or modify existing ones by extending or modifying functions without affecting the entire codebase.

9. `Code Maintenance:` Functions make code maintenance more manageable. If a change is needed, you can update a single function rather than hunting down every occurrence of a certain piece of code.

10. `Code Reusability:` Functions can be used across multiple projects, saving time and effort when building new software.

In summary, functions improve code organization, reusability, readability, debugging, testing, collaboration, abstraction, scalability, and code maintenance, making them an essential tool for writing efficient and maintainable programs.  
**2. When does the code in a function execute: when the function is defined or when the function is called?**  
When the function is called.  
**3. What statement creates a function?**  
The `def` statement.  
**4. What is the difference between a function and a function call?**  
In simpler terms, a function is like a recipe or a blueprint that defines how a certain task should be done. It contains the code that carries out the task. A function call, on the other hand, is like following the recipe or using the blueprint to actually make the dish or build the structure. It triggers the execution of the code within the function.  
**5. How many global scopes are there in a Python program? How many local scopes?**  
In a Python program, there is one global scope and potentially multiple local scopes.  
**6. What happens to variables in a local scope when the function call returns?**  
When a function call returns in Python, the local variables within that function's local scope cease to exist. In other words, they are deleted and their values are no longer accessible. This process is known as "variable scope" or "variable lifetime."  
**7. What is a return value? Can a return value be part of an expression?**  
A return value in programming refers to the value that a function generates and sends back to the caller of the function. It's the result of the computation or processing that the function performs. When a function is executed and reaches a return statement, it evaluates the expression following the return keyword and then exits, passing the evaluated value back to the caller.

Yes, a return value can absolutely be part of an expression. This is a common practice in programming and allows you to use the value returned by a function in other operations or assignments.  
**8. If a function does not have a return statement, what is the return value of a call to that function?**  
`None`.  
**9. How can you force a variable in a function to refer to the global variable?**  
In Python, if you want to force a variable in a function to refer to the global variable instead of creating a new local variable with the same name, you can use the `global` keyword.

Here's how you can do it:

```python
global_var = 10  # This is a global variable

def modify_global():
    global global_var  # Declare the variable as global within the function
    global_var = 20    # Modify the global variable

modify_global()
print(global_var)  # This will output 20
```
In the example above, the `global` keyword is used within the function to indicate that `global_var` refers to the global variable of the same name, rather than creating a new local variable. This way, any modifications made to `global_var` within the function will affect the global variable outside the function as well.  
**10. What is the data type of `None`?**  
The data type of None is actually called NoneType. It is a unique type in Python that only has one value, which is None.  
**11. What does the `import areallyourpetsnamederic` statement do?**  
The statement `import areallyourpetsnamederic` does not have any predefined meaning in Python. It appears to be a humorous reference or a fictional module name that doesn't actually exist in Python's standard library or any commonly used external libraries.

In Python, the `import` statement is used to bring in functionality from external modules or libraries. If `areallyourpetsnamederic` is not a valid module name, attempting to import it will result in an `ImportError`.

It's possible that this statement is being used as an example or a joke rather than a functional import statement.  
**12. If you had a function named `bacon()` in a module named `spam`, how would you call it after importing `spam`?**  
`import bacon from spam` for instance.  
**13. How can you prevent a program from crashing when it gets an error?**  
Using `try` and `exclude` clauses.  
**14. What goes in the `try`clause? What goes in the `except`clause?**  
The code that could potentially have an error is put in a `try` clause. The program execution moves to the start of a following `except` clause if an error happens.