#ask the user to enter a postitive integer
num = int(input("Please enter a positive integer:"))

#print the factors of the number including 1 and the number itself
print(f"The factors of {num} are:")

# for loop for all numbers leading up to num. need num+1 b/c range only includes num-1
for i in range(1, num + 1):
    #make sure only  print numbers that num divides by evenly (remainder zero)
    if num % i == 0:
        print(i)