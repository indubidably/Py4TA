import builtins


class KeyValueStorage:
    def __init__(self, file_path):
        self.data = {}
        with open(file_path, 'r') as file:
            for line in file:
                key, value = line.split('=')
                try:
                    value = int(value)
                except ValueError:
                    pass
                if key in dir(builtins):
                    print(key + " is builtin")
                    continue
                if key.isidentifier():
                    self.data[key] = value
                else:
                    raise ValueError(f"Cannot assign a value to attribute '{key}'")

    def __getitem__(self, key):
        return self.data[key]

    def __getattribute__(self, name):
        if name == 'data':
            return object.__getattribute__(self, name)
        if name in self.data:
            return self.data[name]
        else:
            return object.__getattribute__(self, name)


storage = KeyValueStorage('task1.txt')
print(storage['name'])  # Output: 'kek'
print(storage.song)  # Output: 'shadilay'
print(storage.power)  # Output: 9001
