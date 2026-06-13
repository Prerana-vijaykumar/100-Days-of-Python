import random

rock='''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''
            _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        '''

scissors='''
            _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

        '''
my_choice=int(input(("What do you choose? Type 0 for Rock , 1 for paper or 2 for Scissors ")))

if my_choice<0 or my_choice>2:
    print("Please give a valid input")
else:
    
    if my_choice==0:
        print(f"you chose rock \n{rock}")
    elif my_choice==1:
        print(f"you chose paper \n{paper}")
    elif my_choice==2:
        print(f"you chose scissors \n{scissors}")


    computer_choice=random.randint(0,2)

    if computer_choice==0:
        print(f"Computer chose rock \n{rock}")
    elif computer_choice==1:
        print(f"Computer chose paper \n{paper}")
    elif computer_choice==2:
        print(f"Computer chose scissors \n{scissors}")


    if my_choice==computer_choice:
        print("It's a draw")

    elif my_choice == 0 and computer_choice == 1:
        print("Computer won!")
    elif my_choice==0 and computer_choice==2:
        print("You won !")
    elif my_choice==1 and computer_choice==0:
        print("You won !")
    elif my_choice==1 and computer_choice==2:
        print("Computer won !")
    elif my_choice==2 and computer_choice==0:
        print("Computer won !")
    elif my_choice==2 and computer_choice==1:
        print("You won !")


    elif computer_choice == 0 and my_choice == 1:
        print("You won!")
    elif computer_choice==0 and my_choice==2:
        print("Computer won !")
    elif computer_choice==1 and my_choice==0:
        print("Computer won !")
    elif computer_choice==1 and my_choice==2:
        print("You won !")
    elif computer_choice==2 and my_choice==0:
        print("You won !")
    elif computer_choice==2 and my_choice==1:
        print("Computer won !")

    else:
        print("Something went wrong , try again!")





    
