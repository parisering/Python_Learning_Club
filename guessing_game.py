import random 

guessestaken = 0

print('Hello! What is your name?')
name = input()

number = random.randint(1,20)
print('Hey, '+ name +'! Let us play a game. I am thinking of a number between 1 and 20. You get 5 tries!')

while guessestaken < 6:
    print('Take a guess.')
    guess = input()
    guess = int(guess)

    guessestaken = guessestaken + 1

    if guess < number:
        print('Your guess is too low. Try again!')

    if guess > number: 
        print('Your guess is too high. Try again!')

if guess == number: 
    guessestaken = str(guessestaken)
    print('Good job, '+ name +'! You guessed my number in '+ guessestaken +' guesses!')
    break

if guess != number: 
    number = str(number)
    print('Sorry! The number I was thinking of was ' + number)


