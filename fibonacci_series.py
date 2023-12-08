#n = int(input("Enter the number of terms: "))  # Take input for the number of terms

# Initializing the first two terms of the Fibonacci sequence
#n1, n2 = 0, 1

# Check if the number of terms is valid
#if n <= 0:
 #   print("Please enter a positive integer.")
#elif n == 1:
 #   print("Fibonacci sequence up to", n, ":")
  #  print(n1)
#else:
 ### print(n2)  # Print the second term

    # Loop to generate the Fibonacci sequence
    #for i in range(2, n-1):
     #   n3 = n1 + n2
      #  print(n3)  # Print the next term in the sequence
       # n1, n2 = n2, n3  # Update the values for the next iteration

#n = int(input("Enter the limit for the numbers: "))
#number = 0

#while number <= n:
 ##  number += 1




# for sum of random inputs eg -- 10 20 30 40 50

'''import math



n= int(input("n:"))
import math

def pi(n):
    print(f"{math.pi:.{n}f}")

# Example usage:
  # Replace with the number of decimal places you want
pi(n)'''

'''n= int(input("n: "))
m= int(input("m: "))
for i in range (n,m):
    if i == 1:
        continue
    if i%5==0:
        print(i)'''
#  returnig is vowel or not vowel or wrong input 
'''vowels = "aeiouAEIOU"
n = input("vowel, or -1 to quit: ")

while True:
    if n in vowels:
        print("vowel")
        n = input("vowel, or -1 to quit: ")
    elif n == "-1":
        break
    elif not n.isalpha():
        print("wrong input")
        n = input("vowel, or -1 to quit: ")
    elif n not in vowels:
        print("not vowel")
        n = input("vowel, or -1 to quit: ")
'''

# finding   prime numbers btw two user given numbers
"""x= int(input("x: "))
y= int(input("y: "))
for i in range(x,y):
   if i>1:
     continue
   prime =True
   for j in range(2, i):
        if i % j == 0:
            prime = False
            break
        
              print(i)"""

"""x = int(input("x: "))
y = int(input("y: "))
for i in range(x, y + 1):
    if i > 1:
        prime = True
        for j in range(2, i):
            if (i % j) == 0:
                prime = False
                break
        if prime:
            print(i)"""



# printing armstrong number

"""n= (input("n: "))
a=len(n)
s=0
print("len:",a)
b=[]
for i in n:
    b.append(int(i))
print(b)
for j in b:
    s+=j**a
print(s)
if (s)==n:
    print("armstrong number")
else:
    print("not an armstrong number")"""

# printing for given  is vowel or consonant or not alphapet

"""vowel="aeiouAEIOU"
ch=(input("ch: "))
if not ch.isalpha():
    print("not an alphabet")
else:
    for i in vowel:
        if i==ch:
            print("vowel")
            break
    else:
        print("consonant")"""




# finding strong number  -- it is a number  whose digit factorial sum is equal to its number

"""number = int(input("Enter a number: "))
temp = number
strong_sum = 0

while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact *= i
    strong_sum += fact
    temp //= 10

if strong_sum == number:
    print(" is a strong number")
else:
    print(" is not a strong number")
"""
# to make the floyd triangle also known as right angle triangle


"""rows= int(input("enter the number of rows: "))
num=1
for i in range (1,rows+1):
    for j in range (1,i+1):
        print(num, end=" ")
        num+=1
    print()"""




"""n=5
l=[]

for i in range(n):
    l1=[]
    for j in range(i+1):
        if j==0 or j==i:
            l1.append(1)22
        else:
            l1.append(l[i-1][j-1]+l[i-1][j])
    l.append(l1)
    print(l1)
print(l)"""

#printing good morning or night to user

"""name=(input("name: "))
message=(input("morning/night: "))
n= "Morning"
def greet(name,message):
    if message==n:
        print("Good Morning",name)
    else:
        print("Good night",message)
greet(name,message)"""

"""def squares(x):
    l1=[]
    for i in range(len(x)):
        
        z=x[i]**2
        l1.append(z)
    return l1

    print(l1)

list1= list(map(int,input().split(",")))
print(list(squares( list1)))"""




# built in functions

"""a="python"
print(a.upper())
print(a.capitalize())"""


