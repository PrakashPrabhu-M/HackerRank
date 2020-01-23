#https://www.hackerrank.com/challenges/collections-counter/problem

X=int(input())
shoeSizes=[int(x) for x in input().split()]
N=int(input())

import collections
shoes=collections.Counter(shoeSizes)
cost=0

for _ in range(N):
    cust_req=list(map(int,input().split()))
    if cust_req[0] in shoes.keys():
        if shoes[cust_req[0]]>0:
            shoes[cust_req[0]]-=1
            cost+=cust_req[1]

print(cost)

