def snake_sequence_helper(grid, i, j, m, n):

    maximum_down_value = grid[i][j]
    maximum_right_value = grid[i][j]
            
    if i + 1 <= m and (grid[i][j] + 1 == grid[i+1][j] 
    or grid[i][j] - 1 == grid[i+1][j]):
        
        maximum_down_value += snake_sequence_helper(grid, i + 1, j, m, n)
    
    if j + 1 <= n and (grid[i][j] + 1 == grid[i][j+1] 
    or grid[i][j] - 1 == grid[i][j+1]):
        
        maximum_right_value += snake_sequence_helper(grid, i, j + 1, m, n)
    
    return max(maximum_down_value, maximum_right_value)

def snake_sequence(grid):

    m = len(grid) - 1
    n = len(grid[0]) - 1

    maximum_value = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):

            current_value = snake_sequence_helper(grid, i, j, m, n)
            
            if current_value > maximum_value:

                maximum_value = current_value
    
    return maximum_value

result = snake_sequence([[9, 6, 5, 2], [8, 7, 6, 5], [7, 3, 1, 6], [1, 1, 1, 7]])
print(result)

print()

result = snake_sequence([[7, 5, 2, 3, 1], [3, 4, 1, 4, 4], [1, 5, 6, 7, 8], [3, 4, 5, 8, 9], 
[3, 2, 2, 7, 6]])
print(result)
