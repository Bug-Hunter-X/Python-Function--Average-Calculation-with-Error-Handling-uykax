def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = [1, 2, 3, 4, 5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}") # This will work fine

my_list_with_zero = [0,0,0]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}") # This will also work fine

my_list_with_string = [1,2,'a']
result = calculate_average(my_list_with_string)
print(f"The average is: {result}") # This will throw an error