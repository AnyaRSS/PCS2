n = int(input())
arr = map(int, input("Enter array of points: ").split())

sort = list(sorted(arr))
while sort[-1] == sort[-2]:
    del sort[-1]
del sort[-1]
result = sort.pop(-1)
print(result)

#runner-up python3