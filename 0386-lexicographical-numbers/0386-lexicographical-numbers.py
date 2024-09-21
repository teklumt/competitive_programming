class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return (map(int ,sorted([str(i) for i in range(1, n + 1)])))