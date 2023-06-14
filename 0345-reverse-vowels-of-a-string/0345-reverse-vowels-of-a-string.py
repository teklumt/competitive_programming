class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o', "u"]
        num = list(s)
        i = 0
        j = len(s)-1
        while i < j:
            if num[i].lower() in vowel:
                if num[j].lower() in vowel:
                    num[i], num[j] = num[j], num[i]
                    i += 1
                    j -= 1
                else:
                    j = j-1
            else:
                i = i+1
        return "".join(num)