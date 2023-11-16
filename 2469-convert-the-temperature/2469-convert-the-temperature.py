class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        result=[]
        result.append(celsius + 273.15)
        result.append(celsius*1.8 +32.00)
        return result