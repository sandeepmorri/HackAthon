def findMissingNumbers(numbers):
    num_set = set(numbers)
    output = []
    for i in range(1, max(numbers) + 1):  # Iterating up to the max value in the list
        if i not in num_set:
            output.append(i)
    return output

# Example usage
listOfNumbers = [1, 2, 4, 5, 7, 9, 10, 12]  # A sample list with missing numbers
print(findMissingNumbers(listOfNumbers))
