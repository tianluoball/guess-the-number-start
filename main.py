#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random
import sys

chanceleft = 0
iniNumber = random.randint(0, 100)
easy = 10
hard = 5

def compare(input_number):
    if input_number == iniNumber:
        return True
    elif input_number < iniNumber:
        print("The number is too low")
        return False
    elif input_number > iniNumber:
        print("The number is too high")
        return False


def validNumber():
    isvalidNumber = False
    while isvalidNumber == False:
        try:
            number = int(input("Please input a number: "))
            isvalidNumber = True
            return number
        except ValueError:
            print('The provided value is not an integer')
            continue


def DifficultyChoose():
    validDifficulty = False
    while validDifficulty == False:
      Difficulty = input("Please choose your difficulty. Type 'Easy' or 'Hard': ")
      if Difficulty == "Hard" or Difficulty == "hard":
        return hard
      elif Difficulty == "Easy" or Difficulty == "easy":
        return easy
      else:
        continue

def mainGame():
    chanceleft = DifficultyChoose()
    endGame = False
    while endGame == False:
        input_number = validNumber()
        if (compare(input_number) == True):
            print("Congrats!")
            break
        else:
            chanceleft -= 1

        if (chanceleft == 0):
            print("You lose!")
            break

        print(f"You have {chanceleft} attemps remaining to guess the number.")



print(logo)
print("Welcome to the number guessing game, you have several chances to guess a integer from 0 to 100 depends on difficulty")
restart = False
while restart == False:
    mainGame()
    while True:
        answer = input("Do you want to play another round? Y/N:")
        if (answer == "Y" or answer == "Yes" or answer == "y"):
            continue
        else:
            sys.exit()
