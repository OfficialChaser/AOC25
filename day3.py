with open("day3.in", "r") as f:
    data = [i for i in f.read().strip().split("\n")]

part_1 = 0

# for battery in data:
#     num_list = [int(i) for i in list(battery)]

#     highest_num = max(num_list[:len(num_list) - 1])
#     part_1 += 10 * highest_num

#     start_index = num_list.index(highest_num)
#     second_num = max(num_list[start_index + 1:])
#     part_1 += second_num

#     print(highest_num, second_num)

# print(part_1)

part_2 = 0

for battery in data:
    num_list = [int(i) for i in list(battery)]

    optimal_jolt = []
    gaps = 0
    while len(optimal_jolt) != 7:
        if not num_list:
            break
        optimal_num = max(num_list[:len(num_list) - len(optimal_jolt) - 1 - gaps])
        optimal_jolt.append(optimal_num)

        old_len = len(num_list)
        num_list = num_list[num_list.index(optimal_num) + 1:]
        gaps += old_len - len(num_list) - 1

        if len(optimal_jolt) + len(num_list) == 13: # Remove the smallest number if there's only one more number left to clear
            num_list.remove(min(num_list))
            optimal_jolt += num_list
            print("hello")

    part_2 += int(''.join([str(i) for i in optimal_jolt]))
    
    print(num_list, optimal_jolt)
        
