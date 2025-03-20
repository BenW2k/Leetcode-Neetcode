class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # cost[i] to get to next station
        # start at one of the stations with 0 gas
        # can only travel clockwise, return starting station index if solution, return -1 if no solution
        # only 1 possible solution if there is one
        # brute force n^2 - check if its possible from every point, return if solution else -1

        if sum(cost) > sum(gas):
            return -1

        tank = idx = 0
        
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank, idx  = 0, i+1

        return idx