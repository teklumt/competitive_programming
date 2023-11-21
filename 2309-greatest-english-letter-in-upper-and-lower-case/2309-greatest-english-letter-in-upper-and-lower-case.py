class Solution:
    def greatestLetter(self, s: str) -> str:
        store = []
        for i in s:
            if i.isupper() and i.lower() in s:
                store.append(i)
        store.sort()
        return store[-1] if store else ""
