import re

with open("day2.in", "r") as f:
    ranges = [i for i in f.read().strip().split(",")]

part_1 = 0

for r in ranges:
    start, end = [int(i) for i in r.split("-")]
    
    for big_num in range(start, end + 1):
        big_num =  str(big_num)
        if len(big_num) % 2 == 1:
            continue
        if big_num[:(len(big_num) // 2)] == big_num[(len(big_num) // 2):]:
            part_1 += int(big_num)

print(part_1)

part_2 = 0

for r in ranges:
    start, end = [int(i) for i in r.split("-")]

    for big_num in range(start, end + 1):
        big_num =  str(big_num)
        invalid = False

        if len(set(big_num)) == 1 and len(big_num) > 1:
                invalid = True

        if len(big_num) > 3 and not invalid:
            num_length = int(len(big_num))
            possible_sequence_lens = [i for i in range(1, num_length+1) if num_length % i == 0 and i != 1 and i != num_length]
            for length in possible_sequence_lens:
                seq = big_num[:length]

                if big_num.count(seq) == len(big_num) // length:
                    invalid = True
        
        if invalid:
                part_2 += int(big_num)
    
print(part_2)