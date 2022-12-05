import os
import sys
import re
import copy

def get_last_items(stacks):
    last_items = ""
    for key, value in stacks.items():
        last_items = last_items + value[-1]
    
    return last_items

def sort_crates(multiple_moves):
    stacks = copy.deepcopy(original_stacks)
    for instruction in instructions:
        move_amount, move_from, move_to = [int(x) for x in re.findall(r"\d+", instruction)]
        crate_list = []
        for i in range(move_amount):
            crate_list.append(stacks[move_from][-1])
            del stacks[move_from][-1]
    
        if multiple_moves:
            crate_list.reverse()
            
        stacks[move_to].extend(crate_list)
    
    return stacks

input_file = os.path.join(sys.path[0], "input.txt")
stacks_file = os.path.join(sys.path[0], "stacks.txt")

with open(input_file, "r") as file:
    instructions = file.readlines()

with open(stacks_file, "r") as file:
    lines = file.readlines()

original_stacks = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
for line in lines:
    count = 1
    for crate in line[1], line[5], line[9], line[13], line[17], line[21], line[25], line[29], line[33]:
        stack = []
        if len(crate.strip()) and not crate.isnumeric() > 0:
            original_stacks[count].insert(0,crate)
        count += 1 

print(get_last_items(sort_crates(False)))
print(get_last_items(sort_crates(True)))
