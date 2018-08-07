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

@abc(100)
def print_(number):
    print number


if __name__ == '__main__':
    print_(123, 456, a=1, b=2)
