m = int(input())
M = set(input().split())
n = int(input())
N = set(input().split())

set1 = M.difference(N)
set2 = N.difference(M)
result_set = set1.union(set2)
l = []
for x in result_set:
    l.append(int(x))
l.sort()
for i in l: 
    print(i)

#symmetric difference pypy3