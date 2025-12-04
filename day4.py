import time

start_time = time.perf_counter()

with open("day4.in", "r") as f:
    grid = [list(i) for i in f.read().strip().split("\n")]

part_1 = 0

for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char != "@":
            continue
        
        roll_counter = 0
        directions = [
            (-1, 0),  # Up
            (-1, 1),  # Top-right
            (0, 1),   # Right
            (1, 1),   # Bottom-right
            (1, 0),   # Down
            (1, -1),  # Bottom-left
            (0, -1),  # Left
            (-1, -1)  # Top-left
        ]

        for dy, dx in directions:
            new_col = x + dx
            new_row = y + dy

            if 0 <= new_row < len(row) and 0 <= new_col < len(grid):
                if grid[new_row][new_col] == "@": roll_counter += 1
        
        if roll_counter < 4:
            part_1 += 1

running = True

part_2 = 0

while running:
    rolls_to_delete = []
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char != "@":
                continue
            
            roll_counter = 0
            directions = [
                (-1, 0),  # Up
                (-1, 1),  # Top-right
                (0, 1),   # Right
                (1, 1),   # Bottom-right
                (1, 0),   # Down
                (1, -1),  # Bottom-left
                (0, -1),  # Left
                (-1, -1)  # Top-left
            ]

            for dy, dx in directions:
                new_col = x + dx
                new_row = y + dy

                if 0 <= new_row < len(row) and 0 <= new_col < len(grid):
                    if grid[new_row][new_col] == "@": 
                        roll_counter += 1
                        
            
            if roll_counter < 4:
                part_2 += 1
                rolls_to_delete.append((y, x))
    
    if not rolls_to_delete:
        running = False
        continue
    
    for y, x in rolls_to_delete:
        grid[y][x] = "."
    
    rolls_to_delete.clear()


print(part_1)
print(part_2)

end_time = time.perf_counter()
execution_time = end_time - start_time

print(f"Execution time: {execution_time:.6f} seconds")