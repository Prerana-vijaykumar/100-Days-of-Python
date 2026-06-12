print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
print("Welcome to treasure island !")
print("your mission is to find the treasure")

choice_1=input("You are on cross roads , where you wanna go ? Choose 'left' or 'right'").lower()
if choice_1=="left" :
    choice_2=input("You arrived near a lake , the treasure is in the house which is in the island, how would you like to get there!? , 'wait' till boat arrives or 'swim'").lower()
    if choice_2=="wait":
        choice_3=input("You safely reached the island, Choose which door of the house you'd like to open now ? 'red' , 'yellow' , 'blue' ").lower()
        if choice_3=="red":
            print("You opened the door where fire burst took !, \n Game over!")
        elif choice_3=="yellow":
            print("You found the treasure! \n You won !")
        elif choice_3=="blue":
            print("You opened the door of beasts!, Game over !")
        else:
            print("you typed something that doesnt exists in the option")

    elif choice_2=="swim":
        print("Alegator attacked! , Game over")
    else:
        print("Yopu typed something wrong , Game over!")
else:
    print("Game over!")

