class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        count = 0
        if len(words1) < len(words2):
            for i in words1:
                if words1.count(i) == words2.count(i) and words2.count(i) == 1:
                    count += 1
        else:
            for i in words2:
                if words1.count(i) == words2.count(i) and words2.count(i) == 1:
                    count += 1
        return count
