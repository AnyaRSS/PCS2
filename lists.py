N = int(input())
result = []

for i in range(0,N):
    x = input().split()
    if x[0] == 'insert':
        result.insert(int(x[1]), int(x[2]))
    elif x[0] == 'print':
        print(result)
    elif x[0] == 'remove':
        result.remove(int(x[1]))
    elif x[0] == 'append':
        result.append(int(x[1]))
    elif x[0] == 'sort':
        result.sort()
    elif x[0] == 'pop':
        result.pop()
    elif x[0] == 'reverse':
        result.reverse()

#lists pypy3