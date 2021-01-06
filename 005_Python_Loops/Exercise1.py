# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
#Instruction 1: Separate each list
#Instruction 2: Average of Height
#Instruction 3: Round-Up Average Height

overall = 0
for heights in student_heights:
    overall += heights
quantity = 0
for studs in student_heights:
    quantity += 1
average = overall / quantity

print(round(average))