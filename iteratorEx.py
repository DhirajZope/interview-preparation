class RangeIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            current = self.start
            self.start += 1
            return current
        else:
            raise StopIteration

# ran = RangeIterator(0, 10)
it = iter(RangeIterator(0, 10))
print(next(it))
print(next(it))
