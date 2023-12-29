class Solution:
    def sortSentence(self, s: str) -> str:
        
        sent=s.split(" ")
        sent.sort(key=lambda x:x[-1])
        
        return " ".join([i[:-1] for i in sent])