class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        island_count = 0

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    island_count += 1
                    self.explore_island(grid, row, col, visited)

        return island_count

    def explore_island(self, grid, start_row, start_col, visited):
        num_rows = len(grid)
        num_cols = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        stack = [(start_row, start_col)]
        visited.add((start_row, start_col))

        while stack:
            row, col = stack.pop()
            for row_change, col_change in directions:
                next_row = row + row_change
                next_col = col + col_change
                if (0 <= next_row < num_rows and 0 <= next_col < num_cols
                        and grid[next_row][next_col] == "1"
                        and (next_row, next_col) not in visited):
                    visited.add((next_row, next_col))
                    stack.append((next_row, next_col))