# printing a string  in center preceeded and suceeded by a symbol
"""a= "python"
print(a.center(20,'*'))"""


# joining strings  using a symbol btw them if items are in a list 

"""b='.'
l1=["www","codetantra","com"]
print(b.join(l1))"""

 
"""b= "python is good language"
c="-"
d=b.replace("good","tuple")#replaces a word and changes to given one
print(b.split()) #returns string as list 
print(b.center(25,"%"))# adds sign 
print(c.join(b)) 
print(d)
print(type(d))

e="python3455"
print(e.isalnum())

a=" "
print(a.isspace())
x="Hello Python"
print(x.istitle())"""

"""data= input("data: ")
l = data.split(',')
print(f"list: {l}")
z=type(l)
print(f"Type of l :{z}")"""
 
# to find how many days a person lived since his or her birthday  using datetime module
"""from datetime import datetime
def lived():
   
    birth_date_str= (input("enter the dob in format yy-mm-dd: "))

    birth_date= datetime.strptime(birth_date_str, '%Y%m%d')
    current_date=datetime.now()
    days_lived=(current_date - birth_date).days
    print(days_lived)
    return days_lived


lived()"""


# finding number of days lived without using date time module




"""def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False

def lived(dd, mm, yy, dd1, mm1, yy1):
    month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0

    while not (dd == dd1 and mm == mm1 and yy == yy1):
        if is_leap_year(yy):
            month_days[2] = 29
        else:
            month_days[2] = 28

        total_days += 1
        dd += 1

        if dd > month_days[mm]:
            dd = 1
            mm += 1

            if mm > 12:
                mm = 1
                yy += 1

    return total_days


dob = input("Enter the date of birth in ddmmyyyy format: ")
dd = int(dob[:2])
mm = int(dob[2:4])
yy = int(dob[4:])

todaysdate = input("Enter today's date in ddmmyyyy format: ")
dd1 = int(todaysdate[:2])
mm1 = int(todaysdate[2:4])
yy1 = int(todaysdate[4:])

print("Days since birthday:", lived(dd, mm, yy, dd1, mm1, yy1))
"""


# calculating if given is valley or not     //// valley means after strictly decreasing  number there should be strictly increasing numbers

"""def valley(l):
    if (len(x) < 3):
        return False   
    low_count = 1  ; up_count = 1
    for i in range(0, len(x) - 1):
        if x[i] > x[i + 1]:
            if low_count > 1:
                return False
            up_count = up_count + 1
        if l[i] < l[i + 1]:
            low_count = low_count + 1
        if x[i] == x[i + 1]:
            return False
    if up_count > 1 and low_count > 1:
        return True
    else:
        return False
x=input("enter the numbers with spacing: ")

valley(l)
"""




"""l1=[0,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=[0,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

str1= input("enter the word: ")
ik1=(str1.split(' '))
print(ik1)"""




"""# Get user input for a comma-separated list
user_input = input("Enter a list of values separated by commas: ")

# Convert the user input to a list
user_list = user_input.split(',')

# Get user input for the index
target_index = int(input("Enter the index you want to retrieve: "))

# Check if the index is valid
if -len(user_list) <= target_index < len(user_list):
    # Print the value at the specified index
    print(f"Value at index {target_index}: {user_list[target_index]}")
elif target_index == len(user_list):
    print("Invalid: Index is equal to the length of the list.")
else:
    print("Invalid index")
"""

"""d1=input('data1: ')
d2=input('data2: ')
a1=d1.split(',')
a2=d2.split(',')
a1 = [i.strip() for i in a1]
if len(a1)!=len(a2):
    print('lists are different')
elif len(a1)==len(a2):
    dicti=dict(zip(a1,a2))
    print(dicti)"""

"""import Robots.MathRobot
print('Select an operator:')
print('1. Addiion')
print('2. Subtract')
print('3. Multiply')
choice=input('choice(1/2/3): ')
if choice=='1':
    Robots.MathRobot.add_numbers()
elif choice=='2':
    Robots.MathRobot.subtract_numbers()
elif choice=='3':
    Robots.MathRobot.multiply_numbers()
else:
    print('Invalid choice')
print('goodbye')"""



n = (input())
arr = map(int, input().split())
    
print(arr)