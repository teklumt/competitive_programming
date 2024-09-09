class MapSum:

    def __init__(self):
        self.mapp = defaultdict(int)
        self.root = {"#" : 0, "summ" : 0}
        

    def insert(self, key: str, val: int) -> None:
        self.mapp[key] = val
        cur = self.root
        i = 0
        while i < len(key):
            if key[i] not in cur:
                cur[key[i]] =  {"#" : 0, "summ" : 0}
            cur = cur[key[i]]
            i += 1
        cur["#"] = 1
        cur["summ"] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for chars in prefix:
            if chars not in  cur:
                return 0
            cur = cur[chars]
        
        res = 0
        queue = deque([cur])

        while queue:
            curNode = queue.pop()
            res += curNode["summ"]
            for node in curNode:
                if node != '#' and node != "summ":
                    queue.append(curNode[node])
        return res

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)