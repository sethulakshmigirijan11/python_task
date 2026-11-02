#find even and odd numbers
numbers=[12,7,20,9,33,44,18,5]
result= {
    "even":[],
    "odd":[]
}
for i in numbers:
    if i%2==0:
        result["even"].append(i)
    else:
        result["odd"].append(i)
print(result)

#find elements that appears exactly once
# numbers=[1,2,3,2,4,5,1,6,5,7]
# frequency={}
# for i in numbers:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency=1
# result=[]
# for i in numbers:
#     if frequency[i]==1:
#         result.append(i)
# print(result)

#reverse every word in a list
word=["python","java","developer","coding"]
result=[]
for i in word:
    result.append(i[::-1])
print(result)

#find elements present in one list but not the other
a=[10,20,30,40,50]
b=[30,40,60,70]
set_a=set(a)
set_b=set(b)
only_a=set(a)-set(b)
only_b=set(b)-set(a)
print("only a",only_a)
print("only b",only_b)

#group students according to their marks
students={
    "anu":85,
    "rahul":76,
    "meera":89,
    "arun":45,
    "john":35,
    "sara":75
}
result={
    "ecxellent":[],
    "average":[],
    "poor":[]
}
for name, marks in students.items():
    if marks>=80:
        result["ecxellent"].append(name)
    elif marks>=50:
        result["average"].append(name)
    else:
        result["poor"].append(name)
print(result)

#find the common elements
a={1,2,3,6}
b={6,8,9}
print(a.union(b))

#find the largest in a nested list
data=((1,2),(10,20),(4,5))
largest=data[0]
for i in data:
    if sum(i)>sum(largest):
        largest=i
    print(largest)


numbers=[1,2,4,5,7]
last=numbers.pop
numbers.insert(0,last)
print(numbers)

#count the number of elements in a list
numbers=[10,20,30,40,50,20]
print(numbers.count(20))

#find the cube of elements
list1=[1,2,3]
li=[]
a=[]
for i in list1:
    li=(i,i**3)
    a.append(li)
print(a)