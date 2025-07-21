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

indian_states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

# print(len(indian_states[::-1]))
indian_states[0] = "TamilNadu"
indian_states.append("New Jersey")
indian_states.extend(["Dubai","Georgia","Delaware"])
print(indian_states[::])