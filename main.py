
#Chapter3 : Functions
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
print('Take a guess.')
guess = int(input())
if guess < secretNumber:
print('Your guess is too low.')
elif guess > secretNumber:
print('Your guess is too high.')
else:
break # This condition is the correct guess!
if guess == secretNumber:
print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
print('Nope. The number I was thinking of was ' + str(secretNumber))


def collatz (number):
  if number%2==0:
    print(number//2)
    return (number//2)
  else :
    print (3*number+1)

def collatz_automatise(number_start=1) :
  number_start=int(input())
  end_number=collatz(number_start)
  while end_number!=1:
    end_number = collatz(end_number)


#Chapter 4:lists

def character_picture_grid (grid):
  width_grid= len(grid[0])
  height_grid=len(grid)
  j=0
  while j <width_grid :
      i=0
      to_print=""
      while i< height_grid :
        to_print = to_print + grid[i][j]
        i+=1
      print(to_print)
      j+=1 

  
character_picture_grid([['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']])
