class HashTableChaining:
    def __init__(self, m=8):
        self.m = m
        self.table = [[] for _ in range(self.m)]
        self.counter = 0

    @staticmethod
    def get_hash_code(word):
        key = 0
        characters = list(word)
        for character in characters:
            key += ord(character)
        return key

    def hash_func(self, key):
        return int(key % self.m)

    def chaining_insert(self, key, value):
        # получаем хэш-код
        h_code = self.get_hash_code(key)
        # получаем хэш-значение
        hash_val = self.hash_func(h_code)
        # вставляем в таблицу
        self.table[hash_val].append((key, value))
        self.counter += 1
        # делаем рехэширование, если таблица заполнена на половину
        if self.counter >= (self.m / 2):
            self.print_hash_table()
            self.chaining_rehash(self.m * 2)

    def chaining_rehash(self, new_m):
        print('Table after rehash:')
        entries = self.table
        self.__init__(new_m)
        for bucket in entries:
            if len(bucket) == 0:
                continue
            else:
                for key, value in bucket:
                    self.chaining_insert(key, value)

    def chaining_delete(self, key):
        h_code = self.get_hash_code(key)
        hash_val = self.hash_func(h_code)
        bucket = self.table[hash_val]
        for idx, (key_list, value) in enumerate(bucket):
            if key_list == key:
                del bucket[idx]
                self.counter -= 1

    def chaining_search(self, key):
        h_code = self.get_hash_code(key)
        hash_val = self.hash_func(h_code)
        bucket = self.table[hash_val]
        for idx, (key_list, value) in enumerate(bucket):
            if key_list == key:
                return value

    def print_hash_table(self):
        print(self.table)


if __name__ == "__main__":
    ht = HashTableChaining()

    ht.chaining_insert('apple', 6)
    ht.chaining_insert('dog', 2)
    ht.chaining_insert('art', 4)
    ht.chaining_insert('box', 7)
    ht.print_hash_table()

    ht.chaining_delete('box')
    ht.print_hash_table()

    ht.chaining_insert('cat', 2)
    ht.print_hash_table()

    print(ht.chaining_search('art'))
