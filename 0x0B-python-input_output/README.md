# 0x0B. Python - Input/Output <br />

## Resources <br />

[7.2. Reading and Writing Files](https://docs.python.org/3.4/tutorial/inputoutput.html#reading-and-writing-files) <br />
[8.7. Predefined Clean-up Actions](https://docs.python.org/3.4/tutorial/errors.html#predefined-clean-up-actions) <br />
[Dive Into Python 3: Chapter 11. Files ](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/http://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf) <br />
[JSON encoder and decoder](https://docs.python.org/3.4/library/json.html) <br />
[Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU) <br />
[Automate the Boring Stuff With Python](https://automatetheboringstuff.com) <br />

## Learning Objectives <br />

At the end of this project, you are expected to be able to explain to anyone, without the help of Google: <br />

## General <br />
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
## Python Scripts <br />

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc

## Python Test Cases <br />

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: python3 -m doctest ./tests/*
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Tasks <br />

0. 0-read_file.py // This function reads a text file (UTF8) and prints it to stdout:

- Prototype: def read_file(filename=""):
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

1. 1-number_of_lines.py // This function returns the number of lines of a text file:

- Prototype: def number_of_lines(filename=""):
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

2. 2-read_lines.py // a function that reads n lines of a text file (UTF8) and prints it to stdout:

- Prototype: def read_lines(filename="", nb_lines=0):
- Read the entire file if nb_lines is lower or equal to 0 OR greater or equal to the total number of lines of the file
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

3. 3-write_file.py // a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: def write_file(filename="", text=""):
- You must use the with statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

4. 4-append_write.py // a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: def append_write(filename="", text=""):
- If the file doesn’t exist, it should be created
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

5. 5-to_json_string.py // a function that returns the JSON representation of an object (string):

- Prototype: def to_json_string(my_obj):
- You don’t need to manage exceptions if the object can’t be serialized.

6. 6-from_json_string.py // a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.

7. 7-save_to_json_file.py // a function that writes an Object to a text file, using a JSON representation:

- Prototype: def save_to_json_file(my_obj, filename):
- You must use the with statement
- You don’t need to manage exceptions if the object can’t be serialized.
- You don’t need to manage file permission exceptions.

8. 8-load_from_json_file.py // a function that creates an Object from a “JSON file”:

- Prototype: def load_from_json_file(filename):
- You must use the with statement
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
- You don’t need to manage file permissions / exceptions.

9. 9-add_item.py // a script that adds all arguments to a Python list, and then save them to a file:

- You must use your function save_to_json_file from 7-save_to_json_file.py
- You must use your function load_from_json_file from 8-load_from_json_file.py
- The list must be saved as a JSON representation in a file named add_item.json
- If the file doesn’t exist, it should be created
You don’t need to manage file permissions / exceptions.

10. 10-class_to_json.py //  a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

- Prototype: def class_to_json(obj):
- obj is an instance of a Class
- All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
- You are not allowed to import any module

11. 11-student.py // a class Student that defines a student by:

- Public instance attributes:
-- first_name
-- last_name
-- age
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py)
- You are not allowed to import any module

12. 12-student.py //  a class Student that defines a student by: (based on 11-student.py)

- Public instance attributes:
-- first_name
-- last_name
-- age
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
- If attrs is a list of strings, only attributes name contain in this list must be retrieved.
Otherwise, all attributes must be retrieved
You are not allowed to import any module

13. a class Student that defines a student by: (based on 12-student.py)

- Public instance attributes:
-- first_name
-- last_name
-- age
- Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
- Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 10-class_to_json.py):
- If attrs is a list of strings, only attributes name contain in this list must be retrieved.
- Otherwise, all attributes must be retrieved
- Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
- You can assume json will always be a dictionary
- A dictionary key will be the public attribute name
- A dictionary value will be the value of the public attribute
- You are not allowed to import any module
- Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

14. 14-pascal_triangle.py // *Technical interview preparation*:

- You are not allowed to google anything
- Whiteboard first
- Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

- Returns an empty list if n <= 0
- You can assume n will be always an integer