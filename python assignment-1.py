#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 11th problem
i=0
j=0
n=int(input("enter the value of n:"))
for i in range(n):
    print("*",end="")
    j=i
    for j in range(i):
        print("*",end="")
    print("\n")


# In[ ]:


#12th problem
import re

str1 = str(input("enter a string:"))

print ("The input string is : ")
print(str1)

op = re.sub('[\W_]+', '', str1)

print ("The cleared string is :")
print(op)


# In[ ]:


# 13th problem
listt = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   listt.append(elm)
print("the elements divible by 5 are:")
for i in listt:
    if i%5==0:
        print(i)


# In[ ]:


# 14th problem
str1 = str(input("enter a string:"))
n=int(str1.count('hi'))
print("the string \"hi\" has appeared "+format(n)+" times")


# In[1]:


#15th problem
i=1
j=1
n=int(input("enter the value of n:"))
for i in range(n+1):
    for j in range(i):
        print(i,end='')
    print("")


# In[8]:


#LIST EXERCISES


# In[ ]:


#problem 1
listt = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   listt.append(elm)
first=int(input("enter the element that you want in the first place of the list:"))
last=int(input("enter the element that you want in the first place of the list:"))
listt[0]=first
listt[-1]=last
print(listt)


# In[5]:


#problem 2
listt = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   listt.append(elm)
a=int(input("enter the index position of one element"))
b=int(input("enter the index position of the other element"))
listt[a], listt[b] = listt[b], listt[a]
print("the new list is:",listt)


# In[20]:


#problem 3:
list1=[1,2,35,'oui','meow',9,0]
n=0
print("length of the list=",len(list1))
for i in list1:
    n=n+1
print("the length of the list is",n)


# In[22]:


#problem 4
listt = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   listt.append(elm)
print("the maximum element in the list is:",max(listt))


# In[24]:


#problem 5
listt = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   listt.append(elm)
print("the minimum element in the list is:",min(listt))


# In[25]:


#TUPLES EXERCISES


# In[ ]:


#problem 1
tuplee = []
n = int(input("Enter number of elements in the tuple : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = (input())
   tuplee.append(elm)
tuple1=tuple(tuplee)
print("size of the tuple is:", tuple1.__sizeof__(),"bytes")
print("the length of the tuple is:",len(tuple1))


# In[ ]:


#problem 2
tuplee = []
n = int(input("Enter number of elements in the tuple : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   tuplee.append(elm)
tuple1=tuple(tuplee)
print("the max element is:",max(tuple1))
print("the min element is:",min(tuple1))


# In[1]:


#problem 3
tuplee = []
sum=0
n = int(input("Enter number of elements in the tuple : "))
for i in range(0, n):
   print("Enter the "+format(i+1)+"th element:")
   elm = int(input())
   tuplee.append(elm)
tuple1=tuple(tuplee)
for i in tuple1:
    sum=sum+i
print("the sum is:", sum)


# In[2]:


#STRING EXERCISES


# In[ ]:


#problem 1

str2=str1[::-1]

if str1==str2:
    print("the entered string is a palindrome")
else:
    print("the entered string is not a palindrome")


# In[ ]:


#problem 2
str1=str(input("enter a string:"))
print("the reversed string is:",str1[::-1])


# In[ ]:


#problem 3
str1=str(input("enter a string:"))
i=int(input("enter the position of the element you want to remove:"))
str2 = str1[:i-1] +  str1[i:] 
print ("String after removal of character: " + str2) 


# In[ ]:


#SET EXERCISES


# In[6]:


#problem 1
sett = {"a", "b", 1,("a",2,3)}
print("the size of the set is",sett.__sizeof__(),"bytes")
print("the length of the set is", len(sett))


# In[8]:


#problem 2
sett = {"a", "b", 1,("a",2,3)}
for i in sett:
    print(i)


# In[9]:


#DICTIONARY EXERCISES


# In[17]:


#problem 1
#by key
from collections import OrderedDict
 
dict1 = {'a': '1', 'A': '10',
        'b': '65', 'C': '32', 'CD': '63'}
dict2 = (sorted(dict1.items()))
dict3= (sorted(dict1, key=dict1.get))
print("sorted by value:",dict3)
print("sorted by key:",dict2)


# In[21]:


#problem 2
a, b, c = 11, 5, 2
dict1 = {}
dict1[a, b, c] = a + b * c

a, b, c = 5, 16, 4
dict1[a, b, c] = a - b//c

print("The dictionary is :")
print(dict1)


# In[23]:


#FUNCTION EXERCISES


# In[40]:


#problem 1
def mul(a, b):
    return a*b
import inspect as ip 
print(ip.signature(mul)) 


# In[41]:


#problem 2
def mul(n1, n2=25):
    print(n1*n2)
a=(mul(2))
b=(mul(2,5))
print(a)
print(b)


# In[42]:


#MATRIX EXERCISES


# In[43]:


#problem 1
listt = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
print("The original list : " + str(listt))
out = dict(zip(listt[0], listt[1:]))
print("The Assigned Matrix : " + str(out))


# In[47]:


#problem 2
import numpy as ab
A = ab.array([[1, 2], [3, 4]])
B = ab.array([[4, 5], [6, 7]])
  
print("Printing elements of first matrix")
print(A)
print("Printing elements of second matrix")
print(B)
print("Addition of two matrices")
print(ab.add(A,B))
print("Subtraction of two matrices")
print(ab.subtract(A, B))

