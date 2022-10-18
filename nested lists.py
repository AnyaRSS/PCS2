records = []
score_list = []
name_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    
    records.append([name, score])
    score_list.append(score)
    score_list.sort()
while score_list[0] == score_list[1]:
    del score_list[0]
second_low = score_list[1]
for name, score in records:
    if score == score_list[1]:
        name_list.append(name)
name_list.sort()
for element in name_list:
    print(element)

#nested lists pypy3