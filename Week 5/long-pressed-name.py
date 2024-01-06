class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        hash1={}
        hash2={}
        name1=[]
        name2=[]
        win=[]
        j=0
        for i in name:
            if win:
                if i ==win[-1]:
                    win.append(i)
                else:
                    hash1[j]=len(win)
                    name1.append(win[-1])
                    win=[i]
                    j+=1
            else:
                win.append(i)
        if win:
            hash1[j]=len(win)
            name1.append(win[-1])
        win=[]
        m=0
        for i in typed:
            if win:
                if i ==win[-1]:
                    win.append(i)
                else:
                    hash2[m]=len(win)
                    name2.append(win[-1])
                    win=[i]
                    m+=1
            else:
                win.append(i)
        if win:
            hash2[m]=len(win)
            name2.append(win[-1])
        i=0
        l=0
        while i<len(hash1) and l<len(hash2):
            if name1[i]!=name2[l] or hash1[i]>hash2[l]:
                return False
            i+=1
            l+=1

        return True if len(hash1)==len(hash2) else False

        