def all_true(tuplex):
    for i in tuplex:
        if i == False:
            return False
    return True
        

user_input = input("Write a tuple of numbers: ")
x = tuple(map(int, user_input.split()))
print(all_true(x))
