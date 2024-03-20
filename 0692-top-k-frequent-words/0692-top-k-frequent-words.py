class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        maxx = max(count.values())
        res = [set() for _ in range(maxx)]
        for i in words:
            res[count[i] - 1].add(i)
        res = res[::-1]
        num = []
        for i in range(len(res)):
            num += sorted(res[i])
        return num[:k]
