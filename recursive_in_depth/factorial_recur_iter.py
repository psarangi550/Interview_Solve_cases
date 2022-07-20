fact = 1
import os

def func(num):
    global fact
    fact = num
    while True:
        if num == 1:
            fact *= 1
            break
        else:
            fact *= num - 1
        num -= 1
    return fact


if __name__ == "__main__":
    print(func(5))
