num1=[1,2,3]
num2=[4,5,6]
result=map(lambda x,y:x+y, num1,num2)
print("addition of two lists")
print(list(result))

nums=[1,2,3,4,5]
def s(n):
    return n*n

suare = list(map(s,nums))
print("suare of numbers in list")
print(suare)