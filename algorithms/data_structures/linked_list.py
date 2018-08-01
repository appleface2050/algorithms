# coding=utf-8

# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Node:
    def __init__(self,cargo = None, next = None):
        self.cargo = cargo
        self.next = next

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        #功能：输入头节点，返回链表长度
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insertToFront(self,data):
        #功能：输入data，插入到头节点前，并更改为头节点
        #输出：当前头节点
        if data is None:
            return None
        node = Node(data,self.head)
        self.head = node
        return node

    def append(self,data):
        #功能：输入data,作为节点插入到末尾
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self,data):
        #功能：查找链表的节点data与data相同的节点
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            else:
                curr_node = curr_node.next
        return None

    def delete(self,data):
        #删除节点
        if data is None:
            return None
        if self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
                curr_node = curr_node.next

    def deleteAlt(self, data):
        #只定义一个变量来完成删除操作
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        curr_node = self.head
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

if __name__ == '__main__':
    node1 = Node(1)
