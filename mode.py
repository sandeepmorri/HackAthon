list1 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]
frequency = {}

# Calculate frequency of each element
for num in list1:
    frequency.setdefault(num, 0)
    frequency[num] += 1

# Find the highest frequency
frequent = max(frequency.values())

# Identify the mode(s)
modes = [key for key, value in frequency.items() if value == frequent]

# Print the mode(s)
print("Mode(s):", modes)
print("Frequency:", frequent)