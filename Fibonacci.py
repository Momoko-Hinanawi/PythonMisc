#input a non-negative integer n and press enter
#then the program will output the first nth terms of Fibonacci sequence
#***This is my first python program!!!***
def Fibonacci():
    times =int(input())
    print("-----------------")
    i = 2
    a = 1
    b = 1 
    if times == 0:
        pass
    elif times == 1:
        print(1)
    elif times == 2:
        print(1)
        print(1)
    else:
        print(1)
        print(1)
        i = 2
        while i < times:
            c = a + b
            print(c)
            a = b
            b = c
            i = i + 1
        pass
    pass
    print("-----------------")
pass

while True:
    Fibonacci()
pass