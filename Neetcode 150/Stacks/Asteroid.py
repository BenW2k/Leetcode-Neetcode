from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = deque() # using deque for faster operations than list

        for i, val in enumerate(asteroids): # enumeration not 100% necessary
            while stack and stack[-1] > 0 and val < 0: # if the stack has things in it, the top of the stack is positive and the val is less than 0
                # basically the above is defining conditions for comparison
                if stack[-1] + val < 0: # If the astroid from the list wins, pop the stack
                    stack.pop()
                elif stack[-1] + val > 0: # If the stack wins we break out of the current loop
                    break
                else: # the final condition is if they're equal, needs to be separate to first condition because the asteroids collide and there are no more comparisons for the current asteroid
                    stack.pop()
                    break
            else: stack.append(val) # while else loop - interesting, if the collision conditions aren't met then we know its a positive rock, add it to stack
        return list(stack) #deque objects returns are objects, so we need to convert them to a list then return it