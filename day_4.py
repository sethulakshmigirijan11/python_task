#find the longest word
word=["apple","watermelon","banana","orange"]
longest=""
for i in word:
    if len(i)>len(longest):
        longest=i
print(longest)

#move negative numbers to the beggining
num=[2,5,-3,-2,7,-9,-1,6]
negative=[]
positive=[]
for i in num:
    if i<0:
        negative.append(i)
    else:
        positive.append(i)
result=negative+positive
print(result)

#find missing numbers
num=[1,3,5,6,9,10]
missing=[]
for i in range(1,11):
    if i not in num:
        missing.append(i)
print(missing)

#count occurance in a tuple
data=("a","b","a","c","b","a")
result={}
for i in data:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)

#find common elements in three sets
a={1,2,3,4,5}
b={2,3,5,6}
c={2,5,7,8}
result=a & b & c
print(result)

#check wheather a subset of a set
a={2,4}
b={1,2,3,4,5,6}
if a.issubset(b):
    print("a is a subset of b")
else:
    print("a is not a subset of b")


#find the student with least mark
students={
    "anu":70,
    "john":85,
    "rahul":65,
    "meera":54
}
lowest=float('inf')
lowest_name=""
for name,marks in students.items():
    if marks<lowest:
        lowest=marks
        students_name=name
print(students_name)
print(lowest)

#merge two dictionries and add duplicate values
dict1={"apple":10 ,"banana":20 ,"orange":15}
dict2={"banana":5 ,"orange":10 ,"grapes":25}
result=dict1.copy()
for key,value in dict2.items():
    if key in result:
        result[key]+=value
    else:
        result[key]=value
print(result)

#remve duplicates without using set
numbers=[1,2,3,2,4,1,5,3]
result=[]
for i in numbers:
    if i not in result:
        result.append(i)
print(result)

#reverse a list without using reverse() or slicing
num=[10,20,30,40,50]
result=[]
for i in range(len(num)-1,-1,-1):
    result.append(num[i])
print(result)
