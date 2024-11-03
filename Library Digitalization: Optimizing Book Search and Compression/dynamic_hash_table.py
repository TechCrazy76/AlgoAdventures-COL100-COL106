from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        self.table_size = get_next_size()
        old_table = self.table
        self.key_count = 0

        self.table = [[] for _ in range(self.table_size)] if self.collision_type == 'Chain' else [None] * self.table_size
        for bucket in old_table:
            if bucket:
                for key in (bucket if self.collision_type == 'Chain' else [bucket]):
                    if key is not None:
                        self.insert(key)

    def insert(self, x):
        super().insert(x)
        if self.get_load() >= 0.5:
            self.rehash()


class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def rehash(self):
        self.table_size = get_next_size()
        old_table = self.table
        self.key_count = 0

        self.table = [[] for _ in range(self.table_size)] if self.collision_type == 'Chain' else [None] * self.table_size
        for bucket in old_table:
            if bucket:
                for key_value in (bucket if self.collision_type == 'Chain' else [bucket]):
                    if key_value is not None:
                        self.insert(key_value)

    def insert(self, key):
        super().insert(key)
        if self.get_load() >= 0.5:
            self.rehash()