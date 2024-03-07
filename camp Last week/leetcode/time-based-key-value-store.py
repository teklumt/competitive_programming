class TimeMap:

    def __init__(self):
        self.hash = {}
        self.hash2 = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[(key, timestamp)] = value
        self.hash2[key].append(timestamp) 
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash2:
            return ""
        else:
            num  = self.hash2[key]

            ind = bisect_left(num, timestamp)
            if ind >= len(num):
                return self.hash[(key, num[-1])]
            elif ind == 0:
                if num[ind]  == timestamp:
                    return self.hash[(key, num[0])]
                else:
                    return ""
            else:
                if num[ind]  <= timestamp:
                    return self.hash[(key, num[ind])]
                else:
                    return self.hash[(key, num[ind - 1])]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)