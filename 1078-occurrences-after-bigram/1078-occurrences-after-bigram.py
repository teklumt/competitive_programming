class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        dem = text.split(" ")
        res =[]
        for i in range(len(dem)-2):
            if dem[i] == first and dem[i+1] == second:
                res.append(dem[i+2])

        
        return res