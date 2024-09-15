import math

'''1. Write a Python program to calculate the difference between a given number and 17
with the help of function. If the number is greater than 17, return twice the absolute
difference.'''
def difference(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return abs(n - 17)

'''2. Write a Python program for a function. to test whether a number is within 100 to 1000
or 2000.'''
def test_number(n):
    return 100 <= n <= 1000 or n == 2000

# 3. Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]

'''4. Write a Python function that accepts a string and counts the number of upper and lower
case letters.'''
def count_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

'''5. Write a Python function that takes a list and returns a new list with distinct elements
from the first list.'''
def distinct_elements(lst):
    return list(set(lst))

'''6. Write a Python program to print the even numbers from a given list. Sample List : [1,
2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]'''
def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

# 7. Write a Python program to access a function inside a function.
def outer_function():
    def inner_function():
        return "Inner function accessed"
    return inner_function()

'''8. Define a Python function student(). Using function attributes display the names of all
arguments.'''
def student(name, age):
    pass

student.name = "name"
student.age = "age"

'''9. Write a Python class named Student with two attributes: student_id, student_name. Add
a new attribute: student_class. Create a function to display all attributes and their values
in the Student class.'''
class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  # Added attribute

    def display(self):
        return vars(self)

'''10. Write a Python class named Student with two instances student1, student2 and assign
values to the instances' attributes. Print all the attributes of the student1, student2
instances with their values in the given format.'''
class StudentInstances:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

'''11. Write a Python class named Circle constructed from a radius and two methods that will
compute the area and the perimeter of a circle.'''
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

'''12. Write a Python class that has two methods: get_String and print_String , get_String
accept a string from the user and print_String prints the string in upper case.'''
class StringHandler:
    def __init__(self):
        self.string = ""

    def get_String(self):
        self.string = input("Enter a string: ")

    def print_String(self):
        print(self.string.upper())

# Example usage
print(difference(22))  # 1
print(test_number(150))  # 2
print(reverse_string("hello"))  # 3
print(count_letters("Hello World"))  # 4
print(distinct_elements([1, 2, 2, 3, 4, 4]))  # 5
print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # 6
print(outer_function())  # 7
print(student.__dict__)  # 8

student = Student(1, "John")  # 9
student.student_class = "10th Grade"
print(student.display())

student1 = StudentInstances(1, "John")  # 10
student2 = StudentInstances(2, "Jane")
print(vars(student1))
print(vars(student2))

circle = Circle(5)  # 11
print(circle.area())
print(circle.perimeter())

handler = StringHandler()  # 12
# handler.get_String()  # Uncomment for input
# handler.print_String()  # Uncomment for output

