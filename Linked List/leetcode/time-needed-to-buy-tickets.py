class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res=0

        while tickets[k]>0:

            for i in range(len(tickets)):

                if tickets[i]>0:
                    res+=1
                    tickets[i]-=1
                    if tickets[k]==0:
                        break
        # print(tickets)
        return res
                
        