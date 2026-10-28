#remove duplicated while preserving the order

numbers=[4,2,4,7,2,9,7,1]
new=[]
for number in numbers:
    if number not in new:
        new.append(number)
print(new)


#find secondlargest unique number

numbers=[10,5,20,20,8,15,10]
largest=numbers[0]
secondlargest=numbers[0]
for i in numbers:
    if i>largest:
     secondlargest=largest
     largest=i
    elif largest>i>secondlargest:
     secondlargest=i
      
     print(secondlargest)


#find common elements

list1=[1,2,3,4,5,6]
list2=[3,4,5,6,7,8]
for i in list1:
   if i in list2:
    print(i)

#find numbers that appear in only one list

a={1,2,3,4,5,6}
b={4,5,6,7,8}
print(a.symmetric_difference(b))

#swap values using a tuple

a=12
b=25
a,b=b,a
print(a,b)

#count the frequency of each number

numbers=[1,2,2,3,1,2,4,3,1]
frequency={}
frequency[i]=frequency.get(i,0)+1
print(frequency)

#find the student with highest mark

mark={
   "anu":70,
   "john":89,
   "meera":85,
   "rahul":90
}
top_student=max(mark,key=mark.get)
print(top_student,mark[top_student])


#find students enrolled in both courses

course={
   "python":{"anu","rahul","meera","john"},
   "java":{"rahul","john","arun"}
}
common=course["python"]&course["java"]
print(common)


#find if the word is palindrome

word="malayalam"
if word[::-1]==word:
   print("its palindrome")
else:
   print("its not a palindrome")


#find the last digit in a tuple
numbers=[1,2,3,4,5]
print(numbers[-1])