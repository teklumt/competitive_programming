class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        str_in=list(s)
        be=0
        res=""

        while be<len(str_in):
            if be+2*k < len(s):
                pre = str_in[be:be+2*k]
                rr=pre[:k]
                res+="".join(reversed(rr))+"".join(pre[k:])
                be=be+2*k
            else:
                pre = str_in[be:]
                rr=pre[:k]
                res+="".join(reversed(rr))+"".join(pre[k:])
                be+=len(pre)
        return res