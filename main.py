
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


#Chapter 5: ...
def Fantasy_Game_Inventory (inventory) :
  print(Inventory)
  Tot_items=0
  for k,v in inventory.items() :
    print(k + ' : ' + str(v))
    tot_items+=v
  print("Total Number of Items : " + str(Tot_items))
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
Fantasy_Game_Inventory(stuff)


def addToInventory (loot, stuff):
  for i in loot :
    if i in stuff.keys() :
      stuff[i] +=1
    else :
      stuff[i] = 1

addToInventory (loot1, stuff1)
Fantasy_Game_Inventory(stuff1)


#Chapter 6 Manipulating Strings

def TablePrinter (UnrulyList) :
  width_Llist= len(UnrulyList[0])
  height_Llist=len(UnrulyList)
  j=0
  print_List=""
  while j<width_Llist :
    i=0
    to_print=""
    while i<height_Llist :
      to_print = to_print + (str(UnrulyList[i][j]) + " ")
      i+=1
    print(to_print)
    j+=1

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

TablePrinter(tableData)




#Chapter 7 ; Pattern Matching with Regular Expressions


#Regular expressions = allow you to specify a pattern of text to search for
#Project : a tool for finding every phone number and email address in a long web page or document.

#1/ imports necessary and cretation of the regew expression for phone numbers
'''import pyperclip, re
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)
'''
#2/Create EMail Regex
'''
# Create email regex.
emailRegex = re.compile(r'''(
u [a-zA-Z0-9._%+-]+ # username
v @ # @ symbol
w [a-zA-Z0-9.-]+ # domain name
(\.[a-zA-Z]{2,4}) # dot-something
)''', re.VERBOSE)
'''


