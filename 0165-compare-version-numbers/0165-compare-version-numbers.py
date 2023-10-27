class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        Version1list=version1.split('.')
        Version2list=version2.split('.')
        n=len(Version1list)
        m=len(Version2list)
        if n>m:
            Version2list+=['0']*(n-m)
        elif m>n:
            Version1list+=['0']*(m-n)
        for i in range(len(Version1list)):
            if int(Version1list[i])<int(Version2list[i]):
                return -1
            elif int(Version1list[i])>int(Version2list[i]):
                return 1
        return 0