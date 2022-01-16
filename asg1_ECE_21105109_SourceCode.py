#QUESTION 1
print("Question 1\n")
numb1=int(input("Enter first number: "))
numb2=int(input("Enter second number: "))
numb3=int(input("Enter third number: "))
avg=(numb1+numb2+numb3)/3
print("Average of three numbers = ",avg)

#QUESTION 2
print("\nQuestion 2\n")
tax_rate=0.2
standard_deduction=10000
dependent_deduction=3000
gross_income=int(input("gross income: "))
no_of_dependents=int(input("no of dependents: "))
taxable_income=gross_income-standard_deduction-(dependent_deduction*no_of_dependents)
tax=taxable_income*tax_rate
print("Taxable Income: ",taxable_income)
print("Tax: ",tax)
#QUESTION 3
print("\nQuestion 3\n")
print("Student:[SID, Name, Gender, Course Name, CGPA]")
student=[21105109, 'Siddarth Dixit', 'M', 'ECE', 9.9]
print("Student : ",student)

#QUESTION 4
print("\nQuestion 4\n")
Marks=[23,43,44,34,39]
print("list of marks before sort: ",Marks)
Marks.sort()
print("list of marks after sort",Marks)

#QUESTION 5
print("\nQuestion 5\n")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color.pop(3)
print("(a) after removing: ",color)
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color[3:5]=['Purple']
print("(b) after replacing: ",color)