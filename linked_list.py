class OneLinkNode(object):

    def __init__(self, v, n=None, p=None):
        self.value = v
        self._next = n
        self._data = None

    def set_link_to_data(self, data):
        self._data = data
    
    @property
    def next(self):
        if self._next:
            return self._data[self._next]

    @next.setter
    def next(self, value):
        self._next = value


class TwoLinkNode(object):

    def __init__(self, v, n=None, p=None):
        self.value = v
        self.next = n
        self.previos = p


class LinkedList(object):

    def __init__(self):
        self._data = []
    
    def add(self, node):
        if len(self._data):
            self._data[-1].next = len(self._data)
        self._data.append(node)
        node.set_link_to_data(self._data)

    @property
    def count(self):
        return len(self._data)

    @property
    def head(self):
        if self._data:
            return self._data[0]


if __name__ == '__main__':
    # Test one linked nodes
    arr = [1, 20, 30, 5, 6]
    ll = LinkedList()
    for a in arr:
        ll.add(OneLinkNode(a))

    assert ll.count == len(arr)    
    
    item = ll.head
    assert item.value == arr[0]

    item = item.next
    item = item.next
    assert item.value == arr[2]

    item = item.next
    item = item.next

    assert item.next == None
    assert item.value == arr[-1]
