class DBDB(object):
    def __init__(self, f):
        self._storage = Storage(f)
        self._tree = BinaryTree(self._storage)
    def __getitem__(self, key):
        self._assert_not_closed()
        return self._tree.get(key)
    def __setitem__(self, key, value):
        self._assert_not_closed()
        return self._tree.set(key, value)
    def _assert_not_closed(self):
        if self._storage.closed:
            raise ValueError('Database closed.')
    def commit(self):
        self._assert_not_closed()
        self._tree.commit()
