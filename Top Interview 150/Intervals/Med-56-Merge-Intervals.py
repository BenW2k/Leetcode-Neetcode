class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Solution whereby you're sorting the intervals by their first value
        # We want to then check if the end of the last interval is greater than the start of the current interval - this shows its overlapping.
        # we'll then merge the intervals using the max function and append it to output
        # or we'll append the non-overlapping interval to output
        # We get the intuition by seeing that we should have the ranges sorted to avoid any of the other shenanigans
        
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output