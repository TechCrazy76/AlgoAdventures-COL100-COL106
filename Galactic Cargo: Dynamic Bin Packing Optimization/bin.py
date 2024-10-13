class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.remaining_capacity = capacity
        self.objects = []

    def add_object(self, obj):
        if obj.size <= self.remaining_capacity:
            self.objects.append(obj)
            self.remaining_capacity -= obj.size

    def get_object_ids(self):
        return [obj.object_id for obj in self.objects]
