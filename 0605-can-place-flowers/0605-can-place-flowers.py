class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i > 0:
                    if flowerbed[i - 1] == 0:
                        if i < len(flowerbed) - 1:
                            if flowerbed[i + 1] == 0:
                                res += 1
                                flowerbed[i] = 1
                        else:
                            res += 1
                            flowerbed[i] = 1
                else:
                    if i < len(flowerbed) - 1:
                        if flowerbed[i + 1] == 0:
                            res += 1
                            flowerbed[i] = 1
                    else:
                        res += 1
                        flowerbed[i] = 1
        return res >= n
