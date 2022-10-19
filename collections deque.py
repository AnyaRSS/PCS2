from collections import deque
n = int(input())
d = deque()
for i in range(n):
    operation, *number = input().split()
    if number:
        integer = number[0]
    if operation == "append":
        d.append(int(integer))
    elif operation == "pop":
        d.pop()
    elif operation == "popleft":
        d.popleft()
    elif operation == "appendleft":
        d.appendleft(int(integer))
print(*d)

#collections deque python3