#coding=utf-8

def abc(a):
    def my_dec(func):
        print a
        def wrapper(number, *args, **kwargs):
            # print "abc"
            func(number)
            print "args", args
            print "kwargs" , kwargs
            # print "dcf"
        return wrapper
    return my_dec

@abc(1)
def print_(number):
    print number




def dec2(func):
    def dec_(number):
        print "inner dec"
        obj = func(number)
        return obj
    return dec_

@dec2
def print2(number):
    print number
    return number


def gen():
    for i in range(10):
        yield i



def fib_gen(max):
    n, a, b = 0, 0, 1
    while(n < max):
        yield b
        a, b = b, a+b
        n += 1

if __name__ == '__main__':
    # print_(123, 456, a=1, b=2)
    result = print2(100)
    print result
    # for i in gen():
    #     print i

    # for i in fib_gen(20):
    #     print i
