def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n == 0:
        print("Can't find the median of an empty list!")
        return None
    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        middle_left = sorted_numbers[n // 2 - 1]
        middle_right = sorted_numbers[n // 2]
        return (middle_left + middle_right) / 2
    
user_input = input("Please enter numbers separated by spaces.")
numbers = [float(x) for x in user_input.split()]
result =  find_median(numbers)
print(f"The median is: {result}")
