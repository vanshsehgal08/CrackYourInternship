import random

class RandomizedCollection(object):

    def __init__(self):
        self.numMap = {}  # Maps value to a set of indices
        self.numList = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val not in self.numMap
        if res:
            self.numMap[val] = set()
        self.numMap[val].add(len(self.numList))
        self.numList.append(val)
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.numMap or not self.numMap[val]:
            return False

        # Remove an index of the element to remove
        idx = self.numMap[val].pop()
        lastVal = self.numList[-1]

        # Move the last element to the place of the element to remove
        self.numList[idx] = lastVal

        # Update the map for the last element
        self.numMap[lastVal].add(idx)
        self.numMap[lastVal].discard(len(self.numList) - 1)

        # Remove the last element from the list
        self.numList.pop()

        # Clean up the map if necessary
        if not self.numMap[val]:
            del self.numMap[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.numList)
        

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
