def add(a,b):
    return a+b
def sub(a,b):
     return a-b
def multi(a,b):
     return a*b
def division(a,b):
     return a%b

print(__name__)    
if __name__=='__main__':
    n1=int(input())
    n2=int(input())
    print("add:",add(n1,n2))
    print("sub:",sub(n1,n2))
    print("multi:",multi(n1,n2))
    print("division:",division(n1,n2))
def square(a):
    return a**2

a=(1,2,3,4,5)
result=map(lambda a:a**2,a )
print(list(result))

a=[]
for i in range(1,6):
    num=int(input())
    a.append(square(num))
print(a)

l=(1,2,3,4,5)
print(tuple(map(lambda l:l**2,l)))

a=(1,2,3)
b=(2,1,1)
result=map(lambda l,m:l+m,a,b)
print(list(result))




