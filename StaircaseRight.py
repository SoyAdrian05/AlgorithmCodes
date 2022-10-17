# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:33:35 2022

@author: Adrian
"""

def staircase(n):
    # Write your code here
    s = ""
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end='')
        for k in range(i+1):
            print("#",end='')
        print()

        
        
        
staircase(4)