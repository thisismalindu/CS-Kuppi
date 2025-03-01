# **Python Functions - Reference Guide**

## **Introduction**
This document serves as a reference for understanding and applying functions in Python. Functions help in making code **modular, reusable, and easier to manage**. This guide covers fundamental concepts, practical examples, and exercises to strengthen your understanding.

---

## **1. Recap of Basics**
### **Hello World Example**
```python
print("Hello, World!")
```

### **Variables and Data Types**
Python supports multiple data types, such as integers, floats, strings, and lists:
```python
name = "Alice"  # String
age = 20  # Integer
height = 5.6  # Float
numbers = [1, 2, 3, 4, 5]  # List
```

### **Loops & Conditionals**
```python
for i in range(5):
    print("Iteration", i)

if age > 18:
    print("Adult")
```

### **Lists**
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Access first element
```

### **Why Use Functions?**
- To **avoid code repetition**.
- To **increase readability and organization**.
- To **make debugging easier**.
- To **enable reusability**.

---

## **2. Function Basics**
### **Defining and Calling Functions**
```python
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))
```

### **Function with Multiple Parameters**
```python
def add(a, b):
    return a + b

print(add(5, 3))
```

### **Practical Exercises**
1. Write a function that prints a greeting message five times using a loop.
2. Write a function that calculates the square of a number and returns the result.
3. Write a function that finds the maximum of three given numbers.

---

## **3. Function Concepts**
### **Scope (Local vs. Global Variables)**
```python
x = 10  # Global variable

def func():
    x = 5  # Local variable
    print("Inside function:", x)

func()
print("Outside function:", x)
```

### **Default & Keyword Arguments**
```python
def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Good morning"))
```

### **Practical Exercises**
1. Write a function that removes duplicates from a list and returns the cleaned list.
2. Write a function that returns whether a number is prime or not.
3. Write a function that reads a text file and returns the longest word.

---

## **4. Hands-on Mini Projects**
### **Refactoring a Messy Program**
```python
def get_student_data():
    return [82, 90, 76, 88, 95]

def analyze_students(students):
    avg = sum(students) / len(students)
    return max(students), min(students), avg

students = get_student_data()
print(analyze_students(students))
```

### **Simple Expense Tracker**
```python
def track_expense(expenses):
    total = sum(expenses.values())
    return total

print(track_expense({"Food": 500, "Transport": 200}))
```

---

## **5. Debugging and Best Practices**
### **Common Function Mistakes**
1. Misusing `return` (e.g., forgetting it when needed or using it unnecessarily).
2. Using global variables when local ones should be used.
3. Not handling edge cases properly.

### **Writing Clean Functions**
- Use meaningful function names.
- Keep functions short and focused.
- Write docstrings:
```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
```

---

## **6. Using the Internet to Learn**
### **Helpful Resources**
- **Stack Overflow:** Search for coding solutions.
- **Reddit:** Find discussions on common problems.
- **ChatGPT:** Learn how to ask good programming questions.

---

## **7. Summary & Final Thoughts**
- Functions make code **organized, reusable, and efficient**.
- **Practice makes perfect** – try implementing more examples on your own.
- Use **online resources** to improve your problem-solving skills.

🚀 **Keep coding and keep learning!**

