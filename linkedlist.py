class Node:

    def __init__(self, data):

        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):

        self.head = None

    def push(self, new_data):

        new_node = Node(new_data)

        # new_node.next = self.head

        new_node.next = None

        self.head = new_node

    def search(self, x):

        current = self.head

        while(current != None):

            if current.data == x:
                return True
            current = current.next

        return False


if __name__ == '__main__':

    ll = LinkedList()

    ll.push(1)
    ll.push(13)
    ll.push(19)
    ll.push(20)
    ll.push(22)

    if ll.search(22):
        print("woo")
    else:
        print("ftsa")
