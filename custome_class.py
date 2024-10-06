class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current == 0:
            self.current += 1
            return {'length': self.length}
        elif self.current == 1:
            self.current += 1
            return {'width': self.width}
        else:
            raise StopIteration  

obj = Rectangle(10, 5)

for dimension in obj:
    print(dimension)