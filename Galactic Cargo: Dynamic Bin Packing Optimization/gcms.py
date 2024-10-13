from bin import Bin
from avl import AVLTree
from object import Object, Color
from exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins = AVLTree()  # AVL tree for managing bins
        self.objects = AVLTree()  # AVL tree for managing objects

    def add_bin(self, bin_id, capacity):
        new_bin = Bin(bin_id, capacity)
        self.bins.insert(new_bin)

    def add_object(self, object_id, size, color):
        new_object = Object(object_id, size, color)

        if color == Color.RED:
            suitable_bin = self.find_largest_least_fit(size)
        elif color == Color.GREEN:
            suitable_bin = self.find_largest_greatest_fit(size)
        elif color == Color.BLUE:
            suitable_bin = self.find_compact_least_fit(size)
        elif color == Color.YELLOW:
            suitable_bin = self.find_compact_greatest_fit(size)

        if suitable_bin is None:
            raise NoBinFoundException()

        suitable_bin.add_object(new_object)  # Add object to the selected bin
        new_object.assigned_bin = suitable_bin.bin_id  # Assign bin ID to the object
        self.objects.insert(new_object)  # Add the object to the AVL tree for objects

    def delete_object(self, object_id):
        # Find the object in the AVL tree
        obj_node = self.objects.root
        while obj_node:
            if object_id < obj_node.value.object_id:
                obj_node = obj_node.left
            elif object_id > obj_node.value.object_id:
                obj_node = obj_node.right
            else:
                break
        
        if not obj_node:
            return  # Object not found

        obj = obj_node.value  # Get the object

        # Remove the object from its assigned bin
        if obj.assigned_bin:
            bin_node = self.bins.root
            while bin_node:
                if obj.assigned_bin < bin_node.value.bin_id:
                    bin_node = bin_node.left
                elif obj.assigned_bin > bin_node.value.bin_id:
                    bin_node = bin_node.right
                else:
                    break
            
            if bin_node:
                bin_node.value.objects.remove(obj)  # Remove the object from the bin
                bin_node.value.remaining_capacity += obj.size  # Update remaining capacity

        # Delete the object from the AVL tree
        self.objects.delete(obj)

    def bin_info(self, bin_id):
        current = self.bins.root
        while current:
            if bin_id < current.value.bin_id:
                current = current.left
            elif bin_id > current.value.bin_id:
                current = current.right
            else:
                return (current.value.remaining_capacity, current.value.get_object_ids())
        return None

    def object_info(self, object_id):
        current = self.objects.root
        while current:
            if object_id < current.value.object_id:
                current = current.left
            elif object_id > current.value.object_id:
                current = current.right
            else:
                return current.value.assigned_bin  # Return the assigned bin ID
        return None

    def find_largest_least_fit(self, size):
        best_fit = None
        current = self.bins.root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Go to the leftmost node

            current = stack.pop()
            if current.value.remaining_capacity >= size:
                if best_fit is None or current.value.remaining_capacity > best_fit.remaining_capacity or \
                   (current.value.remaining_capacity == best_fit.remaining_capacity and current.value.bin_id < best_fit.bin_id):
                    best_fit = current.value

            current = current.right  # Now check the right subtree

        return best_fit

    def find_largest_greatest_fit(self, size):
        best_fit = None
        current = self.bins.root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Go to the leftmost node

            current = stack.pop()
            if current.value.remaining_capacity >= size:
                if best_fit is None or current.value.remaining_capacity > best_fit.remaining_capacity or \
                   (current.value.remaining_capacity == best_fit.remaining_capacity and current.value.bin_id > best_fit.bin_id):
                    best_fit = current.value

            current = current.right  # Now check the right subtree

        return best_fit

    def find_compact_least_fit(self, size):
        best_fit = None
        current = self.bins.root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Go to the leftmost node

            current = stack.pop()
            if current.value.remaining_capacity >= size:
                if best_fit is None or current.value.remaining_capacity < best_fit.remaining_capacity or \
                   (current.value.remaining_capacity == best_fit.remaining_capacity and current.value.bin_id < best_fit.bin_id):
                    best_fit = current.value

            current = current.right  # Now check the right subtree

        return best_fit

    def find_compact_greatest_fit(self, size):
        best_fit = None
        current = self.bins.root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left  # Go to the leftmost node

            current = stack.pop()
            if current.value.remaining_capacity >= size:
                if best_fit is None or current.value.remaining_capacity < best_fit.remaining_capacity or \
                   (current.value.remaining_capacity == best_fit.remaining_capacity and current.value.bin_id > best_fit.bin_id):
                    best_fit = current.value

            current = current.right  # Now check the right subtree

        return best_fit
