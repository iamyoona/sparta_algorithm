class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    # [자갈] -> [밀가루] -> [흑연] 사이에 뭘 넣고싶으면 연결 노드를 끊어줘야됨
    # 끊어주고, 원래 이어져있던 애를 임시로 저장해둬야함
    def add_node(self, index, value):

        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index-1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node


linked_list = LinkedList(5)
linked_list.append(12)
#print(linked_list.get_node(1).data)  # -> 5를 들고 있는 노드를 반환해야 합니다!
#linked_list.print_all()
linked_list.add_node(1, 8)
linked_list.print_all()