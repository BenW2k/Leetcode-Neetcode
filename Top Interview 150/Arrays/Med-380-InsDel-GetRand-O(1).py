class RandomizedSet:
    from random import choice

    def __init__(self):
        self.map = {} #initialising a map, not using a set so we can search kv pairs at O(1)
        self.list = [] # using a list to use the random func
        
        

    def insert(self, val: int) -> bool:
        if val in self.map: # if val is already in the map we return false
            return False
        else:
            self.map[val] = len(self.list) # add the num to the hash map with its value being the index its stored in the list
            self.list.append(val) # add to the end of the list
            return True

        

    def remove(self, val: int) -> bool:
        if val not in self.map: # return false if the element isnt in the map
            return False
        else:
            index = self.map[val] # we access the index at which the num is stored by using the kv pair of the map O(1)
            lastVal = self.list[-1] # This accesses the last index of the list
            self.list[index] = lastVal # we overwrite the element we want to delete with the last val of the list
            self.list.pop() # we then delete the last val
            self.map[lastVal] = index # we now change the index value of the last element we moved to the index of the element we deleted
            del self.map[val] # then we delete the element we wanted to delete from the map too
            return True # and return true
        

    def getRandom(self) -> int:
        return random.choice(self.list) # we just return a random item from the list using a built in function


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()