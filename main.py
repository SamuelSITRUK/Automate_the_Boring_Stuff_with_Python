
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


#3/ Find All Matches in the Clipboard Text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
  phoneNum = '-'.join([groups[1], groups[3], groups[5]])
  if groups[8] != '':
    phoneNum += ' x' + groups[8]
  matches.append(phoneNum)
for groups in emailRegex.findall(text):
  matches.append(groups[0])

#4/ Join the Matches into a String for the Clipboard
# Copy results to the clipboard.
if len(matches) > 0:
pyperclip.copy('\n'.join(matches))
print('Copied to clipboard:')
print('\n'.join(matches))
else:
print('No phone numbers or email addresses found.')


#Project: generating random Quiz files

#import random

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New
Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West
Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(35):
# TODO: Create the quiz and answer key files.
 Generate 35 quiz files.
for quizNum in range(35):
# Create the quiz and answer key files.
u quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
v answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')
# Write out the header for the quiz.
w quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
quizFile.write('\n\n')
# Shuffle the order of the states.
states = list(capitals.keys())
x random.shuffle(states)
# TODO: Write out the header for the quiz.
# TODO: Shuffle the order of the states.
# TODO: Loop through all 50 states, making a question for each.



