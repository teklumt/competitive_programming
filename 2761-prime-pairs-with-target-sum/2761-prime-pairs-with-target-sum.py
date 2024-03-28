class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        prime = []
        check = [True] * (n + 1)
        check[0] = False
        if len(check) > 1:
            check[1] = False
        check[-1] = False
        m =  2
        i = 2

        while i < n:
            if check[i]:
                prime.append(i)
                m = i * i
                while m < n:
                    check[m] = False
                    m += i
            i += 1
        seen = set()
        num = Counter(prime)
        res = []
        # print(prime)
        for i in prime:

            if n - i in num:
                tar =[min(i, n - i), max(i, n-i)]
                if tuple(tar) not in seen:
                    res.append(tar)
                    seen.add(tuple(tar))
        return res



        