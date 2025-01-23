class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # If the grid is empty return 0
            return 0

        # As seen in the input each row is its own array, the columns are the length of an individual array
        rows, cols = len(grid), len(grid[0])
        visit = set() # sets are good for visit lists because they're unordered and don't allow duplicates, can be sure that each element is unique.
        islands = 0



        def bfs(r, c):
            q = collections.deque() # we use a queue for bfs
            visit.add((r,c)) # we add the initial node to the visit list and the queue
            q.append((r,c))

            while q: #while there is an element in the queue
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0, - 1]] 

                for dr, dc in directions: # iterates through the list of directions
                    r, c = row + dr, col + dc
                    if (r in range(rows) and
                    c in range(cols) and grid[r][c] == "1"
                    and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r, c))


        for r in range(rows):
            for c in range(cols): #basically goes through every column in every row
                if grid[r][c] == "1" and (r,c) not in visit: # this cam only happen if it a new island as it would've been visited by a previous node's BFS if it was connected to something else
                    bfs(r, c)
                    islands += 1
        if not islands:
            return 0
        else:
            return max(islands)