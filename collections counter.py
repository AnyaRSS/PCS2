from collections import Counter

number_of_shoes = int(input())
shoe_size = list(map(int, input().split()))
number_of_costumers = int(input())
c = Counter(shoe_size)
income = 0

for el in range(number_of_costumers):
    size, price = map(int, input().split())
    if c[size]:
        income += price
        c[size] -=1
        
print(income)

#collections counter pypy3