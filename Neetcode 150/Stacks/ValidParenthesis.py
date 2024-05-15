def isValid(self, s: str) -> bool:
    left = ["(", "{", "["]
    right = [")", "}", "]"]
    map = {")" : "(", "}": "{", "]": "["}
    stack = []
    l=0
    r=0
    if len(s) % 2 != 0:
        return False

            
    for char in s:
        if char in left:
            stack.append(char)
            l+=1
        elif char in right:
            r+=1
            if len(stack) == 0:
                return False
            if map[char] != stack.pop():
                return False
    if r == l:
        return True
    else:
        return False