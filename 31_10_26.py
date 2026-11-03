#find common elements without using set
a=[1,2,3,4,5,6]
b=[4,5,6,7,8,9]
result=[]
for i in a:
    if i in b and i not in result:
        result.append(i)
print(result)

#find the common elements from a set
a={10,20,30,40,50}
b={30,40,50,60,70}
result=a & b
print(result)

#find the missing numbers
num=[1,2,3,5,6,8,9,10]
for i in range(1,11):
    if i not in num:
     print(i)

#rotate the from last by two positions
num=[1,2,3,4,5,6]
for i in range(2):
   last=num.pop()
   num.insert(0,last)
print(num)

#find all elements fron a set
a={10,20,30,40,50}
b={30,40,50,60,70}
result=a.union(b)
print(result)

#find the largest and smallest from a tuple
number=(10,16,28,67,33)
largest=number[0]
smallest=number[0]
for i in number:
   if i>largest:
      largest=i
      if i<smallest:
         smallest=i
print("largest:",largest)
print("smallest:",smallest)

#remove duplicate elements from a tuple
numbers=[1,2,3,2,4,1,5,3]
result=[]
for i in numbers:
   if i not in result:
      result.append(i)
result=tuple(result)
print(result)

#find elements that appers only once
numbers=[1,2,3,2,4,1,5,6,5,7]
result=[]
for i in numbers:
   if numbers.count(i)==1:
      result.append(i)
print(tuple(result))

#find the unique elements from a set
a={1,2,3,4,5,6}
b={4,5,6,7,8,9}
result=a^b
print(result)

#find disjoint without using disjoint()
a={1,2,3,4}
b={5,6,7,8}
if len(a&b)==0:
   print("sets are disjoint")
else:
   print("sets are not disjoint")