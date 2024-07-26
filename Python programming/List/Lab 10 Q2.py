# Write a Python program to get the largest and smallest number from a list without builtin functions.
numbers = [3, 5, 1, 9, -2, 7, 10, -4, 6]
if len(numbers) > 0:
    largest = numbers[0]
    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
        if numbers[i] < smallest:
            smallest = numbers[i]

    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")
else:
    print("The list is empty.")
