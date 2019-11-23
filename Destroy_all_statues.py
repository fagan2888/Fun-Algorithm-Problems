#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 17:57:13 2019

@author: jcunanan
"""
#######################################
#      Problem  Description
#Bob the Adventurer is one step away from solving the mystery of an ancient Mayan tomb. 
#He just approched the secret chamber where the secret Mayan scriptures are locked in a chest.
#There are N ancient statues in the room. 
#After long thought, Bob figured out that in order to open the treasure chest 
#he needs to stand in the middle of the room and hit every statue with a laser ray at the same time.
#Bob is a highly experienced adventurer, so setting multiple laser rays at the same time is not a problem for him. 
#Moreover, every ray that he creates is perfectly straight and never changes direction at all.

#The middle of the room, where Bob is standing, has coordinates (0, 0). 
#Every statue is located at some point with coordinates (x, y). 
#Each statue is made of pure glass, so that if any ray hits it, it does not stop, 
#but goes through the statue and continues beyond in the same, unchanged direction.
#Bob wonders how he can hit every ancient statue in the room using the fewest rays possible.

#Assume that the following declarations are given:

#class Point2D { public int x; public int y; }

#Write a function

#class Solution { public int solution(Point2D[] A); }

#that, given an array of points A, representing the locations of the statues, 
#returns the minimal number of rays that Bob must set in order to hit every statue in the room.

#For example, given an array A

#A[0].x = -1 A[0].y = -2 (statue 0) A[1].x = 1 A[1].y = 2 (statue 1) A[2].x = 2 A[2].y = 4 (statue 2) A[3].x = -3 A[3].y = 2 (statue 3) A[4].x = 2 A[4].y = -2 (statue 4)
#your function should return 4.

 #https://i.stack.imgur.com/ad5gc.png

#As is shown in the image, it is possible to create four rays in such a way that:

#the first will hit statue 0;
#the second will hit statues 1 and 2;
#the third will hit statue 3;
#the fourth will hit statue 4.
#Assume that:

#N is an integer within the range [1..100,000];
#the coordinates of each point in array A are integers within the range [−1,000,000,000..1,000,000,000];
#the elements of A are all distinct;
#Array A does not contain point (0,0).
#Complexity:

#expected worst-case time complexity is O(N);
#expected worst-case space complexity is O(N*log(N)), beyond input storage (not counting the storage required for input arguments).


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
    
