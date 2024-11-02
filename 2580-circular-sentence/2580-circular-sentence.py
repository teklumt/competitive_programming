class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        st = sentence.split(" ")
        flag = True
        for i in range(len(st) - 1):
            if st[i][-1] != st[i + 1 ][0]:
                flag = False
                break
        if st[-1][-1] != st[0][0]:
            flag = False 

        return flag