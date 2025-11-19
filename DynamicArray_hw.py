import ctypes

class DynamicArray:
    def __init__(self, initial_capacity=1):
        self._n = 0
        self._capacity = initial_capacity
        self._A = self._make_array(self._capacity)
        self.resize_count = 0
        self.growth_factor = 1.5 

    def __len__(self):
        return self._n

    def _make_array(self, c):
        return (c * ctypes.py_object)()

    def _resize(self, new_cap):
        B = self._make_array(int(new_cap))
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = int(new_cap)
        self.resize_count += 1

    def append(self, obj):
        if self._n == self._capacity:
            new_capacity = int(self._capacity * self.growth_factor)
            if new_capacity == self._capacity:  
                new_capacity += 1
            self._resize(new_capacity)

        self._A[self._n] = obj
        self._n += 1



arr = DynamicArray(initial_capacity=128)

for i in range(1_000_000):
    arr.append(i)

print("Final capacity:", arr._capacity)
print("Resize count:", arr.resize_count)
