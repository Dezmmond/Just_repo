class Node:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.value = data
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None  # корень дерева

    def lookup(self, current, target):
        if target < current.key:
            if current.left == None:
                return current
            else:
                return self.lookup(current.left, target)

        elif target > current.key:
            if current.right == None:
                return current
            else:
                return self.lookup(current.right, target)
        else:
            return current

    # /* функция для добавления узла в дерево */
    def new_node(self, key, data):
        if self.root == None:
            self.root = Node(key, data)

        else:
            current = self.lookup(self.root, key)
            if current.key == key:
                current.value = data
            elif key > current.key:
                current.right = Node(key, data)
            elif key < current.key:
                current.left = Node(key, data)
            return current

    def looking_for_kill(self, start, target, previous = None):
        if start == None:
            return None, None
        else:
            if start.key == target:
                return previous, start
            else:
                if target < start.key:
                    return self.looking_for_kill(start.left, target, start)
                else:
                    return self.looking_for_kill(start.right, target, start)

    def remove(self, key):
        prev, node = self.looking_for_kill(self.root, key)
        if node == None:
            return False
        if node.left == None and node.right == None:
            if prev == None:
                self.root = None
                return True
            if node == prev.left:
                prev.left = None
            else:
                prev.right = None
            return True
        if node.left != None:
            max = node.left
            maxprev = node
            while max.right != None:
                maxprev = max
                max = max.right
            node.key, node.value = max.key, max.value
            if max == maxprev.left:
                maxprev.left = None
            else:
                maxprev.right = None
            return True

        if node.right != None:
            max = node.right
            maxprev = node
            while max.left != None:
                maxprev = max
                max = max.left
            node.key, node.value = max.key, max.value
            if max == maxprev.left:
                maxprev.left = None
            else:
                maxprev.right = None
            return True
            


class HashTable(Tree): 
    def __init__(self, len_hasht):
        self.len_hasht = len_hasht
        self.hash_table = [Tree() for i in range(self.len_hasht)]

    def hash_maker(self, key, value):
        hsh = abs(hash(key)) % self.len_hasht
        self.hash_table[hsh].new_node(key, value)

    def print_hash_table(self, tree):
        if tree == None:
            return
        self.print_hash_table(tree.left)
        self.print_hash_table(tree.right)
        print(tree.key, ':', tree.value)

    def start_printing(self):
        for i in range(self.len_hasht):
            self.print_hash_table(self.hash_table[i].root)

    def look_for(self, key):
        index = abs(hash(key)) % self.len_hasht
        curr = self.hash_table[index].root
        if curr == None:
            return None

        elif curr.key == key:
            return curr.value

        else:
            found = self.lookup(curr, key) # lookup в дерЕВЕ!!!
            if not found or found.key != key:
                return None
            else:
                return found.value

    def dell(self, key):
        index = abs(hash(key)) % self.len_hasht
        return self.hash_table[index].remove(key)


# Тесты:
print("Test 1")
a = HashTable(3)
a.hash_maker('b', 'asd')
a.hash_maker('a', 'asd')
a.hash_maker('c', 'asd')
a.hash_maker('a', 'a')
a.hash_maker('sd', 'asd')
a.hash_maker('dd', 'asd')
a.hash_maker('db', 'asd')
a.hash_maker('dq', 'asd')
a.start_printing()
print("\nTest 2")
print(a.look_for('a'))
print(a.look_for('a'))
print(a.look_for('op'))
print(a.look_for('ab'))
print("\nTest 3")
print(a.dell('a'))
print(a.dell('a'))
print(a.dell('op'))
