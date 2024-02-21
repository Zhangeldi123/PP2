class MyNumbers:
    def __iter__(self):
      self.a = 0
      return self
    def __next__(self):
       x = self.a
       self.a += 2
       return x

myclass = MyNumbers()
myiter = iter(myclass)

user_input = int(input("Enter the value that will define the top: "))

for i in range(0, user_input):
   if i % 2 == 0:
      print(next(myiter))


