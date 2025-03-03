class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
    

from collections import deque
class Solution:
    def removeStars(self, s: str) -> str:
        stack = deque()

        for i, char in enumerate(s):
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)