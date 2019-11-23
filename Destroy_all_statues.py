#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:57:13 2019

@author: jcunanan
"""

#from extratypes import Point2D  # library with types used in the task
from sympy import Point2D

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    slopeE = []
    slopeW = []
    sN = 0
    sS = 0
    
    for i in range(N):
        
        if Point2D(A[i]).x == 0 and Point2D(A[i]).y > 0:
            sN = 1
            
        elif Point2D(A[i]).x == 0 and Point2D(A[i]).y < 0:
            sS = 1
            
        if Point2D(A[i]).x >0 :
            if Point2D(A[i]).y / Point2D(A[i]).x not in slopeE:
                slopeE.append(Point2D(A[i]).y / Point2D(A[i]).x)
                
        if Point2D(A[i]).x < 0:
            if Point2D(A[i]).y / Point2D(A[i]).x not in slopeW:
                slopeW.append(Point2D(A[i]).y / Point2D(A[i]).x)
                
    return len(slopeE)+len(slopeW)+sN+sS
    
