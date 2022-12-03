import os
import sys
from itertools import islice

def get_item_value(item):
    if item.isupper():
        item_value = ord(item) - 38
    else:
        item_value = ord(item) - 96
    
    return item_value

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    rucksacks = file.readlines()

with open(input_file, "r") as file:
    rucksack_groups = []
    while True:
        next_group = list(islice(file,3))
        if not next_group:
            break
        else:
            rucksack_groups.append(next_group)

total_item_value = 0
for rucksack in rucksacks:
    rucksack = rucksack.strip()
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]
    common_item = list(set(compartment1).intersection(compartment2))[0]

    total_item_value += get_item_value(common_item)

total_badge_value = 0
for group in rucksack_groups:
    group = [rucksack.strip() for rucksack in group]
    badge = list(set.intersection(*map(set, group)))[0]

    total_badge_value += get_item_value(badge)

print(f"total_item_value: {total_item_value}")
print(f"total_badge_value: {total_badge_value}")