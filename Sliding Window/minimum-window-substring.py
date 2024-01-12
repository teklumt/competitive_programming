class Solution:
    def minWindow(self, s: str, t: str) -> str:
            if len(t)>len(s):
                return ""

            def check(word_count1,word_count2):
                if len(word_count1)!=len(word_count2):
                    return False
                for i in word_count2:
                    if word_count2[i]<word_count1[i]:
                        return False
                return True

            Tcount=Counter(t)
            temp=Counter()
            result=deque()
            min_length=len(s)+1
            window=deque(s[:len(t)])



            for i in range(len(t)):
                if s[i] in Tcount:
                    temp[s[i]]+=1

            if Tcount == temp:
                return s[:len(t)]
            
            for i in range(len(t),len(s)):
                
                window.append(s[i])
                if s[i] in Tcount:
                    temp[s[i]]+=1

                if check(Tcount,temp) and len(window)<min_length:
                    result=window.copy()
                    min_length=len(window)            
                    
                while window and check(Tcount,temp):
                    if check(Tcount,temp) and len(window)<min_length:
                        result=window.copy()
                        min_length=len(window)
                    if window[0] in temp:
                        temp[window[0]]-=1
                    window.popleft()
                    
            
            while window and check(Tcount,temp):
                if len(window)<len(result):
                    result=window.copy()
                if window[0] in temp:
                    temp[window[0]]-=1
                window.popleft()

            return "".join(result)