from collections import OrderedDict


class BiDictionary:
    def __init__(self):
        self.values_by_first_key = {}
        self.values_by_second_key = {}
        self.values_by_tuple = {}

    def add(self, key1, key2, value):
        keys = (key1, key2)
        if key1 not in self.values_by_first_key:
            self.values_by_first_key[key1] = OrderedDict()
        if key2 not in self.values_by_first_key[key1]:
            self.values_by_first_key[key1][key2] = []

        if key2 not in self.values_by_second_key:
            self.values_by_second_key[key2] = OrderedDict()
        if key1 not in self.values_by_second_key[key2]:
            self.values_by_second_key[key2][key1] = []

        if keys not in self.values_by_tuple:
            self.values_by_tuple[keys] = []

        self.values_by_first_key[key1][key2].append(value)
        self.values_by_second_key[key2][key1].append(value)
        self.values_by_tuple[(key1, key2)].append(value)

    def find(self, keys: tuple):
        if keys not in self.values_by_tuple:
            return []

        return self.values_by_tuple[keys]

    def find_by_key1(self, key):
        if key not in self.values_by_first_key:
            return []
        return [distance for distances in self.values_by_first_key[key].values() for distance in distances]

    def find_by_key2(self, key):
        if key not in self.values_by_second_key:
            return []
        return [distance for distances in self.values_by_second_key[key].values() for distance in distances]

    def remove(self, key1, key2):
        keys = (key1, key2)
        if keys not in self.values_by_tuple:
            return False

        del self.values_by_first_key[key1][key2]
        del self.values_by_second_key[key2][key1]
        del self.values_by_tuple[(key1, key2)]

        return True

distances = BiDictionary()
distances.add("Sofia", "Varna", 443)
distances.add("Sofia", "Varna", 468)
distances.add("Sofia", "Varna", 490)
distances.add("Sofia", "Plovdiv", 145)
distances.add("Sofia", "Bourgas", 383)
distances.add("Plovdiv", "Bourgas", 253)
distances.add("Plovdiv", "Bourgas", 292)

print(distances.find_by_key1("Sofia"))  # 443, 468, 490, 145, 383
print(distances.find_by_key2("Bourgas"))  # 383, 253, 292
print(distances.find(("Rousse", "Varna")))  # []
print(distances.find(("Sofia", "Varna")))  # 443, 468, 490
print(distances.remove("Sofia", "Varna"))  # true
print(distances.find_by_key1("Sofia"))  # 145, 383
print(distances.find_by_key2("Varna"))  # []
print(distances.find(("Sofia", "Varna")))  # []