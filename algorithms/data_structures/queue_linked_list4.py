class Node:
    def __init__(self, value):
        self.data = value
        self.front = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def en_queue(self, value):
        new_node = Node(value)

        if self.tail is not None:
            # make the front attribute of old node point to new node
            self.tail.front = new_node

        else:
            # if first ever node in Queue both front and tail will point to it
            self.head = new_node

        self.tail = new_node
        self.count += 1

    def de_queue(self):
        if not self.is_empty():
            # point head to next node
            self.head = self.head.front
            print("sucess")
            self.count -= 1
        else:
            print("Empty QUEUE")

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.front

    def is_empty(self):
        if self.head is None and self.tail is None:
            return True
        else:
            return False

    def peek_front(self):
        return self.head.data

    def peek_back(self):
        return self.tail.data

    def queue_search(self, value):
        # start from the head
        p = self.head
        while p is not None:
            # make p reference to next node
            if p.front is not None:
                if p.data == value:
                    print("Found value")
                    return p.data
                p = p.front
            else:
                print("fail")
                return 0


    def length(self):
        return self.count

if __name__ == '__main__':
    my_queue = Queue()
    test_list = [1, 2, 3, 4, -2000000, 'a', 500000, 50]

    for i in test_list:
        my_queue.en_queue(i)