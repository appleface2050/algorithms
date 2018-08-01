class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue(object):
    def __init__(self):
        self.front = None
        self.back = None

    def en_queue(self, value):
        n = Node(value)
        if self.front is None:
            self.front = n
            self.back = n
        else:
            self.back.next = n
            self.back = n

    def de_queue(self):
        if not self.front:
            return None
        else:
            result = self.front
            self.front = self.front.next
        return result.data

    def search(self, value):
        p = self.front
        while p is not None:
            if p.data == value:
                return p.data
            else:
                p = p.next
        return None

    def is_empty(self):
        return self.front is None


if __name__ == '__main__':
    q = Queue()
    q.en_queue(1)
    q.en_queue(2)
    q.en_queue(3)

    print q.search(3)

    print q.de_queue()
    print q.de_queue()
    print q.de_queue()
    print q.de_queue()
