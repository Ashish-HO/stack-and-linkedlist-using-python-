class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None

    def InsertAtBegining(self, data):
        node = Node(data, self.head)
        self.head = node

    def InsertAtEnd(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)
        pass

    def display(self):
        if self.head == None:
            print("Linked list is empty")

        itr = self.head
        while itr:
            print(itr.data, end="->")
            itr = itr.next

    def RemoveLastNode(self):
        if self.head == None:
            print("linked list is empyt")
            return

        itr = self.head
        while itr.next.next:
            itr = itr.next
        itr.next = None

    def RemoveFirstNode(self):
        if self.head == None:
            print("linked list is empyt")
            return

        itr = self.head
        self.head = itr.next

    def InsertDataList(self, data_list):
        for data in data_list:
            linked_list.InsertAtEnd(self, data)

    def LinkedListLength(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count


ll = linked_list()
# ll.InsertAtBegining(2)
# ll.InsertAtBegining(12)
# ll.InsertAtBegining(1)
# ll.InsertAtEnd(90090)
# ll.RemoveFirstNode()
# ll.RemoveLastNode()
# ll.RemoveLastNode()
ll.InsertDataList(["name", "age", "address", "phone", "email"])
print(ll.LinkedListLength())
ll.display()
