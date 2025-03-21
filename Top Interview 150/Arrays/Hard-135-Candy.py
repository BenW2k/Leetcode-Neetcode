class Solution:
    def candy(self, ratings: List[int]) -> int:
        # each child 1 candy
        # children with higher rating get more candy
        # return min number of candy given to each child
        if len(ratings) <= 1:
            return 1
        i = 1
        candies = [1] * len(ratings)

        #first pass
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # second pass
        for i in range(len(ratings)-2, -1, -1):
            print(i)
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)
        
        print(candies)
        return sum(candies)
