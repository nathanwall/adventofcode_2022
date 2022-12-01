import os
import sys

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    lines = file.readlines()

elves = {}
elf_number = 1
calories = 0
for line in lines:
    if line != "\n":
        calories += int(line)
    else:
        elves.update({f"elf{elf_number}": calories})
        elf_number += 1
        calories = 0

most_calories = 0
for elf, calorie_count in elves.items():
    if calorie_count > most_calories:
        most_elf = elf
        most_calories = calorie_count 

print(f"The elf with the most calories is: {most_elf} with {most_calories}")
