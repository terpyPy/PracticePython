#!/usr/bin/python3
#  Author:      Cameron Kerley
#  Date:        6 Feb 2019
#  Description: game.py is a guessing game for a number between 1-99
#
import random # import random implements pseudo-random number
#strings that will operate in  part of the while loop that proceeds it
guesses = 0# guesses needs to be an int,as it keeps tack of the users total guesses
target = random.randrange(0, 100)#this genarates a pseudo-random number between 1 and 99

print('Enter an integer between 0 and 99, inclusive: ')# our intal query for the user
userInput =(input())# holds the intal input we request from the user
					#this inputs value will operate the while loop
while ((userInput[0] >= '0') and (userInput[0] <= '9')):
		guesses = guesses + 1
		guess = int(userInput)
		if (guess < target):
				print (str(guess) + ' is to low')
		elif (guess > target):
				print (str(guess) + ' is to high')
		else:
				print('Yay! you guessed it!')
				break

		print('Enter an integer between 0 and 99, inclusive: ')
		userInput =(input())

print('you took ' + str(guesses) + ' guesses.\n' +                     \
		'thanks for playing')
