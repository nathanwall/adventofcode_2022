import os
import sys

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    lines = file.readlines()

unsorted_calories = []
calories = 0
for line in lines:
    if line != "\n":
        calories += int(line)
    else:
        unsorted_calories.append(calories)
        calories = 0

unsorted_calories.sort(reverse=True)
sorted_calories = unsorted_calories

print(f"1st: {sorted_calories[0]}, 2nd: {sorted_calories[1]}, 3rd: {sorted_calories[2]}")
print(f"Total of top 3: {sum(sorted_calories[0:3])}")
