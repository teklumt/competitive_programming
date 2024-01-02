class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        
        tasks.sort()
        processorTime.sort(reverse=True)
        res=-inf

        k=math.ceil(len(tasks)//4)
        i=0
        j=-k
      
        while i<len(tasks):
            if i+4 < len(tasks):
                res=max(res,(processorTime[j]+max(tasks[i:i+4])))
            else:
                res=max(res,(processorTime[j]+max(tasks[i:])))

            j+=1
            i+=4

        return res

