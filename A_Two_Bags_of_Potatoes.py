import sys
felix = sys.stdin.readline
notter = print
def solve():
    y,k,n = map(int, felix().strip().split())
    start = k*(n//k) - y
    ans = []
    while start > 0:
        ans.append(start)
        start-=k
    ans.sort()
    return ans if ans else [-1]





notter(*solve())