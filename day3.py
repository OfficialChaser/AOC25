import time

start_time = time.perf_counter()

with open("day3.in", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

part_1 = 0

for battery in data:
    num_list = [int(i) for i in list(battery)]

    highest_num = max(num_list[:len(num_list) - 1])
    part_1 += 10 * highest_num

    start_index = num_list.index(highest_num)
    second_num = max(num_list[start_index + 1:])
    part_1 += second_num

part_2 = 0

for battery in data:
    num_list = [int(i) for i in list(battery)]

    optimal_jolt = []

    while len(optimal_jolt) < 12:
        optimal_num = max(num_list[:len(num_list) - (11 - len(optimal_jolt))])

        optimal_jolt.append(optimal_num)

        old_len = len(num_list)
        num_list = num_list[num_list.index(optimal_num) + 1:]

    part_2 += int(''.join([str(i) for i in optimal_jolt]))

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")
        
