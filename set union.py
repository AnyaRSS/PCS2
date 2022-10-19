e = int(input())
Eng = set(input().split())
f = int(input())
Fre = set(input().split())

res = Eng.union(Fre)
print(len(res))

#set union pypy3