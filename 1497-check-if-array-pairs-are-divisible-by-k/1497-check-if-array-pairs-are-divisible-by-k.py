class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash = defaultdict(int)
        for i in arr:
            hash[i % k] += 1
    
        for i in hash:
            
            if i != 0 and hash[k - i] != hash[i]:
                return False
            if i == 0 and hash[i] % 2:
                return False
        return True


