# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:52:35 2020

@author: Karthik Shekar
"""
'''
sum of the list
'''
'''

lst = list(input())

for i in range(0,len(lst)):
    lst[i] = int(lst[i])
    
print(type(lst[1]))

print(sum(lst))
'''

'''
product of the list
'''
'''
lst = list(input())

result = 1

for i in range(0,len(lst)):
    lst[i] = int(lst[i])
    result *= lst[i]
    
print(result)
'''

'''
min in the list
'''
'''
lst = list(input())


for i in range(0,len(lst)):
    lst[i] = int(lst[i])

print(min(lst))
'''

'''
max in the list
'''
'''
lst = list(input())


for i in range(0,len(lst)):
    lst[i] = int(lst[i])

print(max(lst))
'''

'''
ENtering the string, comparing first and the last lew=tter
'''
'''
lst = ['abc', 'xyz', 'mam']

print(lst)
j = 0

for i in lst:
    if (len(i)>1 and i[0] == i[-1]):
        j += 1
        print(j)
'''

'''
remove duplicates from a list
'''
'''
lst = list(input())

m = []

for i in range(0,len(lst)):
    lst[i] = int(lst[i])
    
print(len(lst))
    
for i in lst:
    if i not in m:
        m.append(i)
print(m)
'''    
'''
checking if a list is empty
'''
'''
lst = list(input())

if(len(lst)==0):
    print('empty list')
else:
    print(len(lst))

'''
'''
duplicate a list
'''
'''
lst = list(input())

new_lst = []

for i in lst:
    new_lst.append(i)
    
print(new_lst)
'''    
'''
list of words no longer than ceratin number
'''
'''
lst = ['abc','xyz','mamamsdmasdm','asdcvsdfgvsd']

n = int(input('enter the length of the string you want to see'))

m = []

print(lst)

for i in lst:
    if(len(i)<=n):
        m.append(i)
print(m)
'''
'''
finds one common in two lists
'''
'''
lst = [1,2,3,4,5,6]
lst1 = [6,7,8,9]

for i in lst:
    if i in lst1:
        print(True)

'''   
'''
Removing some elements from list
''' 
'''
Lst =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']



del Lst[0]
del Lst[3]
del Lst[3]
    
print(Lst)
'''
'''
Removing Even numbers from list
'''
'''
lst = list(input())

m = []

for i in range(0,len(lst)):
    lst[i] = int(lst[i])

for i in lst:
    if i%2==0:
        m.append(i)
        
print(m)

'''
'''
shuffle items in a list
'''
'''
from random import shuffle 

lst = ['bangalore','mysore','Bellary']

shuffle(lst)

print(lst)

'''
'''
 Generate all permutations of a list in Python
'''
'''
import itertools
print(list(itertools.permutations([1,2,3])))
'''
'''
removing common elements from two lists
'''
'''
lst1 = list(input())
lst2 = list(input())
m = []
m = list(set(lst1) - set(lst2))

print(m)
'''
'''
finding an index of a particular list
'''
'''
lst = list(input())

for index,lst in enumerate(lst):
    print(index,lst)
 '''
'''
Converting list of characters into a string
''' 
'''
lst = list(input())

lst_str = ''.join(lst)

print(lst_str)
print(type(lst_str))
'''
'''
append the first list to second
'''
'''
lst = list(input())
m = list(input())
n= []

n =lst + m

print(n)
'''
'''
choosing a random value from list
''' 
''' 
import random 
lst = list(input())
print(random.choice(lst))

'''
'''
finding the second largest number
'''
'''
lst = list(input()) 

for i in range(0,len(lst)):
    lst[i] = int(lst[i])

x = []    
n = len(lst)
y = max(lst) 
lst.sort(reverse = True)

print(lst)
for y in lst:
    if y not in x:
        x.append(y)
print(x)   
    
print(x[1])

'''
'''
finding second smallest number
'''

lst = list(input()) 

for i in range(0,len(lst)):
    lst[i] = int(lst[i])

x = []    
n = len(lst)
y = max(lst) 
lst.sort()

print(lst)
for y in lst:
    if y not in x:
        x.append(y)
print(x)   
    
print(x[1])
