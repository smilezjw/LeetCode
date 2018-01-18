# coding=utf8

class MyCalendar(object):
    def __init__(self):
        self.eventDate = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.eventDate:
            if s < end and e > start:
                return False
        self.eventDate.append([start, end])
        return True

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendarTreeMap(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if not self.root:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))

if __name__ == '__main__':
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))

    calTreeMap = MyCalendarTreeMap()
    print(calTreeMap.book(10, 20))
    print(calTreeMap.book(15, 25))
    print(calTreeMap.book(20, 30))
