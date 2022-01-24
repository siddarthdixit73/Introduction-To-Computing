#Question 1
print("\nQuestion 1 :\n")
string = "Python is a case sensitive language"
print("(a) The length of the string is :", len(string))
reverse_str = string[ : : -1 ]
print("(b) The string in reverse would be :", reverse_str)
new_str = string[10:26]
print("(c) The new string becomes :", new_str)
string2 = string.replace("a case sensitive", "object oriented")
print("(d) The replaced substring will be :", string2)
indx = string.find("a")
print("(e) 'a' occurs at index no. =", indx)
string3=string.replace(" ","")
print("(f) The string with no white spaces will be", string3)

#Question 2
print("\nQuestion 2 :\n")
name = input("Enter your name : ")
sid = int(input("Enter your SID : "))
department = input("Enter the name of your department : ")
cgpa=float(input("Enter your CGPA : "))
print("\nHey, %s Here!\nMy SID is %d\nI am from %s department and my CGPA is %0.1f\n" % (name, sid, department, cgpa))

#Question 3
print("\nQuestion 3 :\n")
a=56
b=10
print("a. a & b = %d" % (a & b))
print("b. a | b = %d" % (a | b))
print("c. a ^ b = %d" % (a ^ b))
print("d. Left shift both a and b with 2 bits : a = %d, b = %d" % (a << 2,b << 2))
print("e. Right shift a with 2 bits and b with 4 bits : a = %d, b = %d\n" % (a >> 2,b >> 4))

#Question 4
print("\n Question 4 :\n")
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))
if num1 >= num2:
    if num1 >= num3:
        print("The largest number is", num1)
    else:
        print("The largest number is", num3)
else:
    if num2 >= num3:
        print("The largest number is", num2)
    else:
        print("The largest number is", num3)

#Question 5
print("\nQuestion 5 :\n")
string = input("Enter the string : ")
if "name" in  string:
    print("Yes\n")
else:
    print("No\n")

#Question 6
print("\nQuestion 6 :\n")
side1 = int(input("Enter the value of first side : "))
side2 = int(input("Enter the value of second side : "))
side3 = int(input("Enter the value of third side : "))
if side1 + side2 <= side3 or side2 + side3 <= side1 or side3 + side1 <= side2:
    print("No")
else:
    print("Yes")