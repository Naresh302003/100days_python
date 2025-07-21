# def even_odd(num):
#     even = []
#     odd = []
#     for i in num:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#
#     print(even)
#     print(odd)
#
#
# num1 = int(input("Enter The Num for the list where you want to start: "))
# num2 = int(input("Enter the number for the list where you want to end before: "))
# even_odd(range(num1, num2))

# age = int(input("Enter your age: "))
#
# if age <= 18:
#     if age >= 12:
#         print("Your should pay $7")
#     else:
#         print("You should pay $5")
# else:
#     print("You should pay $12")
#
#
# print("Welcome to the Roller coaster")
# height = int(input("Enter your Height please: "))
# bill = 0
#
# if height >= 120:
#     print("You can ride the rollercoaster")
#     age = int(input("Enter your age here: "))
#     if age <= 12:
#         bill += 5
#         print("Child tickets are 5$")
#     elif age <= 18:
#         bill += 7
#         print("Youth tickets are 7$")
#     elif 45 <= age <= 50:
#         bill += 0
#     else:
#         bill += 12
#         print("Adult tickets are 12$")
#
#     want_photo = input("Do you want to have a photo take? if you want type y or no type n: ").lower()
#     if want_photo == "y":
#         bill += 4
#
#     print(f"Your total bill is: ${bill}")
# else:
#     print("sorry you have to grow up before you ride.")
#

# print("Welcome to python pizza Deliveries!")
# size = input("What size pizza Do you want? S,M and L: ").lower()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese on you pizza? Y or N: ").lower()
# bill = 0
#
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# elif size == "l":
#     bill += 25
# else:
#     print("You type wrong input")
#
# if pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your final amount is ${bill}")

# print('''*******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/[TomekK]
# *******************************************************************************''')
#
# print("Welcome to treasure island.")
# print("Your mission is find the treasure.")
# step1 = input('You\'re at a crossroad, where do you want do? Type "Left" or "right": ').lower()
#
# if step1 == "left":
#     step2 = input('you\'ve come to lake. there is an island in the middle of the lake.Type "wait" to waite for boat. type "swim" to swim across: ').lower()
#     if step2 == "wait":
#         step3 = input('You\'ve reached and there is trice door. which door would you like to open "Red" or "Blue or "Yellow": ').lower()
#         if step3 == "yellow":
#             print("You win the game!")
#         elif step3 == "red":
#             print("Game over!")
#         elif step3 == "blue":
#             print("Game over!")
#         else:
#             print("You've typed wrong input, Game over!")
#     elif step2 == "swim":
#         print("you've swim in crocodile lake so crocodile was finished you, Game Over!")
#     else:
#         print("You've type wrong input.")
#
# elif step1 == "right":
#     print("you fell in the hole. Game over.")
# else:
#     print("You've type wrong input!")

float_number = 12.2435