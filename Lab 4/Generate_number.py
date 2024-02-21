class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a * self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

user_input = int(input("Enter the number of iterations: "))

for _ in range(user_input):
    print(next(myiter))