class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        counting=[0]*(max(costs)+1)
        output=[]
        for i in costs:
            counting[i]+=1
        for i in range(len(counting)):
            output+=[i]*counting[i]
        for i in range(len(output)):
            if coins>0 and coins>=output[i]:
                coins-=output[i]
            else:
                return i
        return len(output)
        