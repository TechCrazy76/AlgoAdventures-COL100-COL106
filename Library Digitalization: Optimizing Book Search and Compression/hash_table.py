from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.key_count = 0
        self.collision_type = collision_type
        # Extract parameters based on collision type
        if collision_type == 'Chain' or collision_type == 'Linear':
            self.z1, self.table_size = params[0], params[1]
            self.table = [[] for _ in range(self.table_size)] if collision_type == 'Chain' else [None] * self.table_size
        elif collision_type == 'Double':
            self.z1, self.z2, self.c2, self.table_size = params
            self.table = [None] * self.table_size
        else:
            raise ValueError("Invalid collision type specified.")

    def insert(self, x):
        pass
    
    def find(self, key):
        pass
    
    def get_slot(self, key):
        pass
    
    def get_load(self):
        return self.key_count / self.table_size
    
    def __str__(self):
        return str(self.table)
    
    def rehash(self):
        pass

class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)

    def insert(self, key):
        slot_index = self._hash(key)

        if self.collision_type == 'Chain':
            if key not in self.table[slot_index]:
                self.table[slot_index].append(key)
                self.key_count += 1

        elif self.collision_type == 'Linear':
            self._linear_probing_insert(slot_index, key)

        else:  # Double
            self._double_hashing_insert(slot_index, key)
            
    def find(self, key):
        idx = self._hash(key)

        if self.collision_type == 'Chain':
            return key in self.table[idx]

        elif self.collision_type == 'Linear':
            return self._linear_probing_find(idx, key)

        else:  # Double
            return self._double_hashing_find(idx, key) 
        
    def get_slot(self, key):
        return self._hash(key)
    def __str__(self):
        result = []
        if self.collision_type in ('Linear', 'Double'):
            for element in self.table:
                result.append("<EMPTY>" if element is None else str(element))
            return " | ".join(result)

        else:  # For "Chain"
            for chain in self.table:
                chain_result = " ; ".join(str(element) for element in chain)
                result.append(f"{chain_result}" if chain_result else "<EMPTY>")
            return " | ".join(result)

    def _hash(self, key):
        return sum(
            (ord(char) - ord('a') if 'a' <= char <= 'z' else
             ord(char) - ord('A') + 26 if 'A' <= char <= 'Z' else 0) *
            (self.z1 ** i) for i, char in enumerate(str(key))) % self.table_size

    def _linear_probing_insert(self, slot_index, key):
        start_index = slot_index
        while self.table[slot_index] is not None:
            if self.table[slot_index] == key:
                return
            slot_index = (slot_index + 1) % self.table_size
        if self.key_count == self.table_size:
            raise Exception('Table is Full')
        self.table[slot_index] = key
        self.key_count += 1

    def _double_hashing_insert(self, slot_index, key):
        h2 = self._hash_secondary(key)
        while self.table[slot_index] is not None:
            if self.table[slot_index] == key:
                return
            slot_index = (slot_index + h2) % self.table_size
        if self.key_count == self.table_size:
            raise Exception('Table is Full')
        self.table[slot_index] = key
        self.key_count += 1

    def _hash_secondary(self, key):
        return self.c2 - (sum(
            (ord(char) - ord('a') if 'a' <= char <= 'z' else
             ord(char) - ord('A') + 26 if 'A' <= char <= 'Z' else 0) *
            (self.z2 ** i) for i, char in enumerate(str(key))) % self.c2)

    def _linear_probing_find(self, idx, key):
        start_idx = idx
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return True
            idx = (idx + 1) % self.table_size
            if idx == start_idx:
                break
        return False

    def _double_hashing_find(self, idx, key):
        h2 = self._hash_secondary(key)
        while self.table[idx] is not None:
            if self.table[idx] == key:
                return True
            idx = (idx + h2) % self.table_size
        return False

class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def insert(self, x):
        slot_index = self._compute_hash_index(x[0])
        if self.collision_type == 'Chain':
            self._insert_chain(x, slot_index)
        elif self.collision_type == 'Linear':
            self._insert_linear(x, slot_index)
        else:  # Double
            self._insert_double(x, slot_index)
            
    def find(self, key):
        idx = self._compute_hash_index(key)
        if self.collision_type == "Chain":
            for ele in self.table[idx]:
                if ele[0] == key:
                    return ele[1]
        elif self.collision_type == "Linear":
            return self._find_linear(key, idx)
        else:  # Double
            return self._find_double(key, idx)
        return None 
    
    def get_slot(self, key):
        return self._compute_hash_index(key)
    
    def __str__(self):
        result = []
        if self.collision_type in ('Linear', 'Double'):
            result = [str(element) if element is not None else "<EMPTY>" for element in self.table]
        else:  # For "Chain"
            result = [
                " ; ".join(f"{key}:{value}" for key, value in chain) if chain else "<EMPTY>"
                for chain in self.table
            ]
        return " | ".join(result)

    def _compute_hash_index(self, key):
        return sum(
            (ord(char.lower()) - ord('a') if 'a' <= char.lower() <= 'z' else 0) *
            (self.z1 ** i) for i, char in enumerate(str(key))
        ) % self.table_size

    def _insert_chain(self, x, slot_index):
        if x not in self.table[slot_index]:
            self.table[slot_index].append(x)
            self.key_count += 1

    def _insert_linear(self, x, slot_index):
        start_index = slot_index
        while self.table[slot_index] is not None:
            if self.table[slot_index][0] == x[0]:  # Key already exists
                return
            slot_index = (slot_index + 1) % self.table_size
            if slot_index == start_index:  # Full table check
                raise Exception('Table is Full')
        self.table[slot_index] = x
        self.key_count += 1

    def _insert_double(self, x, slot_index):
        h2 = self.c2 - self._compute_hash_index(x[0]) % self.c2
        while self.table[slot_index] is not None:
            if self.table[slot_index][0] == x[0]:  # Key already exists
                return
            slot_index = (slot_index + h2) % self.table_size
        if self.key_count == self.table_size:
            raise Exception('Table is Full')
        self.table[slot_index] = x
        self.key_count += 1
        
    def _find_linear(self, key, idx):
        if self.table[idx] is not None and self.table[idx][0] == key:
            return self.table[idx][1]
        while self.table[idx] is not None:
            idx = (idx + 1) % self.table_size
            if self.table[idx] is not None and self.table[idx][0] == key:
                return self.table[idx][1]
        return None

    def _find_double(self, key, idx):
        k2 = self.c2 - self._compute_hash_index(key) % self.c2
        if self.table[idx] is not None and self.table[idx][0] == key:
            return self.table[idx][1]
        while self.table[idx] is not None:
            idx = (idx + k2) % self.table_size
            if self.table[idx] is not None and self.table[idx][0] == key:
                return self.table[idx][1]
        return None

    

    

