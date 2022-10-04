a=7
print(type(a))

b=3.56
print(type(b))

z=complex(2,-3)
print(z)
print(type(z))
print(z.conjugate())

days_list=['Mondayt','Tuesday',1,2,3,4,5,6]
maxList = [7,'dog',[1,2,3,4],'abs']
print(days_list)
print(maxList)
print(maxList[2][1])

num_list=[10,20,30,40]
print(num_list[2:len(num_list)])

num_list[0] = 9
num_list[2:1]=[11,30] 
for n in num_list:
    print(n)

maxListHybrid = [7,'dog',[1,2,'3',4],'abs']
print(maxListHybrid)
print(maxListHybrid+num_list)
print(num_list*2)
maxListHybrid.append('abs2')
print(maxListHybrid)

fruit_tuple = ('Apple','Banana','Orange')
print(fruit_tuple)
print(fruit_tuple[0:2])

person_dictionary = {'age':10,'name':'Heart Break Kid'}
print(person_dictionary['age'])
person_dictionary['age']=20
print(person_dictionary['age'])
print(person_dictionary.keys())
print(person_dictionary.values())

print(2>1)

a={1,2,3}
print(a)
a.remove(1)
a.add(6)
print(a)
print(2+1)
print(2-1)
print(2*1)
print((2/1))
print(4//3)
print(5%3)
print(-5)
print(+5)
print(abs(-5))
print(divmod(5,6))
print(pow(2,8))
print(2**8)
print(1/-2)
print(1//-2)
print(0**0)

