# 0x01. Python - if/else, loops, functions <br />

## Resources <br />

[More Control Flows - python.org](https://docs.python.org/3.4/tutorial/controlflow.html) <br />
[Python Indentation Myths, LA Django, Sandy Strong](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://files.meetup.com/1544869/Python%20Indentation%20Myths.pdf) <br />
[Python IndentationError, Atom](https://www.youtube.com/watch?v=1QXOd2ZQs-Q) <br />
[How to Use String Formatters in Python](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3) <br />
[Learn to program with Python, Derek Banas](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt) <br />
[PEP 8 Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/) <br />
[Holberton intranet, 0x00 Resources](https://intranet.hbtn.io/projects/231) <br />

## Learning Objectives <br />

At the end of this project, you are expected to be able to explain to anyone, without the help of Google: <br />

## General <br />
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- Why indentation is so important in Python
- How to use the if, if ... else statements
- How to use comments
- How to affect values to variables
- How to use the while and for loops
- How is Python’s for different from C‘s?
- How to use the break and continues statements
- How to use else clauses on loops
- What does the pass statement do, and when to use it
- How to use range
- What is a function and how do you use functions
- What does return a function that does not use any return statement
- Scope of variables
- What’s a traceback
- What are the arithmetic operators and how to use them

## Tasks <br />

0. 0-positive_or_negative.py // This program will assigns a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random. randint do. Please do not touch this code
- The output of the program should be:
-- The number, followed by
--- if the number is greater than 0: is positive
--- if the number is 0: is zero
--- if the number is less than 0: is negative
-- followed by a new line

1. 1-last_digit.py // This program will assigns a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
- The variable number will store a different value every time you will run this program
- You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
- The output of the program should be:
-- The string Last digit of, followed by
-- the number, followed by
-- the string is, followed by
--- if the number is greater than 5: the string and is greater than 5
--- if the number is 0: the string and is 0
-- if the number is less than 6 and not 0: the string and is less than 6 and not 0
-- followed by a new line

2. 2-print_alphabet.py // a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

3. 3-print_alphabt.py // a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

- Print all the letters except q and e
- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store characters in a variable
- You are not allowed to import any module

4. 4-print_hexa.py // a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

- You can only use one print function with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

5. 5-print_comb2.py // a program that prints numbers from 0 to 99.

- Numbers must be separated by ,, followed by a space
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

6. 6-print_comb3.py //  a program that prints all possible different combinations of two digits.

- Numbers must be separated by ,, followed by a space
- The two digits must be different
- 01 and 10 are considered the same combination of the two digits 0 and 1
- Print only the smallest combination of two digits
- Numbers should be printed in ascending order, with two digits
- The last number should be followed by a new line
- You can only use no more than 3 print functions with string format
- You can only use no more than 2 loops in your code
- You are not allowed to store numbers or strings in a variable
- You are not allowed to import any module

7. 7-islower.py // a function that checks for lowercase character.

- Prototype: def islower(c):
- Returns True if c is lowercase
- Returns False otherwise
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()
You don’t need to understand __import__

8. 8-uppercase.py // a function that prints a string in uppercase followed by a new line.

- Prototype: def uppercase(str):
- You can only use no more than 2 print functions with string format
- You can only use one loop in your code
- You are not allowed to import any module
- You are not allowed to use str.upper() and str.isupper()
- Tips: ord()
You don’t need to understand __import__

9. 9-print_last_digit.py // a function that prints the last digit of a number.

- Prototype: def print_last_digit(number):
- Returns the value of the last digit
- You are not allowed to import any module
You don’t need to understand __import__

10. 10-add.py // a function that adds two integers and returns the result.

- Prototype: def add(a, b):
- Returns the value of a + b
- You are not allowed to import any module
- You don’t need to understand __import__

11. 11-pow.py // a function that computes a to the power of b and return the value.

- Prototype: def pow(a, b):
- Returns the value of a ^ b
- You are not allowed to import any module
You don’t need to understand __import__

12. 12-fizzbuzz.py // a function that prints the numbers from 1 to 100 separated by a space.

- For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
- For numbers which are multiples of both three and five print FizzBuzz.
- Prototype: def fizzbuzz():
- Each element should be followed by a space
- You are not allowed to import any module
You don’t need to understand __import__

13. 13-insert_number.c, lists.h // Technical interview preparation:

- You are not allowed to google anything
- Whiteboard first
Write a function in C that inserts a number into a sorted singly linked list.

- Prototype: listint_t *insert_node(listint_t **head, int number);
- Return: the address of the new node, or NULL if it failed