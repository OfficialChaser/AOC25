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

modified_ranges = []
for low, high in ranges:
    if not modified_ranges:
        modified_ranges.append([low, high])
        continue

    for i, m_low, m_high in enumerate(modified_ranges):
        if low < m_low:
            m_low = low
        if high > m_high:
            m_high = high

print(part_1)
