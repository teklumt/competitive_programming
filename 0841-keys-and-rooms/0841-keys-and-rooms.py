class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        queue = deque([0])
    
        while queue:
            currRoom = queue.popleft()
            for key in rooms[currRoom]:
                if key not in seen:
                    queue.append(key)
            seen.add(currRoom)
        return len(seen) == len(rooms)

        