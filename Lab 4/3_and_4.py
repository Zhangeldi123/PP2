class MyDivisibleNumbers:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            x = self.current
            self.current += 12 
            return x
        else:
            raise StopIteration

user_input = int(input("Enter the value that will define the top: "))
myclass = MyDivisibleNumbers(user_input)
myiter = iter(myclass)

for _ in range((user_input + 1) // 12):
    print(next(myiter))