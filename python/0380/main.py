import random


class RandomizedSet:

    def __init__(self):
        self.dct = {}
        self.lst = []
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.dct:
            return False
        self.dct[val] = self.i
        self.lst.append(val)
        self.i += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.lst:
            return False
        last = self.lst[-1]
        i = self.dct[val]
        self.lst[i] = last
        self.i -= 1
        self.lst.pop()
        self.dct[last] = i
        del self.dct[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
