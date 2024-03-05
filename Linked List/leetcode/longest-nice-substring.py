class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def check(strIn):
            count = Counter(strIn)
            # bol = True
          
            for i in count:
                num = ord(i)
              
                if num <= 90:
                    num += 32
                    if chr(num) not in count:
                        
                        return False
                else:
                    num -= 32
                    if chr(num) not in count:
                        
                        return False
            return True

        res = ""
        temp = []
        for i in range(len(s)-1):
            temp = []
            for j in range(i, len(s)):
                temp.append(s[j])
                print(temp)
                if check(temp) and len(temp) > len(res):
                    res = "".join(temp)
        print(check(['a', 'A', 'z', 't', 'T', 'k', 'Z', 'K']))
        return res
                