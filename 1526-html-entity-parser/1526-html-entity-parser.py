class Solution:
    def entityParser(self, text: str) -> str:
        mymap  = { "&quot;": '"',  "&apos;":"'", "&amp;": '&',  "&gt;":'>', "&lt;":"<", "&frasl;":"/" }
        res = ""
        temp = ""
        for i in text:
            if  temp:
                if i == ';':
                    temp += i
                    res += mymap[temp] if temp in mymap else temp
                    temp = ""
                elif i == '&':
                    res += temp
                    temp = "&"
                else:
                    temp += i
            elif i == '&':
                temp += i
            else:
                res += i

        return res + (mymap[temp] if temp and temp in mymap else temp)