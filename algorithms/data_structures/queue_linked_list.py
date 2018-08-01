
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.tail = None

    def isEmpty(self):
        return self.front == None

    def EnQueue(self, item):
        n = Node(item)
        if self.tail is None:
            self.front = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n

    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.tail = None
        return str(temp.data)


# Driver Code
if __name__ == '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.EnQueue(6)
    q.EnQueue(7)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)

    print("Dequeued item is " + q.DeQueue())
