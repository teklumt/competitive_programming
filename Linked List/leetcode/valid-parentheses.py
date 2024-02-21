class Solution:
    def isValid(self, s: str) -> bool:
        left=['{','(','[']
        right=['}',')',']']

        le=[]
        # re=[]
        for i in s:
            if i in left:
                le.append(i)
            else:
                if le:
                    if left.index(le.pop()) != right.index(i):
                        return False
                else:
                    return False
        return True if len(le)==0 else False
        