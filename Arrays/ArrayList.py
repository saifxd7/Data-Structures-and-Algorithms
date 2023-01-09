import ctypes

class ArrayList:
    def __init__(self):
        """
        Initializes an empty ArrayList with a fixed capacity of 1.
        """
        self.capacity = 1
        self.size = 0
        self.A = self.make_array(self.capacity)

    def __len__(self):
        """
        Returns the number of elements in the list.
        """
        return self.size

    def __getitem__(self, k):
        """
        Returns the element at index k.
        """
        if not 0 <= k < self.size:
            return IndexError('Index out of bounds')
        return self.A[k]

    def append(self, elem):
        """
        Appends the given element to the end of the list.
        """
        if self.size == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.size] = elem
        self.size += 1

    def remove(self, elem):
        """
        Removes the first occurrence of the given element from the list.
        Raises a ValueError if the element is not found in the list.
        """
        for i in range(self.size):
            if self.A[i] == elem:
                self.A[i] = None
                self.size -= 1
                self._shift_left(i)
                return
        raise ValueError('Element not found in list')

    def _shift_left(self, index):
        """
        Shifts all elements after the removed element one position to the left.
        """
        for i in range(index, self.size):
            self.A[i] = self.A[i+1]
        self.A[self.size] = None

    def _resize(self, new_capacity):
        """
        Resizes the array to the given capacity.
        """
        B = self.make_array(new_capacity)
        for k in range(self.size):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        """
        Makes a new array with the given capacity.
        """
        return (new_capacity * ctypes.py_object)()


