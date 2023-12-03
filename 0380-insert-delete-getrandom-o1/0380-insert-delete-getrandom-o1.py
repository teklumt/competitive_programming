class RandomizedSet:

    def __init__(self):
        self.myhash={}
        self.mylist=[]
        

    def insert(self, val: int) -> bool:
        if val in self.myhash:
            return False
        else:
            self.myhash[val]=1
            self.mylist.append(val)
            return True

        

    def remove(self, val: int) -> bool:
        if val not in self.myhash:
            return False
        else:
            del self.myhash[val]
            return True
        

    def getRandom(self) -> int:
        random_num = random.choice(list(self.myhash.keys()))
        return random_num



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()