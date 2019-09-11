class HashTable:
    def __init__(self, len_hasht):
        self.len_hasht = len_hasht
        self.hash_table = [Maker() for i in range(self.len_hasht)]

    def hash_maker(self, key, data):
        hsh = abs(hash(key)) % self.len_hasht
        if self.hash_table[hsh].value == None or self.hash_table[hsh].value == "Tombstone":
            self.hash_table[hsh].add(key, data)
            return
        elif self.hash_table[hsh].value.key == key:
            self.hash_table[hsh].value.data = data
        else:
            tik = hsh
            tok = 0
            while self.hash_table[tik].value != None:
                if tok == self.len_hasht:
                    raise IndexError("Некуда класть")
                if self.hash_table[tik].value == "Tombstone":
                    break
                if self.hash_table[tik].value.key == key:
                    self.hash_table[tik].value.data = data
                    return
                tik = (tik+1)%self.len_hasht
                tok += 1
            self.hash_table[tik].add(key, data)

    def print_hash_table(self):
        for i in range(self.len_hasht):
            curr = self.hash_table[i].value
            print(i, end=' - ')
            if curr != None and curr != "Tombstone":
                print(curr.key, ':', curr.data)
            elif curr == None:
                print('None')
            else:
                print("Tombstone")

    def looking(self, key, index):
        tik = index
        tok = 0
        for i in range(self.len_hasht):
            if tok == self.len_hasht:
                return None
            if self.hash_table[tik].value == None:
                return None
            if self.hash_table[tik].value == "Tombstone":
                tik = (tik+1)%self.len_hasht
                tok += 1
                continue
            else:
                if self.hash_table[tik].value.key == key:
                    found = self.hash_table[tik].value
                    return found.data
                else:
                    tik = (tik+1)%self.len_hasht
                    tok += 1

    def look_for(self, key):
        index = abs(hash(key)) % self.len_hasht
        return self.looking(key, index)

    def deleting(self, key, index):
        tik = index
        tok = 0
        for i in range(self.len_hasht):
            if tok == self.len_hasht:
                return None
            if self.hash_table[tik].value == None:
                return None
            if self.hash_table[tik].value == "Tombstone":
                tik = (tik + 1) % self.len_hasht
                tok += 1
                continue
            else:
                if self.hash_table[tik].value.key == key:
                    self.hash_table[tik].value = "Tombstone"
                    self.print_hash_table()
                    break
                else:
                    tik = (tik + 1) % self.len_hasht
                    tok += 1

    def dell(self, key):
        index = abs(hash(key)) % self.len_hasht
        curr = self.hash_table[index].value
        if curr == None:
            return None
        elif curr == "Tombstone":
            self.deleting(key, index)
        elif curr.key == key:
            self.hash_table[index].value = "Tombstone"
            self.print_hash_table()
        else:
            return self.deleting(key, index)


class Cell:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data


class Maker:
    def __init__(self, value=None):
        self.value = value

    def add(self, key, ad_data):
        self.value = Cell(key, ad_data)




a = HashTable(7)
# Тестовые данные:

print('Test 1')
a.hash_maker('a', 1)
a.hash_maker('b', 1)
a.hash_maker('a', 2)
a.hash_maker('z', 2)
a.hash_maker('b', 3)
a.hash_maker('c', 2)
a.print_hash_table()   # b - 3, a - 2, c - 2, z - 2
print('\nTest 2')
a.look_for('c')     # c - 2
a.look_for('b')     # b - 3
a.look_for('a')     # a - 2
a.look_for('op')    # Нет такого ключа!
a.look_for('a')     # Нет такого значения в паре с данным ключом!
print('\nTest 3')
a.dell('c')            # print Tombstone
a.dell('d')            # Нет такого ключа!
a.dell('z')            # print Tombstone
print('\nTest 4')
a.hash_maker('a', 1)
a.hash_maker('b', 1)
a.hash_maker('a', 2)
a.hash_maker('z', 2)
a.hash_maker('b', 3)
a.hash_maker('c', 2)
a.print_hash_table()   # b - 3, a - 2, c - 2, z - 2, Tombstone, Tombstone
print('\nTest 5')
print(a.look_for('c'))    # c - 2
print(a.look_for('b'))     # b - 3
print(a.look_for('a'))     # a - 2
print(a.look_for('op'))    # Нет такого ключа!
print(a.look_for('e'))     # Нет такого значения в паре с данным ключом!
print('\nTest 6')
a.dell('c')            # print Tombstone
print(a.dell('d'))            # Нет такого ключа!
a.dell('z')            # print Tombstone
