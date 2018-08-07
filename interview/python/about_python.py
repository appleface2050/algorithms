
def instance1():
    def createGenerator():
        for i in range(10):
            yield i*i
    a = createGenerator()
    for i in a:
        print i



if __name__ == '__main__':
    instance1()

