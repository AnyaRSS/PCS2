numlst =input().split()
arr_elements = input().split()
A = set(input().split())
B = set(input().split())
happiness = 0
for e in arr_elements:
    if e in A:
        happiness += 1
    elif e in B:
        happiness -= 1
print(happiness)

#no idea pypy3