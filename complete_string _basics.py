# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:02:20 2020

@author: Karthik Shekar
"""


'''
length of a string
'''
'''
name = str(input())

x = len(name)
print(x)
print(type(name))
'''
'''
finding length of a string 2 method
'''
'''
name = str(input())

count = 0

for i in name:
    count += 1
print(count)
'''
'''
Frequency of a character in a string
'''
'''
import collections
name = str(input())

ctr = collections.Counter(name)

print(ctr)
'''
'''
adding the firdt two and the last two in the string
'''
'''
x = str(input())

if len(x) == 0:
    print('empty string')
else:
    for i in x:
        y = x[0:2] + x[-2:]

print(y)
'''
'''
Replacing the first char
'''
'''
name = str(input())

k = name[0]

name = name.replace(k , '$')

name = k + name[1:]

print(name)

'''
'''
swapping first two characters from a string
'''
'''
x = str(input())
y = str(input())

new_x = y[0:2] + x[2:]
new_y = x[0:2] + y[2:]

new_x = new_x + new_y

print(new_x)
'''
'''
add ing and ly at the end of the string
'''
'''
name = str(input())

if len(name)<3:
    print('nothing')
elif(name[-3:] == 'ing'):
    print(name+'ly')
else:
    print(name+'ing')
'''






