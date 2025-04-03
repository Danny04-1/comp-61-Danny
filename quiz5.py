def sum_region(grid):
    return sum(sum(row) for row in grid)

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum_region(grid))  

# this function would add up all of the rows in the grid. It then prints 45 because I put the sum() around the whole thing so it added all the rows up to get 45. 


