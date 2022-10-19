def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    string = ''.join(string_list)
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

#mutations python3