import os
import sys

def get_scenario_1_value(scenario):
    match scenario:
        case "A X":
            value = 4
        case "A Y":
            value = 8
        case "A Z":
            value = 3
        case "B X":
            value = 1
        case "B Y":
            value = 5
        case "B Z":
            value = 9
        case "C X":
            value = 7
        case "C Y":
            value = 2
        case "C Z":
            value = 6

    return value

def get_scenario_2_value(scenario):
    match scenario:
        case "A X":
            value = 3
        case "A Y":
            value = 4
        case "A Z":
            value = 8
        case "B X":
            value = 1
        case "B Y":
            value = 5
        case "B Z":
            value = 9
        case "C X":
            value = 2
        case "C Y":
            value = 6
        case "C Z":
            value = 7

    return value

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    lines = file.readlines()

scenario_1_value = 0
scenario_2_value = 0
for line in lines:
    scenario_1_value += get_scenario_1_value(line.strip()) 
    scenario_2_value += get_scenario_2_value(line.strip()) 

print(f"scenario 1: {scenario_1_value}")
print(f"scenario 2: {scenario_2_value}")
