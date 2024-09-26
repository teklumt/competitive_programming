class MyCalendar:

    def __init__(self):
        self.books = []
        

    def book(self, start: int, end: int) -> bool:
        Flag = True
        for l , r in self.books:
            if l <= start  < r  or start <= l  < end:
                Flag = False
                break
        if Flag:self.books.append((start, end))        
        return Flag


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)