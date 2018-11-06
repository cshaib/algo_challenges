#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    sum_ = 0
    
    for i in range(len(q)):
        #checks if numbers in the line are not in spots further than 2 away
        if (q[i]-(i+1) > 2):
            print("Too chaotic")
            return 
        #all positive steps will be total number of moves
        for j in range(max(0, q[i] - 2),i):
            if (q[j] > q[i]):
                sum_+=1  
    print(sum_)
    
        

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)