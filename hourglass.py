#https://www.hackerrank.com/challenges/2d-array/problem?h_r=next-challenge&h_v=zen

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    h=[]
    for i in range(4):
        for j in range(4):
            temp=arr[0+i][0+j]+arr[0+i][1+j]+arr[0+i][2+j]+arr[1+i][1+j]+arr[2+i][0+j]+arr[2+i][1+j]+arr[2+i][2+j]
            h.append(temp)
    return max(h)

    

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
