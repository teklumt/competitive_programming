class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        newNum = sorted([i % value for i in nums ])
        count = Counter()
    
        res = []
        for i in newNum.copy():
            if i in count:
                res.append(i +  count[i] * value)
            count[i] += 1
        newNum = sorted(list(set(newNum)) + res)

        for i  in range(len(newNum)):
            if i != newNum[i]:
                return i 
        return len(newNum) 