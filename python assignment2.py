#!/usr/bin/env python
# coding: utf-8

# # TYPES OF INHERITANCE
Single inheritance:
# In[5]:


class Parent():
       def first(self):
           print('parent class')
class Child(Parent):
       def second(self):
          print('child class')
 
ob = Child()
ob.first()
ob.second()

Multiple inheritance:
# In[4]:


class Parent:
   def func1(self):
        print("this is a parent class")
class Parent2:
   def func2(self):
        print("this is another parent class")
class Child(Parent , Parent2):
    def func3(self):
        print("this is the child class")
 
ob = Child()
ob.func1()
ob.func2()
ob.func3()

Multilevel inheritance:
# In[13]:


class Parent:
      def func1(self):
          print("Parent class")
class Child(Parent):
      def func2(self):
          print("Child class")
class Child2(Child):
      def func3(self):
        print("Another child class")
ob = Child2()
ob.func1()
ob.func2()
ob.func3()


# # Exception handling

# In[19]:


try:
    100/0

except:
     print("ZeroDivisionError")


# In[22]:


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The list is:", myList)
index = 10
try:
    element = myList[index]
    print("Element at index {} is {}".format(index,element))
except:
    print("IndexError")


# In[31]:


a=10 
try:
    print(aa)
except:
    print("NameError")


# In[35]:


import math


# In[38]:


try:
    print(math.sqrt(-1))
except:
    print("ValueError")


# In[50]:


try:
    num = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    num['Forty']
except:
    print("KeyError")


# # Regex functions

# In[61]:


import re
str1 = "Hi, Im iron man in an iron suit"
x=re.findall("iron", str1)
print(x)
y=re.search('man',str1)
print(y)
z=re.compile('[a-e]')
print(z)
a=re.escape(str1)
print(a)


# # Aggregate functions

# In[62]:


import numpy as np


# In[75]:


arr1=np.array([[1,2,3],[4,5,6]])


# In[76]:


np.sum(arr1,axis=0)


# In[77]:


np.sum(arr1,axis=1)


# In[78]:


np.prod(arr1)


# In[79]:


np.min(arr1)


# In[80]:


np.argmin(arr1)


# In[82]:


np.max(arr1)


# In[83]:


np.argmax(arr1)


# In[86]:


np.std(arr1)


# In[87]:


np.var(arr1)


# In[88]:


np.any(arr1)


# In[89]:


np.all(arr1)


# In[90]:


np.mean(arr1)


# In[91]:


np.median(arr1)


# # comparisons

# In[93]:


x1 = [1,2,3]
x2 = [4, 5, 6]
if  x1 is x2:
    print("Yes")
else:
    print("No")
    
x3 = x1
if  x1 is x3:
    print("yes")
else:
    print("No")
if  x1 == x3:
    print("Yes")
else:
    print("No")


# # mask

# In[99]:


import pandas as pd
data = pd.DataFrame({
    'Part': ['Monitor', 'CPU', None, 'Mouse', None, 'Extensions', 'Table', 'Chair', 'Wifi'],
    'Feature': ['LED', 'i7', 'RGB', 'Wireless', 'Zebronics', None, 'Urban Clap', 'Apex Chairs', 'Airtel'],
    'Price': [12000, 3500, None, 1200, None, 250, 7000, 12000, 799]
})
data.mask(data.isnull(),'mask')


# # Boolean arrays 

# In[98]:


import numpy as np
arr = np.array([5, 0.001, 1, 0, 'g', None, True, False, " "], dtype=bool)
print(arr)


# In[ ]:




