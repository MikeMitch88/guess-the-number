# A = [9, 9, 9]
# B = [2, 3, 5]

# s = ''.join(map(str, A))
# print(int(s) + 1)
import random
print('Hello world!\n''what is your name')
myName = input()

number = random.randint(1, 20)

print('Well, '+ myName +', I am thinking of a number between 1 and 20.')


guessTaken = 0
print('I have set a number for you to guess. You have 6 attempts to find it.')
for guessTaken in range(6):
    print('Take a guess : ')

    guess = input()

    guess = int(guess)    

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break
       
if guess == number:
     guessesTaken = str(guessTaken + 1)
     print('Good job, ' + myName + '! You guessed my number in ' +
          guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
    

    