import time
import math

def delayed_square_root(number, milliseconds):
    
    time.sleep(milliseconds / 1000)
    
    
    result = math.sqrt(number)
    
    return result


number = int(input("Enter a number: "))
milliseconds = int(input("Enter the delay in milliseconds: "))


result = delayed_square_root(number, milliseconds)


print(f"Square root of {number} after {milliseconds} milliseconds is {result}")
