class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minn=min(start,destination)
        maxx=max(start,destination)
        ss1=sum(distance[minn:maxx])
        ss2=sum(distance[:minn])+sum(distance[maxx:])
        return min(ss1,ss2)