class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefixSum=[0]*n
        for book in bookings:
            prefixSum[book[0]-1]+=book[-1]
            if book[1]<n:
                prefixSum[book[1]]-=book[-1]
        for i in range(1,len(prefixSum)):
            prefixSum[i]+=prefixSum[i-1]
        return prefixSum