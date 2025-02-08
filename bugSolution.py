def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [0,0,0]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_with_string = [1,2,'a']
result = calculate_average(my_list_with_string)
print(f"The average is: {result}") #This will now correctly compute the average