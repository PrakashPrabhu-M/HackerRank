#https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    lines=size*2-1
    width=(size*2-1)+(size*2-2)
    alph='abcdefghijklmnopqrstuvwxyz'
    need_alph='-'.join(alph[:size][::-1])
    #print(need_alph+need_alph[:-1][::-1])
    for i in range(1,lines+1,2):
        print('{}'.format(need_alph[:i]+need_alph[:i-1][::-1]).center(width,'-'))
    for i in range(lines-2,-1,-2):
        print('{0:-^{1}}'.format(need_alph[:i]+need_alph[:i-1][::-1],width))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
