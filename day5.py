import time

start_time = time.perf_counter()
with open("day5.in", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

def sum_range(low, high):
    return high - low + 1

part_1 = 0

ranges = []
split_index = 0
for i, line in enumerate(data):
    if line != '':
        a, b = [int(i) for i in line.split('-')]
        ranges.append([a,b])
    else:
        split_index = i
        break

for num in data[split_index + 1:]:
    for low, high in ranges:
        if low <= int(num) <= high:
            part_1 += 1
            break

part_2 = 0
ranges = sorted(ranges)
prev_range = ranges[0]
for low, high in ranges[1:]:
    prev_low = prev_range[0]
    prev_high = prev_range[1]

    if prev_high < low:
        part_2 += sum_range(prev_low, prev_high)
        prev_range = [low, high]
        continue
    
    if low < prev_range[0]:
        prev_range[0] = low
    
    if high > prev_range[1]:
        prev_range[1] = high

part_2 += sum_range(prev_range[0], prev_range[1])

print(part_1)
print(part_2)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")