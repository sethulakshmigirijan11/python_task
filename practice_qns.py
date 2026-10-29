# #remove duplicated while preserving the order

# numbers=[4,2,4,7,2,9,7,1]
# new=[]
# for number in numbers:
#     if number not in new:
#         new.append(number)
# print(new)


# #find secondlargest unique number

# numbers=[10,5,20,20,8,15,10]
# largest=numbers[0]
# secondlargest=numbers[0]
# for i in numbers:
#     if i>largest:
#      secondlargest=largest
#      largest=i
#     elif largest>i>secondlargest:
#      secondlargest=i
      
#      print(secondlargest)


# #find common elements

# list1=[1,2,3,4,5,6]
# list2=[3,4,5,6,7,8]
# for i in list1:
#    if i in list2:
#     print(i)

# #find numbers that appear in only one list

# a={1,2,3,4,5,6}
# b={4,5,6,7,8}
# print(a.symmetric_difference(b))

# #swap values using a tuple

# a=12
# b=25
# a,b=b,a
# print(a,b)

# #count the frequency of each number

# numbers=[1,2,2,3,1,2,4,3,1]
# frequency={}
# for i in numbers:
#  frequency[i]=frequency.get(i,0)+1
# print(frequency)

# #find the student with highest mark

# mark={
#    "anu":70,
#    "john":89,
#    "meera":85,
#    "rahul":90
# }
# top_student=max(mark,key=mark.get)
# print(top_student,mark[top_student])


# #find students enrolled in both courses

# course={
#    "python":{"anu","rahul","meera","john"},
#    "java":{"rahul","john","arun"}
# }
# common=course["python"]&course["java"]
# print(common)


# #find if the word is palindrome

# word="malayalam"
# if word[::-1]==word:
#    print("its palindrome")
# else:
#    print("its not a palindrome")


# #find the last digit in a tuple
# numbers=[1,2,3,4,5]
# print(numbers[-1])

#28/oct/26
#move all zeros to the end

numbers=[0,5,0,3,8,0,2,7]
i=0
for num in numbers:
   if num!=0:
       numbers[i]=num
       i += 1
while i <len(numbers):
    numbers[i]=0
    i += 1
print(numbers)


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

    