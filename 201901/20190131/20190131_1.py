# -*- coding: utf-8 -*-

'''
@Author: chenxj
@Github: https://github.com/chenxj1101
@Mail: ccj799@gmail.com
@Date: 2019-01-31 10:16:28
@LastEditTime: 2019-01-31 14:10:06
@Description: hashmap data type
'''


class HashTable(object):

    _empty = object()
    _deleted = object()

    def __init__(self, size=11):
        self.size = size
        self.len = 0
        self._keys = [self._empty] * size
        self._values = [self._empty] * size

    def put(self, key, value):
        initial_hash = hash_ = self.hash(key)

        while True:
            if self._keys[hash_] is self._empty or self._keys[hash_] is self._deleted:
                self._keys[hash_] = key
                self._values[hash_] = value
                self._len += 1
                return
            elif self._keys[hash_] == key:
                self._keys[hash_] = key
                self._values[hash_] = value
                return

            hash_ = self._rehash(hash_)

            if initial_hash == hash_:
                raise ValueError("Table is full")

    def get(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                return None
            elif self._keys[hash_] == key:
                return self._values[hash_]

            hash_ = self._rehash(hash_)
            if initial_hash == hash_:
                return None

    def del_(self, key):
        initial_hash = hash_ = self.hash(key)
        while True:
            if self._keys[hash_] is self._empty:
                return None
            elif self._keys[hash_] == key:
                self._keys[hash_] = self._deleted
                self._values[hash_] = self._deleted
                self._len -= 1
                return
            
            hash_ = self._rehash(hash_)
            if initial_hash = hash_:
                return None

    def hash(self, key):
        return key % self.size

    def _rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        return self.del_(key)

    def __setitem__(self, key, value):
        self.put(key, value)
    
    def __len__(self):
        return self._len


class ResizableHashTable(HashTable):
    MIN_SIZE = 8

    def __init__(self):
        super().__init__(self.MIN_SIZE)

    def put(self, key, value):
        rv = super().put(key, value)
        if len(self) >= (self.size * 2) / 3:
            self.__resize()

    def __resize(self):
        keys, values = self._keys, self._values
        self.size *= 2
        self._len = 0
        self._keys = [self._empty] * self.size
        self._values = [self._empty] * self.size
        for key, value in zip(keys, values):
            if key is not self._empty and key is not self._deleted:
                self.put(key, value)

