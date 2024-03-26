class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:

        Aset = set()
        Bset = set()
        res = []
        for i in range(len(A)):
            Aset.add(A[i])
            Bset.add(B[i])

            res.append(len(Aset & Bset))
        return res




        