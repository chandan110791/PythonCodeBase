x=2

if x==1:
    print ("A")
elif x==2:
    print("B")
elif x==3:
    print("Ok")

prices = [12,10,12]
taxes = [5,6,7]

for i in range(0,len(prices),2):
    print(prices[i]+taxes[i])

i= 1
while i < 6:
    print(i)
    if i%3==0:
        break
    i=i+1

def addition(n):
    return n*n

res = map(addition,[1,2,3])
print(list(res))

from functools import reduce

def redFunction(x1,x2):
    return x1+x2

print(reduce(redFunction,[1,2,3,4,5,6,7,8,9]))

print(list(filter(lambda x:x%2==0,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])))

def newFunction(first,*values):
    for val in values:
        first=first+val
    return first

print(newFunction(1))
print(newFunction(1,2,-1,2,))