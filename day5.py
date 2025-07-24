# Loops 


# sum
student_marks = [90,55,33,22,11,9,8,5,1,55,100,200,300,22,5]
total_marks = sum(student_marks)
print(total_marks)

#Manual method
sum = 0
for score in student_marks:
    sum += score
print(f"Manual method sum: {sum}")