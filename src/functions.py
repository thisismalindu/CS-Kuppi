print('Hello')

name = 'Alice'
name = 10

age = 5

if age > 10:
    print('You are too old')
elif age < 10:
    print('You are too young')
else:
    print('You are just right')
    
for i in range(10):
    print(i)
age = 5
    
while age < 10:
    print('You are still young')
    age += 1
    
mylist = [1, 2, 3, 4, 5]
for i in mylist:
    print(i)
    
def greet(name):
    print(f'Hello {name}!')

greet('Alice')

def add(a, b):
    return a + b

sum = add(1, 2)
print(sum)

def sqr(a):
    return a * a

print(sqr(5))

def max(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    return c
    
    
print(max(1, 2, 3))


a = 10
def myFunc():
    global a
    a  = a ** 5
    print(a)    
myFunc()
print(a)

a = 10

def myFunc(n,p):   
    n = n**p
    return  n

a = myFunc(a,5)
print(a)

def greet1(name, msg):
    return f"{msg}, {name}!"

def greet2(name, msg="Hello"):
    return f"{msg}, {name}!"

greet2('John')

def printNumbersUpto10(i):
    if i > 10:
        return
    print(i)
    i += 1
    printNumbersUpto10(i)
    
printNumbersUpto10(1)

i = 1
while i <= 10:
    print(i)
    i += 1
    
listWithDuplicates = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def removeDuplicates(listWithDuplicates):
    for i in listWithDuplicates:
        if listWithDuplicates.count(i) > 1:
            listWithDuplicates.remove(i)
    return listWithDuplicates

print(removeDuplicates(listWithDuplicates))


def isPrime(n):
    """Returns True if n is prime, False otherwise"""

    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generatePrimes(n):
    primes = []
    for i in range(2, n):
        if isPrime(i):
            primes.append(i)
    return primes

print(generatePrimes(100))


# def get_student_data():
#     return [82, 90, 76, 88, 95]

# def analyze_students(students):
#     avg = sum(students) / len(students)
#     return max(students), min(students), avg

# students = get_student_data()
# print(analyze_students(students))

print('printing specific stuff')

# create a function to find if palindrome
def isPalindrome(s):
    return s == s[::-1] 