import random, temp
name = input('whats is your name? ')
print('good luck ' + name)
words = [temp.read()]
word = random.choice(words)
print('guess the characters')

guesses = ''
turns = 12

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed += 1
    if failed == 0:
        print('you win!!')
        print('the word is:', word)
        break
    guess = str(input("guess a character:"))
    guesses += guess
    if guess not in word:
        turns -= 1
        print('wrong')
        print('you have', + turns, 'more to guess')
        if turns == 0:
            print('You Loose')
            print(word)