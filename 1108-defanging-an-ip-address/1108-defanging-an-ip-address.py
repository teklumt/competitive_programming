class Solution:
    def defangIPaddr(self, address: str) -> str:
        stack=""
        for i in address:
            if i==".":
                stack+="[.]"
            else:
                stack+=i
        
        return f"{stack}"
            