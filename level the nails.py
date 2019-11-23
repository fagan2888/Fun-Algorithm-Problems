#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:43:58 2019

@author: jcunanan
"""

# Problem description
# Given and array A where the elements are starting height of nails, and you are allowed
#to hammer (no pulling) nails down up to K times so that you achieve the 
# most number of leveled nails 
# Write an algorithm that determines the most number nails at the same level 
#after hitting at most K times
# Example. A = [1,1,2,2,2,3,4,4,4,4] and K =2 should have the solution 5.
# this is achieved by hammering any nails with height 3, 4 down to height 2

def solution (A,K):
    
    N=len(A)
    best = 0
    count = 1
    
    for j in range(1,N-K):
        if A[j] == A[j+1]:
            count += 1
            
        else:
            count = 1
            
        best = max(best, count+K)
        
    return best