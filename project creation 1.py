class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

class manager(employee):
     def __init__(self,name,salary,department):
         self.department=department
         super().__init__(name,salary)
     def display(self):
         print(self.name,self.salary,self.department)

s1=manager("siva",65000,"AI")
s1.display()

salary=int(input("salary:"))
age=int(input("age:"))
if(salary>=20000 or age<=25):
    loan=int(input("loan amount"))
    if(loan<=50000):
        print("yor are eligible")
    else:
        print("maximum loan amount is 50000")
else:
    print("yor are not eligible")
    try:
    a=int(input())
    b=int(input())
    c=input()
    print(a+b)

except ValueError as e:
    print("ValueError",e)

except TypeError as e:
    print("typeError",e)

except NameError as e:
    print("NameError",e)

finally:
    print("done")



