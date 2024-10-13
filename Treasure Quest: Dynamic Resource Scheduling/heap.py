class Heap:
    '''
    Class to implement a heap with a general comparison function
    '''
    
    def __init__(self, comp_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function.
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        self.size = len(init_array)
        self._heap = init_array
        self.comparator = comp_function
        self.build_heap()  # Build the heap upon initialization

    def build_heap(self):
        '''
        Arguments:
            None
        Returns:
            None
        Description:
            Builds the heap based on the comparison function
        Time Complexity: O(n)
        '''
        for i in range((self.size // 2) - 1, -1, -1):
            self.heapify_down(i)

    def heapify_up(self, curr_index):
        '''
        Arguments:
            curr_index : int : Index to heapify up from
        Returns:
            None
        Time Complexity: O(log(n))
        '''
        # Calculate parent index inline
        while curr_index > 0:
            parent_index = (curr_index - 1) // 2
            if self.comparator(self._heap[curr_index], self._heap[parent_index]):
                # Swap current element with its parent
                self._heap[curr_index], self._heap[parent_index] = self._heap[parent_index], self._heap[curr_index]
                curr_index = parent_index
            else:
                break

    def heapify_down(self, parent_index=0):
        '''
        Arguments:
            parent_index : int : Index to heapify down from
        Returns:
            None
        Time Complexity: O(log(n))
        '''
        while True:
            # Calculate child indices inline
            left_child = 2 * parent_index + 1
            right_child = 2 * parent_index + 2
            smallest_index = parent_index

            # Check if the left child exists and is smaller than the current smallest
            if left_child < self.size and self.comparator(self._heap[left_child], self._heap[smallest_index]):
                smallest_index = left_child

            # Check if the right child exists and is smaller than the current smallest
            if right_child < self.size and self.comparator(self._heap[right_child], self._heap[smallest_index]):
                smallest_index = right_child

            # If the parent is in the correct position (i.e., no swaps needed), stop
            if smallest_index == parent_index:
                break

            # Swap parent with the smallest child and continue
            self._heap[parent_index], self._heap[smallest_index] = self._heap[smallest_index], self._heap[parent_index]

            # Move down to the smallest child's position and continue heapifying
            parent_index = smallest_index

    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Time Complexity: O(log(n))
        '''
        self._heap.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Time Complexity: O(log(n))
        '''
        if self.isEmpty():
            return None
        
        if self.size == 1:
            self.size -= 1
            return self._heap.pop()

        # Store the top value
        value = self._heap[0]
        # Replace the root with the last element
        self._heap[0] = self._heap.pop()
        # Decrease size
        self.size -= 1
        # Restore heap property by bubbling down
        self.heapify_down(0)

        return value

    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Time Complexity: O(1)
        '''
        return None if self.isEmpty() else self._heap[0]

    def isEmpty(self):
        '''
        Arguments:
            None
        Returns:
            bool : True if the heap is empty, False otherwise
        Time Complexity: O(1)
        '''
        return self.size == 0

