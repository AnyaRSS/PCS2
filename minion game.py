def minion_game(string):
    player1 = 0
    player2 = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    string_len = len(string)
    for letter in range(string_len):
        if string[letter] in vowels:
            player1 += string_len - letter
        else:
            player2 += string_len - letter

    if player1 > player2:
        print('Kevin', player1)
    elif player1 <player2:
        print("Stuart", player2)
    else:
        print("Draw")

s = input()
minion_game(s)

#minion game pypy3