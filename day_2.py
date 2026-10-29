#28/10/26
#move all zeros to the end

numbers=[0,5,0,3,8,0,2,7]
num=[]
for i in numbers:
    if i!=0:
        num.append(i)
for x in numbers:
    if x==0:
        num.append(x)
print(num)
    


#find duplicate elements
numbers=[2,5,3,2,8,5,9,3,3]
unique=set()
duplicate=set()
for num in numbers:
     if num in unique:
        duplicate.add(num)
     else:
        unique.add(num)
print(duplicate)
   

#rotate a list to right
num=[10,20,30,40,50]
print(num[::-1])

#find common element in three list
a=[1,2,3,4,5,6]
b=[2,4,6,8,10]
c=[2,4,6,12]
result=set(a) & set(b) & set(c)
print(result)


#print list in descenting and ascending order
numbers=[3,1,4,2]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

#merge 2 dictionaries and add a common value
stock1={"apple":10,"banana":15,"grapes":5}
stock2={"apple":5,"banana":10,"grapes":5}
result={}
result=stock1.copy()

for item,quantity in stock2.items():
    if item in result:
        result[item]+=quantity
    else:
        result[item]=quantity
print(result)
   

#group words by their first letter
words=["apple","ant","bat","ball","cat","dog"]
result={}
for i in words:
    first=i[0]
    if first not in result:
        result[first]=[]
        result[first].append(i)
print(result)

#find the largest word in a sentence
word="hai my name is sethulakshmi"
longest=""
new=word.split()
for i in new:
    if len(i)>len(longest):
        longest=i
print(longest)

#find sum of numbers in a tuple
numbers=(3,7,5,8)
sum=0
for i in numbers:
    sum+=i
print(sum)

 #find the product of numbers
numbers=[2,4,6,8]
result=[]
for i in range(len(numbers)):
    product=1
    for j in range(len(numbers)):
        if j != i:
            product*=numbers[j]
    result.append(product)
    print(product)  