import os
import sys

get_scenario_1_value = {"A X":4, "A Y":8, "A Z":3, "B X":1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6}
get_scenario_2_value = {"A X":3, "A Y":4, "A Z":8, "B X":1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    lines = file.readlines()

scenario_1_value = 0
scenario_2_value = 0
for line in lines:
    scenario_1_value += get_scenario_1_value[line.strip()] 
    scenario_2_value += get_scenario_2_value[line.strip()] 

print(f"scenario 1: {scenario_1_value}")
print(f"scenario 2: {scenario_2_value}")
