import collections
n = int(input())
words = []
for i in range(n):
    words.append(input())
dic = collections.Counter(words)
print(len(dic))
print(*dic.values())

#word order  python3