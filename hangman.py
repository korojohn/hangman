import random

with open('words.txt', 'r', encoding='utf8') as f:
    word = random.choice(f.readlines()).rstrip()

tries = 6
letters = []

def hide():
    hidden = ''
    for letter in word:
        if letter in letters:
            hidden += letter
        else:
            hidden += '-'
    return hidden

while tries > 0:
    hidden_word = hide()
    if hidden_word == word:
        print('Συγχαρητήρια το βρήκες!!')
        exit()
    print(hidden_word)
    letter = input('Γράμμα; ')
    if letter in letters:
        print('Έχεις ήδη δοκιμάσει αυτό το γράμμα !!')
        continue
    letters.append(letter)
    if letter in word:
        print('Το γράμμα υπάρχει !!')
    else:
        print('Το γράμμα δεν υπάρχει !!')
        tries -= 1
    print(f'Απομένουν {tries} προσπάθειες !!')

print('Δυστυχώς, χάσατε :( ')
print(f'Η λέξη ήταν: {word}')