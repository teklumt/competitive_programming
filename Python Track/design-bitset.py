class Bitset:

    def __init__(self, size: int):

        self.bitset = ['0']*size
        self.size = size
        self.store = {0: set(x for x in range(size)), 1: set()}

    def fix(self, idx: int) -> None:
        self.store[0].discard(idx)
        self.store[1].add(idx)

    def unfix(self, idx: int) -> None:
        self.store[1].discard(idx)
        self.store[0].add(idx)

    def flip(self) -> None:
        self.store[1], self.store[0] = self.store[0], self.store[1]

    def all(self) -> bool:
        return len(self.store[1]) == self.size

    def one(self) -> bool:
        return len(self.store[1]) >= 1

    def count(self) -> int:

        return len(self.store[1])

    def toString(self) -> str:

        for i in (self.store[1]):
            self.bitset[i] = '1'
        for i in (self.store[0]):
            self.bitset[i] = '0'
        return "".join(self.bitset)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()