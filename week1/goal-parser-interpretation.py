class Solution:
    def interpret(self, command: str) -> str:
        res=""
        i=0
        while i<len(command):
            if command[i]!='(':
                res+=command[i]
                i+=1
            else:
                num=""
                i=i+1
                while command[i]!=')':
                    num+=command[i]
                    i+=1
                if num=="":
                    res+='o'
                else:
                    res+=num
                i+=1
        return res