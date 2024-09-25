import random

class RandomizedSet:

    def __init__(self):
        self.my_set = []
        self.seen = {}

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        
        self.my_set.append(val)
        self.seen[val] = len(self.my_set) - 1
        
        return True

    def remove(self, val: int) -> bool:
        if val in self.seen:
            remove_idx = self.seen[val]
            last_element = self.my_set[-1]
            self.my_set[remove_idx] = last_element
            self.seen[last_element] = remove_idx

            self.my_set.pop()
            del self.seen[val]

            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.my_set)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()