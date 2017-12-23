import test


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = self.__class__(value)
                print(self)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = self.__class__(value)
                print(self)

    def step(self, arr):
        if self.left:
            self.left.step(arr)

        arr.append(self.value)

        if self.right:
            self.right.step(arr)

    def __str__(self):
        return '<l:%s>, %s, <r:%s>' % (self.left, self.value, self.right)

    @classmethod
    def run(cls, arr):
        node = Node(arr[0])
        for a in arr[1:]:
            node.insert(a)
        sorted_arr = []
        node.step(sorted_arr)
        return sorted_arr, None


if __name__ == '__main__':
    test.test(Node.run)