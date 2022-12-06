import os
import sys

input_file = os.path.join(sys.path[0], "input.txt")

with open(input_file, "r") as file:
    datastream = file.read()
    datastream = datastream.strip()

def get_distinct_of_chunks(datastream, chunk_size):
    count = 0
    while datastream:
        chunk_to_check = datastream[:chunk_size]
        if len(set(chunk_to_check)) != len(chunk_to_check):
            count +=1
            datastream = datastream[1:]
        else:
            count += chunk_size    
            break
        
    return count

print(f"part 1: {get_distinct_of_chunks(datastream, 4)}")
print(f"part 2: {get_distinct_of_chunks(datastream, 14)}")
