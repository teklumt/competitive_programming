class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        queue=deque()
        for i in trainers:
            queue.append(i)
        count=0
        for i in players:
            flag=True
            while flag and queue:
                n=queue.popleft()
                if n>=i:
                    count+=1
                    break
        return count

