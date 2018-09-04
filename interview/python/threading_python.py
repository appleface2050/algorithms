import threading
import time

thread_lock = threading.Lock()

class A(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id


    def run(self):
        thread_lock.acquire()
        for i in range(10):
            print self.id, i
            time.sleep(0.5)
        # thread_lock.release()

if __name__ == '__main__':
    a = A("a")
    b = A("b")
    a.start()
    b.start()
    b.join()
    # a.join()
    print "finish"