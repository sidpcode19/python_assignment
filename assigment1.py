'''1. Write a Python program to print the following string in a specific format (see the
output). Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above
the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what
you are".'''

print("Twinkle,Twinkle, little star.")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")
print("Twinkle,Twinkle, little star.")
print("How I wonder what you are!")



'''2. Write a Python program that accepts the user's first and last name and prints them in
reverse order with a space between them.'''

fName = input("Enter first name:")
lName = input("Enter last name: ")
print(lName,fName)



'''3. Write a Python program that calculates the area of a circle based on the radius entered
by the user.'''

r = int(input("Enter the radius : "))
Area = 3.14*r*r
print(Area)



'''4. Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]'''

color_list = ["Red","Green","White","Black"]
print(color_list[0])
print(color_list[3])



'''5. Write a Python program that accepts an integer (n) and computes the value of
n+nn+nnn.
Sample value of n is 5'''

n = int(input("Enter the number: "))
ones = n
tens = n*10 + ones
hundreds = n*100 + tens
add = ones + tens + hundreds
print(add)



'''6. Write a Python program that accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple of those numbers. Sample data : 3, 5, 7, 23'''

x = str(input("Enter the number: ")).split(",")
print(x)
x = tuple(x)
print(x)



# 7. Write a program that will convert celsius value to Fahrenheit.

celsius = float(input("Enetr temperature: "))
fahrenheit = 1.8*celsius + 32
print(fahrenheit)




'''8. User will input (2numbers). Write a program to swap the numbers. Add incrementally
in any one variable.'''

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
temp = first
first = second
second = temp

print(first,second)




# 9. Write a program that will tell whether the number entered by the user is odd or even.

n = int(input("Enter the number: "))
if (n%2 == 0) : print("even number.")
else : print("odd number.")



# 10. Write a program that will tell whether the given year is a leap year or not.

year = int(input("Enter the year"))

if (year % 400 == 0) and (year % 100 == 0):
    print("is a leap year")
elif (year % 4 ==0) and (year % 100 != 0):
    print("is a leap year")
else:
    print("is not a leap year")


# 11. Write a program to find the euclidean distance between two coordinates.


x1,y1 = int(input("x1:")), int(input("y1:"))
x2,y2 = int(input("x2:")), int(input("y2:"))
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(distance)



'''12. Write a program that take a user input of three angles and will find out whether it can
form a triangle or not.'''

a1, a2, a3 = float(input("a1:")),float(input("a2:")),float(input("a3:"))
sum = a1 + a2 + a3
if (sum == 180) : print("This is a triangle.")
else : print("This is not a triangle.")



# 13. WAP to find compound interest for given values.

p ,r ,t,n  = int(input("principle: ")), int(input("rate: ")), int(input("time: ")), int(input(number of time))
CI = p*((1+(r/n))**(t*n))
print(CI)



'''14. Given a positive integer N, the task is to write a Python program to check if the number
is Prime or not in Python.'''

N = int(input("Enter the number : "))
c = 0
for i in range (2,N):
if(N % i == 0) :
c = c + 1
if c > 0:
print("Not Prime")
else:
print("Prime")


# 15. Given a positive integer N. The task is to find 12 + 22 + 32 + ….. + N2.

n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1) :
sum = sum + i**2
print(sum)
