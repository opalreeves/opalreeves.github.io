num_integers = int(input("How many integers would you like to enter?"))
print(f"Please enter {num_integers} integers: ")
num = int(input())
min_value = num
max_value = num

for i in range(num_integers - 1):
    num = int(input())
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num 
print(f"minimum: {min_value}")
print(f"maximum: {max_value}")
