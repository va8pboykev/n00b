Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = int(input("Enter your math grade: "))    
b = int(input("Enter your science grade: "))
c = int(input("Enter your english grade: "))
d = int(input("Enter your social studies grade: "))
e = int(input("Enter your computer grade: "))

total_sum = a+b+c+d+e
avg = total_sum/5
print("Your grade average is:", avg)
if avg < 60:
    print"GET YOUR GRADE UP!"
else:
    print"Good job, keep up the good work!"
