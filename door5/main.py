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

with open(input_file, "r") as file:
    instructions = file.readlines()

original_stacks = {1:["R","N","P","G"], 
                   2:["T","J","B","L","C","S","V","H"],
                   3:["T","D","B","M","N","L"],
                   4:["R","V","P","S","B"],
                   5:["G","C","Q","S","W","M","V","H"],
                   6:["W","Q","S","C","D","B","J"],
                   7:["F","Q","L"],
                   8:["W","M","H","T","D","L","F","V"],
                   9:["L","P","B","V","M","J","F"]}

print(get_last_items(sort_crates(False)))
print(get_last_items(sort_crates(True)))
