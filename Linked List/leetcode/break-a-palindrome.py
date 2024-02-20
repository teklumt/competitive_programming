class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        pali=list(palindrome)
        pa=pali.count('a')
        a=pa
        if len(set(pali))==1 and pali[0]=='a':
            pali[-1]='b'
            return "".join(pali)
        for i in range(len(pali)):
            if pali[i]!='a':
                if pa+1==len(pali):
                    if a==pa//2:
                        pali[-1]='b'
                    else:
                        pali[i]='a'
                else:
                        pali[i]='a'

                return "".join(pali)
          
            a-=1
