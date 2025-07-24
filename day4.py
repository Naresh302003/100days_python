import random
import day3

# random_integer = random.randint(1,20)
# print(random_integer)
#
# print(day3.float_number)
#
# random_float = round(random.random() * 10,2)
# print(random_float)
#
# random_float = round(random.uniform(1,10),2)
# print(random_float)
#
#
# random_integer = random.randint(0,1)
# user_input = int(input('Enter "0" or "1": '))
#
# if random_integer == 0 == user_input:
#     print("Heads")
# else:
#     print("Tails")

# indian_states = [
#     "Andhra Pradesh",
#     "Arunachal Pradesh",
#     "Assam",
#     "Bihar",
#     "Chhattisgarh",
#     "Goa",
#     "Gujarat",
#     "Haryana",
#     "Himachal Pradesh",
#     "Jharkhand",
#     "Karnataka",
#     "Kerala",
#     "Madhya Pradesh",
#     "Maharashtra",
#     "Manipur",
#     "Meghalaya",
#     "Mizoram",
#     "Nagaland",
#     "Odisha",
#     "Punjab",
#     "Rajasthan",
#     "Sikkim",
#     "Tamil Nadu",
#     "Telangana",
#     "Tripura",
#     "Uttar Pradesh",
#     "Uttarakhand",
#     "West Bengal"
# ]

# # print(len(indian_states[::-1]))
# indian_states[0] = "TamilNadu"
# indian_states.append("New Jersey")
# indian_states.extend(["Dubai","Georgia","Delaware"])
# print(indian_states[::])


import random
print("Welcome to Calculator Application")
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
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissor = '''  
  _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list_game = [rock,paper,scissor]
user_choice = int(input("Enter your choice: 0 for rock, 1 for paper, 2 for scissor: "))
if user_choice >= 0 and user_choice <= 2:
    print("You chose: ",list_game[user_choice])
else:
    print("Invalid choice")


computer_choice = random.randint(0,2)
if user_choice >= 0 and user_choice <= 2:
    print("Computer chose: ",list_game[computer_choice])
else:
    print("computer: i can't recognize what you did choose")


if user_choice < 0 or user_choice > 2:
    print("")
elif user_choice == computer_choice:
    print("draw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("User wins")
else:
    print("Computer wins")
