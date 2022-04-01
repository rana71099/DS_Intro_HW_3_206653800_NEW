# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 12:43:14 2022

@author: Pc
"""


#A
def read_line(n, file):
    if not isinstance(n, int):
        return("invalid input detected")
    try:
        f=open(file)
    except FileNotFoundError:
        return("file not found")
    else:
        lines=f.readlines()
        if( len(lines) < (n-1)):
            return("line "+ str(n) +" doesn't exist")
        return(lines[n-1])
print(read_line(4, 'ex3_text (1).txt')) 
print(read_line(9, 'ex3_text (1).txt')) 
print(read_line(29, 'ex3_text (1).txt')) 
print(read_line("c", 'ex3_text (1).txt'))
print(read_line(9, 'ex3_text (1).txt'))  