class CountdownIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n >= 0:
            result = self.n
            self.n -= 1
            return result
        else:
            raise StopIteration

user_input = int(input("Enter a value: "))
myiter = CountdownIterator(user_input)

for _ in range(user_input + 1):
    print(next(myiter))