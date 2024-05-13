import collections

def isAnagram(s, t):
    map = collections.defaultdict(int)

    for char in s:
        map[char]+=1
    for char in t:
        map[char]-=1
    
    for val in map.values():
        if val != 0:
            return False
    return True
isAnagram(s, t)