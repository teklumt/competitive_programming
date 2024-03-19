class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        val = list(count.values())
        maxx = max(val)
        MaxCount = val.count(maxx)

      
        nn = n * (maxx - 1) + maxx              
        mm = MaxCount - 1

              
        return max(nn + mm , len(tasks))