#ask the user how many variables they want to enter
num_integers = int(input("How many integers would you like to enter?"))

print(f"Please enter {num_integers} integers: ")

#use first value entered to initialize the maximum and minimum
num = int(input())
min_value = num
max_value = num

#for loop for remaining integers
for i in range(num_integers - 1):
    num = int(input())
    #if statement for finding minimum and maximum values
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num 

#print results
print(f"minimum: {min_value}")
print(f"maximum: {max_value}")
