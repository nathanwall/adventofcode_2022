import os
import sys

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    lines = file.readlines()

fully_contained = 0
overlaps = 0
for line in lines:
    line = line.strip()
    ids = line.split(",")
    id1_start, id1_end = [int(x) for x in ids[0].split("-")]
    id2_start, id2_end = [int(x) for x in ids[1].split("-")]

    if (id1_start <= id2_start and id2_end <= id1_end) or \
       (id2_start <= id1_start and id1_end <= id2_end):
        fully_contained += 1
    
    id1_range = range(id1_start, id1_end+1)
    id2_range = range(id2_start, id2_end+1)
    common = list(set(id1_range).intersection(id2_range))

    if common:
        overlaps += 1
        
print(f"fully contained:{fully_contained}")
print(f"overlaps: {overlaps}")
