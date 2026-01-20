'''
***Write Up***

This problem involves finding the next hottest day to one at our index.
The result list is to be returned in the order that the temperatures are given
which gives us intuition that we need to be keeping track of the indexes of the days
because if we pop and only rely on stack order for indexes then it quickly becomes
inaccurate.

We use the stack because it is acting as a queue of days that are waiting to find their next
hottest day. Once a day is popped then it'll never have to find its hottest day again so we can just
pop it from the stack.

So we pre-write our res array with 0s and push the days into the stack as a pair with
pair[0] being the temp and pair[1] being the index.

The nature of popping in this problem causes the stack to become monotonic where the
pairs on the stack are always in decreasing order. As such we can just pop from the stack
so long as the stk[-1][0] is less than our current temp.

'''




class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0]*len(temperatures)

        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stackT, stackI = stk.pop()
                res[stackI] = i - stackI
            stk.append((t, i))
        return res