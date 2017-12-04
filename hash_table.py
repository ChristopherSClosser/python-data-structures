"""Hash table."""


class HtNode:
    """."""
    def __init__(self, key, val):
        """."""
        self.key = key
        self.val = val
        self.next = None


class HashTable(object):
    """."""

    def __init__(self, size=8192):
        """."""
        self.size = size
        self.buckets = [None] * self.size

    def _hash(self, key):
        """."""
        return hash(key) % self.size

    def set(self, key, val):
        """."""
        if any(char.isdigit() for char in key) or any(char.isdigit() for char in val):
            raise ValueError('no numbers permitted')
        bucket = self._hash(key)
        entry = self.buckets[bucket]
        if not entry:
            self.buckets[bucket] = HtNode(key, val)
        else:
            self.extend(entry, key, val)

    def extend(self, entry, key, val):
        """."""
        while entry and entry.key != key:
            prev = entry
            entry = entry.next
            if entry:
                entry.val = val
            else:
                prev.next = HtNode(key, val)

    def get(self, key):
        """."""
        bucket = self._hash(key)
        if not self.buckets[bucket]:
            raise KeyError('key not found')
        else:
            entry = self.buckets[bucket]
            while entry and entry.key != key:
                if entry.next:
                    entry = entry.next
                else:
                    return 'something went wrong'
            return entry.val
