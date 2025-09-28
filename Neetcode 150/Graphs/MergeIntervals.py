class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]  # start with first interval

        for start, end in intervals[1:]:
            # compare with last interval in output
            if start <= output[-1][1]:
                # merge
                output[-1][1] = max(output[-1][1], end)
            else:
                # no overlap, add new interval
                output.append([start, end])

        return output