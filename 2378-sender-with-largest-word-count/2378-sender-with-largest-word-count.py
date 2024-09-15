class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        mapp = Counter()
        for i in range(len(senders)):
            mapp[senders[i]] += len(messages[i].split(" "))
        maxx = []
        name , maxi = mapp.most_common(1)[0]
        for i in mapp:
            if mapp[i] == maxi:
                maxx.append(i)
        return max(maxx)
