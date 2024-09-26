class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1, event2 = sorted([event1, event2])
        if event1[0] <= event2[0] <= event1[1] or event2[0] <= event1[0] <= event2[0]:
            return True
        return False
        # if event2[0] <