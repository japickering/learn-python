class HashTable:
    def __init__(self):
        self.collection = {}

    # Return the sum of the Unicode code points in key.
    def hash(self, key):
        if not isinstance(key, str):
            return "Key must be a string"

        return sum(ord(character) for character in key)

    # Add or update a key-value pair in its collision bucket
    def add(self, key, value):
        hashed = self.hash(key)
        if not isinstance(hashed, int):
            return

        self.collection.setdefault(hashed, {})[key] = value

    # Remove key without affecting other keys sharing its hash
    def remove(self, key):
        hashed = self.hash(key)
        if not isinstance(hashed, int) or hashed not in self.collection:
            return

        bucket = self.collection[hashed]
        if key not in bucket:
            return

        del bucket[key]
        if not bucket:
            del self.collection[hashed]

    # Return the value for key or None when it is absent
    def lookup(self, key):
        hashed = self.hash(key)
        if not isinstance(hashed, int):
            return None

        return self.collection.get(hashed, {}).get(key)
