#for loops and the range() function

evens = 0
for numbers in range (1, 102, 2):
    #print(numbers - 1)
    subtracted = numbers - 1
    evens += subtracted
print(f"\n{evens}")