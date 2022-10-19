from itertools import combinations
n = int(input())
l = list(input().split())
k = int(input())
comb = combinations(l,k)
count = 0
for element in comb:
    if 'a' in element:
        count += 1
ratio = count/len(list(combinations(l,k)))
print(ratio)

#iterables and iterators pypy3