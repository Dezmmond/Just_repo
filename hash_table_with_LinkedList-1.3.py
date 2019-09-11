class HashTable:
    def __init__(self, len_hasht):
        self.len_hasht = len_hasht
        self.hash_table = [LinkedList() for i in range(self.len_hasht)]

    def hash_maker(self, key, value):
        hsh = abs(hash(key))%self.len_hasht
        self.hash_table[hsh].add(key, value)

    def print_hash_table(self):
        for i in range(self.len_hasht):
            curr = self.hash_table[i].first
            print(i, end = ' - ')
            if curr != None:
                while curr.next != None:
                    print(curr.key, ':', curr.value, end = ', ')
                    curr = curr.next
                print(curr.key, ':', curr.value)
            else:
                print('None')

    def look_for(self, key):
        index = abs(hash(key))%self.len_hasht
        curr = self.hash_table[index].first
        if curr == None:
            return "Нет такого ключа!"
        while curr.key != key and curr.next!= None:
            curr = curr.next
        if curr.key == key:
            return curr.value
        else:
            return "Нет такого ключа!"

    def dell(self, key):
        index = abs(hash(key)) % self.len_hasht
        current = self.hash_table[index].first
        previous = None
        found = False
        while current and not found:
            if current.key == key:
                found = True
            else:
                previous = current
                current = current.next
        # nothing found, return None
        if not current:
            print("Ничего не найдено!")
        # the case where first item is being deleted
        elif not previous:
            self.hash_table[index].first = current.next
        # item from inside of the list is being deleted
        else:
            previous.next = current.next

class Host:
    def __init__(self, key = None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None

    def add(self, key, advalue):
        if self.first == None:
            self.first = Host(key, advalue)
        else:
            current = self.first
            while current != None:
                if current.key == key:
                    current.value = advalue
                    return
                else:
                    current = current.next
            self.first = Host(key, advalue, self.first)




a = HashTable(7)
# Тесты:

print('Test 1')
a.hash_maker('a', 'acd')
a.hash_maker('b', 'bacs')
a.hash_maker('c', 'sdsd')
a.hash_maker('d', 'sdsd')
a.hash_maker('x', 'sdsd')
a.hash_maker('z', 'sdsd')
a.hash_maker('v', 'sdsd')
a.hash_maker('a', 'sdasd')
a.print_hash_table()
print('\nTest 3')
print(a.look_for('c'))
print(a.look_for('b'))
print(a.look_for('op'))
print('\nTest 4')
a.dell('c')
a.dell('d')
a.hash_maker(2, 'bcd')
a.print_hash_table()
