class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        def BitCount(n, hashs):
            i = 0
            while i < n.bit_length():
                hashs[i] +=( (1 << i) & n )!=0
                i += 1 
               
        count = Counter()
        cCount = Counter()
        BitCount(a, count)
        BitCount(b, count)
        BitCount(c, cCount)
        res = 0
        keyss = list(count.keys()) if len(count) >= len(cCount) else list(cCount.keys())
        for i in keyss:
            if cCount[i] == 0:
                res += count[i]
            elif count[i] == 0:
                res += 1
   
        return res
        
        
        
#         i = 0
        
#         while i < a.bit_length():
#             count[i] +=( (1 << i) & a )!=0
#             i += 1 
#         i = 0
#         while i < b.bit_length():
#             count[i] += ((1 << i) & b) != 0
#             i += 1 
#         cCount = Counter()
#         i = 0
#         while i < c.bit_length():
#             cCount[i] += ((1 << i) & c) != 0
#             i += 1
#         res = 0
#         keyss = list(count.keys()) if len(count) >= len(cCount) else list(cCount.keys())
#         for i in keyss:
#             if cCount[i] == 0:
#                 res += count[i]
#             elif count[i] == 0:
#                 res += 1
   
#         return res
            
