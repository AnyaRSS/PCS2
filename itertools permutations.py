from itertools import permutations
S, k = input().split()
k = int(k)
l = sorted(list(permutations(S, k)))
for element in l:
    print("".join(element))


#itertools permutations pypy3