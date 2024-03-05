with open('Hello.txt', 'r') as x, open('World.txt', 'w') as y:
    ada = x.read()
    y.write(ada)