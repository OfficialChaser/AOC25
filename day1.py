with open("day1.in", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

dial_count = 50
part_1 = 0
part_2 = 0
for line in data:
    dir = line[0]
    amt = int(line[1:])

    if amt > 100:
        part_2 += amt // 100
        amt = amt %  100
    
    already_added = False
    prev_dial_count = dial_count
    
    if  dir == "L":
        dial_count -= amt
        if dial_count < 0:
            dial_count = 100 + dial_count
            if prev_dial_count != 0:
                part_2 += 1
                already_added = True
    else:
        dial_count += amt
        if dial_count > 99:
            dial_count = dial_count - 100
            if prev_dial_count != 0:
                part_2 += 1
                already_added = True
    
    if  dial_count == 0:
        part_1 += 1
        if not already_added:
            part_2 += 1

print(part_1)
print(part_2)