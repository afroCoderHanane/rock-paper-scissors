import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_ai=[rock,paper,scissors]
user=[rock,paper,scissors]
# game_list = [[game_ai],[user]]

# ai_choice = random.randint(0,len(game_ai)-1)
ai_choice = random.choice(game_ai);

user_choice = int(input("Enter your choice\n 1: for rock 2: for paper 3: for scissors "))
if user_choice <0 or user_choice>3:
  print("You entered an invalid input ")
else :
  print("AI choose\n"+ ai_choice)
  print("You choose\n"+ user[user_choice-1])
  if(ai_choice==game_ai[0] and user[user_choice-1]==user[1] ):
    print(" You won")
  elif (ai_choice==game_ai[1] and user[user_choice-1]==user[2] ):
    print(" You won")
  elif (ai_choice==game_ai[2] and user[user_choice-1]==user[0] ):
    print("You won")
  elif(ai_choice == user[user_choice -1]):
    print("It is a draw")
  else:
    print("AI machine won, You lost")