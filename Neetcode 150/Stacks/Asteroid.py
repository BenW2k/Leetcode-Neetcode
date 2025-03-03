from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque()

        for i, val in enumerate(asteroids):
            while stack and stack[-1] > 0 and val < 0:
                if stack[-1] + val < 0:
                    stack.pop()
                elif stack[-1] + val > 0:
                    break
                else:
                    stack.pop()
                    break
            else: stack.append(val)
        return list(stack)