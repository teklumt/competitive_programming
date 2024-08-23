class Solution:
    def fractionAddition(self, expression: str) -> str:
        listed = expression.split("/")

        top = []
        bot = []

        for li in range(len(listed)):
            if li == 0 or li == len(listed) - 1:
                if li == 0:
                    top.append(int(listed[li]))
                else:
                    bot.append(int(listed[li]))

            elif len(listed[li]) == 3:
                bot.append(int(listed[li][:1]))
                top.append(int(listed[li][1:]))
            else:
                temp = ""
                last = li
                for i in range(len(listed[li])):
                    if listed[li][i].isdigit():
                        temp += listed[li][i]
                    else:
                        last = i
                        break
                
                bot.append(int(temp))
                top.append(int(listed[li][last:]))
        botM = 1
        for i in bot:
            botM *= i
        topM = 0
        for i in range(len(top)):
            topM += ( botM // bot[i] ) * top[i]
        
        common = gcd(int(topM), int(botM))
        if topM == 0:
            return "0/1"
        return f"{topM // common}/{botM // common}"
