class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myhash = {}
        myhash2 = {}
        for i in magazine:
            if i in myhash:
                myhash[i] += 1
            else:
                myhash[i] = 1
        for i in ransomNote:
            if i in myhash2:
                myhash2[i] += 1
            else:
                myhash2[i] = 1
        for i in myhash2:
            if i not in myhash or myhash2[i] > myhash[i]:
                return False
        return True
                