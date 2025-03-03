class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char != "*":
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)