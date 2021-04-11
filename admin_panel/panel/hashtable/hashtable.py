from hashlib import md5

# The size of the rashtable is directly proportional to the number of collisions
# that might
defaultHashTableSize = 10


class Node:

    # @param {string} key
    # @param {*} value
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "<Node: (%s, %s), next: %s>" % (
            self.key, self.value, self.next != None)

    def __repr__(self):
        return str(self)


class HashTable:

    # @param {number} hashtable
    def __init__(self, hashTableSize = defaultHashTableSize):
        self.buckets = [None] * hashTableSize

    # @param {string} key
    # @param {*} value
    def set(self, key, value):
        _index = self.hash(key)
        _node = self.buckets[_index]

        if _node is None:
            # Create node
            self.buckets[_index] = Node(key, value)
            return True

        _prev = _node
        while _node is not None:
            _prev = _node
            _node = _node.next
        _prev.next = Node(key, value)
        return True

    # @param {string} key
    # @returns {*}
    def get(self, key):

        _index = self.hash(key)
        _node = self.buckets[_index]

        while _node is not None and _node.key != key:
            _node = _node.next

        if _node is None: return None
        else: return _node.value


    # @param {string} key
    # @returns {*}
    def delete(self, key):

        _index = self.hash(key)
        _node = self.buckets[_index]
        _prev = None

        while _node is not None and _node.key != key:
            _prev = _node
            _node = _node.next

        if _node is None: return None
        else:
            _result = _node.value
            if _prev is None: self.buckets[_index] = _node.next
            else: _prev.next = _prev.next.next
            return _result

    # @params {string} key
    # @returns {number}
    def hash(self, key):
        k = 0
        for s in list(md5(str(key).encode('utf-8')).hexdigest()):
            k += ord(s)
        return k % len(self.buckets)

    # @returns hashtable visual structure
    def structure(self):
        for i, _node in enumerate(self.buckets):
            print("Bucket %s" % i, end=' -> ')
            while _node is not None:
                print("{%s: %s}" % (_node.key, _node.value), end=' -> ')
                _node = _node.next
            print("None")
