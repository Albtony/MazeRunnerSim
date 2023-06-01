class EntityMap:
    def __init__(self):
        self.entries = {}

    def addEntry(self, key, value):
        self.entries[key] = value

    def removeEntry(self, key):
        if key in self.entries:
            del self.entries[key]

    def getEntry(self, key):
        return self.entries.get(key)

    def hasEntry(self, key):
        return key in self.entries