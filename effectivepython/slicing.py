# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:40:41 2017

@author: zahid
"""

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
#  visualization of the list above 
#  and the positive and negative indices
#
#  +---+---+---+---+---+---+---+---+
#  | a | b | c | d | e | f | g | h |
#  +---+---+---+---+---+---+---+---+
#  0   1   2   3   4   5   6   7   8
#  -8  -7  -6  -5  -4  -3  -2  -1  

# alist[start:end]
# start: inclusive index, starting with 0
# exclusive index

# think of the indices as pointing between characters
# start = 0, end 4 (get items at index 0, 1, 2, 3)
print (a[:4])
# ['a', 'b', 'c', 'd']

# start from the reverse position and then everything after that
# start = -4, end everything after that
print(a[-4:])
# ['e', 'f', 'g', 'h']
print(a[-1:])
# ['h']

# all three are equivalent
print(a[:])
print(a[0:])
print(a[-0:])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# why is this empty?
print(a[2:2])
print(a[0:0])

# remember it's returning values between the two indices
# there is nothing between the two indices

print(a[3:-3])
# [d', 'e']

print(a[-5:-2])
# ['d', 'e', 'f']

# why are these empty?
print(a[-3:3])
# []
print(a[-3:-5])
# []

# nothing between starting at -3 and ending at 3
# nothing between starting at -3 and ending at -5
# look at the visualization to confirm

print(a[5:len(a)])
# ['f', 'g', 'h']
print(a[5:])
# ['f', 'g', 'h']
assert a[5:len(a)] == a[5:]
# No Error
print( a[5:len(a)] == a[5:])
# True

# why it's helpful
# give me everything
print(a[:])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# everything up to the 5th item
print(a[:5])
# ['a', 'b', 'c', 'd', 'e']
 
# everything but the last item
print(a[:-1])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# everything after the 4th index
print(a[4:])
# ['e', 'f', 'g', 'h']

# everything after three back from the end or 3rd to last
print(a[-3:])
# ['f', 'g', 'h']

# everything between 2nd to 5th index
print(a[2:5])
# ['c', 'd', 'e']


# everyting from the 2nd to everything but the last index
print(a[1:-1])
# ['b', 'c', 'd', 'e', 'f', 'g']

# everything from fourth-to-last to first-to-last
print(a[-4:-1])
# ['e', 'f', 'g']

# slicing deals properly for indices beyond the list
# everything up to the 20th element
print(a[:20])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# get the last 20th elements
print(a[-20:])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# don't confuse with this which tries to retrieve the 20th element
# print(a[20])
# list index out of range

# stride
# get every other item
print(a[::2])
# ['a', 'c', 'e', 'g']

print(a[1::2])
# ['b', 'd', 'f', 'h']

# reverse all the elements
print(a[::-1])
['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
# Note: If <start> is omitted and the step is negative then it starts at the end of the string.
# when start is ommited, it starts from the end and works backwards
# when the start is supplied, it starts there and then works backwards

# SURPRISE! SURPRISE!
print(a[2::-2])
# ['c', 'a']

# so what's going on?
# when stride is negative, it works backward
# a[2::-1] would produce ['c', 'b', 'a']
#  start at the 3rd element and work backwards all the way to the start
#  a stride of -2 says to take every 2nd element; that would be 'c', 'a'
print(a[1::-2])
# ['b']
# because stride is negative, it first produces the list ['b', 'a']
# then it takes every other element; in this case only one: ['b']


print(a[:2:-2])
# ['h', 'f', 'd']
# because start was not specified and stride is negative:
# create a list from the end to the 2nd element ['h', 'g', 'f', 'e', 'd']
# then take every other element ['h', 'f', 'd']

print(a[-2::-2])
# ['g', 'e', 'c', 'a']
print(a[-2:2:-2])
# ['g', 'e']
# start at 'g' and all the way to 'd' (end is not inclusive)
