class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        left = 0
        right = len(people) - 1
        while left <= right:
            if people[left]  + people[right] <= limit:
                res +=1
                right -= 1
                left += 1
            else:
                res += 1
                right -= 1
        return res