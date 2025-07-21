# name1 = "madam"
#
# if name1 == name1[::-1]:
#     print("The string is palindrome")
# else:
#     print("the string is not palindrome")
#
# print(123_456_789)
#
# print("123" + "456")

#
# print(type("Hello"))
# print(type(1234))
# print(type(True))
# print(type(1.234))
#
# # type conversion
# print(type(int("123")))
#
# print (f"You Name length is: {len(input("Enter your Name: ").strip())}")
#
# print(6 + 3)
# print(6 - 3)
# print(6 * 3)
# print(6 / 3)
# print(6 // 3)
# print(6 % 3)
# print(5 % 3)
# print(5 // 2)

# print(3* (3 + 3) // 3 - 3)


# BMI Calculation
#
# height = float(input("Enter Your Height In Feet: "))
# weight = float(input("Enter Your Weight: "))
#
# height_meter = height * 0.3048
#
# BMI = round( weight / (height_meter ** 2),2)
#
# print("*********************************")
# print(f"Your BMI Value is: {round(BMI)}")
#
# if BMI < 18:
#     print("You are Underweight.")
# elif 18 <= BMI < 24.9:
#     print("You have normal weight.")
# elif 25 <= BMI < 29.9:
#     print("You are Overweight.")
# else:
#     print("Your are Obese")
# print("*********************************")
#
#
# score = 0
#
# score //= 1
# print(score)

# age = 12
#
# print("you are age:"+ age + "year old")

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill: ₹"))
tips = int(input("How much tip would you want to give? 10,12, or 15? :  "))
split = int(input("How many people to split this bill: "))

total_amount_tips = (tips/100)*total_bill + total_bill
total_amount = round(total_amount_tips / split,2)

print(f"Each person should pay: ₹{total_amount}")