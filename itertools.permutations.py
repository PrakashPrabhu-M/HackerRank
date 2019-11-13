#https://www.hackerrank.com/rest/contests/master/challenges/itertools-permutations/download_pdf?language=English
from itertools import permutations
inp,n=input().split()
n=int(n)
inp=list(inp)
inp.sort()
for i in permutations(inp,n):
    for j in i:
        print(j,end='')
    print()
    
'''
from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')
'''
