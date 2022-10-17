# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 17:33:35 2022

@author: Adrian
"""


def staircase(n):
    # Write your code here
    stair = ""
    level = 0
    while level != n:
        stair += "#"
        print(stair)
        level +=1
        
staircase(4)