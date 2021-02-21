'''
Question:
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically.
The grid is completely surrounded by water, and there is exactly one island.
The island doesn't have "lakes". One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.
'''


def islandPerimeter(self, grid: List[List[int]]) -> int:

    H, W = len(grid), len(grid[0])
    perimeter = 0

    for h in range(H):
        for w in range(W):
            if grid[h][w]:
                perimeter += 4
                if h < H - 1 and grid[h+1][w]:
                    perimeter -= 2
                if w < W - 1 and grid[h][w+1]:
                    perimeter -= 2
    return perimeter
