import math

with open("day6.in", "r") as f:
    data = [i for i in f.read().split("\n")]

part_1 = 0

num_sets = []
cols = {}

for line in data[:-1]:
    nums = line.split(" ")
    corrected_nums = []
    for num in nums:
        if num:
            corrected_nums.append(int(num))
    
    num_sets.append(corrected_nums)

operands = [i for i in list(data[-1]) if i != " "]

for i in range(len(num_sets[0])):
    for num_set in num_sets:
        if not i in cols:
            cols[i] = [num_set[i]]
        else:
            cols[i].append(num_set[i])

for key, nums in cols.items():
    if operands[key] == "+":
        part_1 += sum(nums)
    else:
        part_1 += math.prod(nums)

str_num_sets = []
for y, line in enumerate(data[:-1]):
    nums = line.split(" ")
    corrected_nums = []
    highest_num_len = len(max([str(i) for i in cols[y]], key=len))
    
    modified_num = ""
    for num in nums:
        if num and len(num) == highest_num_len:
            corrected_nums.append(num)
        elif not num:
            modified_num += "."
        else:
            modified_num += num

        if len(modified_num) == highest_num_len:
            corrected_nums.append(modified_num)
            modified_num = ""
    
    str_num_sets.append(corrected_nums)

new_cols = {}

char_counter = 0
for num_set in str_num_sets:
    for num in num_set:
        for char in num:
            if char != ".":
                if not char_counter in new_cols:
                    new_cols[char_counter] = char
                else:
                    new_cols[char_counter] += char
            char_counter += 1
    char_counter = 0

for key, num in new_cols.items():
    new_cols[key] = int(num)

ranges = []
for num_set in cols.values():
    ranges.append(len(max([str(i) for i in num_set], key=len)))

part_2 = 0
print(len(ranges))
i = 0
operand_index = 0
for r in ranges:
    result = 0
    for j in range(i, i + r):
        if j == len(new_cols): print(j == len(new_cols)), print(operand_index), print(len(operands))
        
        if operands[operand_index] == "+":
            result += new_cols[j]
        else:
            if result == 0:
                result = new_cols[j]
            else:
                result *= new_cols[j]
    

    part_2 += result
    result = 0
    i += r
    operand_index += 1

print(part_1)
print(part_2)