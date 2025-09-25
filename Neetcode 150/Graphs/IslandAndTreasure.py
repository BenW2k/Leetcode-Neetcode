class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen_set = set()
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def dfs(r,c, dist):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] < dist:
                return
            grid[r][c] = dist
            for dr, dc in directions:
                dfs(r + dr, c + dc, dist + 1)
                        
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and (r,c) not in seen_set:
                    seen_set.add((r, c))
                    for dr, dc in directions:
                        dfs(r + dr, c + dc, 1)