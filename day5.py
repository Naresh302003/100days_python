# # Loops 


# # sum
# student_marks = [90,55,33,22,11,9,8,5,1,55,100,200,300,22,5]
# total_marks = sum(student_marks)
# print(total_marks)

# #Manual method
# sum = 0
# for score in student_marks:
#     sum += score
# print(f"Manual method sum: {sum}")

# # max

# print(max(student_marks))

# #Manual method
# mx_score = 0
# for score in student_marks:
#     if score > mx_score:
#         mx_score = score
# print(f"Manual method max score: {mx_score}")

# Range
# print(list(range(1,11,3)))

# sum1 = 0
# for i in range(1,21,2):
#     sum1 += i
# print(sum1)

# Exercise 1
# total = 0
# for j in range(1,101):
#     total += j
# print(total)


# # EXERCISE PROBLEM 1 
# for number in range(1,101):
#     if (number % 3 == 0) and (number % 5 == 0):
#         print("FizzBuzz")
#     elif (number % 3 == 0):
#         print("Fizz")
#     elif (number % 5 == 0):
#         print("Buzz")
#     else:
#         print(number)

# Password Generator
import random
import string

def password_generator(letters,symbols,digits):
    password = ""
    characters = string.ascii_letters
    punctuation = ['!','#','$','%','(',')','*','+']
    numbers = string.digits

    for char in range(1,letters + 1):
        password += random.choice(characters)
    for char in range(1,symbols + 1):
        password += random.choice(punctuation)
    for char in range(1,digits +1):
        password += random.choice(numbers)
    return password 
    


print("Password Generator \U0001F512")
try:
    letters = int(input("Enter how many letters do you want your password: "))
    symbols  = int(input("Enter how many symbols do you want in your password: "))
    digits = int(input("Enter how many digits do you want in your password: "))
    if (letters < 3) and (symbols < 1) and (digits < 1):
        print("Password length should be more then 3 letters and more then 1 symbols and more then 1 digits.")
    else:
        print("Generated password:",password_generator(letters,symbols,digits))

except ValueError:
    print("Enter valid number.")








