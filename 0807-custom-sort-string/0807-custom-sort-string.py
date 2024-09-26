class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_ = defaultdict(int)
        for i in range(len(order)):
            if i not in order_:
                order_[order[i]] = i + 1
        return "".join(sorted(list(s), key= lambda x : order_[x]))