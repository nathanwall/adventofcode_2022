import os
import sys
from collections import defaultdict

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    commands = file.readlines()

dirs = defaultdict(int)
pwd = []
for command in commands:
    command = command.strip()
    if command == "$ cd ..":
        del pwd[-1]
    elif command.startswith("$ cd"):
        dir = command.split(" ")[2]
        pwd.append(dir)
    elif command[0].isdigit():
        size = int(command.split(" ")[0])
        for dir_no in range(len(pwd)):
            dirs["/".join(pwd[:dir_no + 1])] += size

total_size = 0
big_dirs = []
total_space = 70000000
update_size = 30000000
for size in dirs.values():
    if size < 100000:            
        total_size += size
    if dirs["/"] - size <= (total_space - update_size):
        big_dirs.append(size)

print(f"Total of directories less than 1000000: {total_size}")
print(f"Size of smallest directory to delete: {sorted(big_dirs)[0]}")
