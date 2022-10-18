n = int(input())
integer_list = map(int, input().split())

my_tuple = tuple(integer_list)
hashed = hash(my_tuple)
print(hashed)

#tuples pypy3