#https://www.hackerrank.com/rest/contests/master/challenges/itertools-product/download_pdf?language=English
from itertools import product
A=map(int,input().split()),map(int,input().split())
for i in list(product(*A)):
    print(i,end=' ')

'''
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a, b))

https://docs.python.org/3/reference/expressions.html?highlight=list#expression-lists
'''
