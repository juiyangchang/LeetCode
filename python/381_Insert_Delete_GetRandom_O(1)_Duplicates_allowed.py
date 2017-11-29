from collections import defaultdict
from random import randint

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = defaultdict(list)
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.nums.append(val)
        ret_val = (val in self.pos)
        self.pos[val].append(len(self.nums)-1)
        return ret_val     

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            last_no = self.nums[-1]
            self.nums[-1], self.nums[self.pos[val][-1]] = val, last_no
            self.pos[last_no][-1] = self.pos[val][-1]
            self.pos[last_no].sort()
            self.nums.pop()
            if len(self.pos[val]) == 1:
                self.pos.pop(val)
            else:
                self.pos[val].pop()
            return True
        
        return False        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.nums[randint(0, len(self.nums)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()