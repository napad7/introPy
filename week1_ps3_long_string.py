# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 07:01:22 2018
Longest substring in alphabetical order is: beggh
@author: Primary
abcdefghijklmnopqrstuvwxyz -abcdefghijklmnopqrstuvwxyz
nknaymvnxabvdltu - dltu
rkmkzzziwb -kzzz
yjbaaebfst - bfst

The thinking
check iterative char 
or next big save in temp_big and not save in last one in current_big + last char

save current into final and compare them save them in final
there is also range not going at the end and if condition with big good


"""

s = 'cfmrcykp'
long = ''
temp_big = ''
current_big = ''
final_big = ''

for char in range(len(s) - 1):
    current_char = s[char]
    temp_big = temp_big + long
    if s[char] <= s[char + 1]:
        long = s[char]
    else:
        current_big = temp_big + s[char]
        long = ''
        temp_big = ''
    if char == (len(s) - 2) and s[char] <= s[char + 1]:
            long = temp_big + s[char] + s[char + 1]
            current_big = long
    if len(current_big) > len(final_big):
            final_big = current_big
            current_big = ''
print('Longest substring in alphabetical order is: ', final_big)
