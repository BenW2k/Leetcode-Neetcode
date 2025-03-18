class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # max val of h such that h papers have been cited at least h times
        # O(n^2) loop through list for each val, note if valid h val, return highest num
        # sorting the array could be useful 
        n = len(citations)

        # Important no
        paper_counts = [0] * (n+1) # this is an array that shows the count of all num of citations where the last value is a bucket for any val greater than n

        for c in citations: # the number of paper counts for each paper
            paper_counts[min(n, c)] += 1 # we take the minimum of n and c here because if c is greater than n we increment the >=n bucket
        
        h = n # sets h to n for clarity
        papers = paper_counts[n]
        # papers is used to show the number of papers that have at least h notations

        while papers < h: # This is basically saying 'while we havent found a valid h value'
            h -= 1 # we decrement h by 1
            papers += paper_counts[h] # and add the num of papers at h to the total papers seen variable then the loop continues
        
        return h # return the h value