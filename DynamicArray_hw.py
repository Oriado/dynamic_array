import ctypes

class DynamicArray:
    def __init__(self, initial_capacity=1, growth_factor= 1 + 5/10):
        self._n = 0
        self._capacity = initial_capacity
        self._A = self._make_array(self._capacity)
        self.resize_count = 0
        self.growth_factor = growth_factor

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
            if new_capacity <= self._capacity:
                new_capacity = self._capacity + 1
            self._resize(new_capacity)

        self._A[self._n] = obj
        self._n += 1


if __name__ == "__main__":
    elements_checks = [1, 100, 1000, 10000, 100000]
    growth_factors = [1.2, 1.5, 2.0]

    for gf in growth_factors:
        print(f"#### Growth Factor: {gf}")
        print("| number of elements | final capacity | resize count | wasted memory |")
        print("|--------------------|----------------|--------------|---------------|")
        
        for num in elements_checks:
            arr = DynamicArray(initial_capacity=1, growth_factor=gf)
            for i in range(num):
                arr.append(i)
            
            wasted = arr._capacity - arr._n
            print(f"| {num:<18} | {arr._capacity:<14} | {arr.resize_count:<12} | {wasted:<13} |")
        print("\n---")

    print("| growth_factor | initial capacity | elements | resize count | wasted memory |")
    print("|---------------|------------------|----------|--------------|---------------|")
    
    test_cases = [
        (1.2, 8), (1.2, 32), (1.2, 128),
        (1.5, 8), (1.5, 32), (1.5, 128),
        (2.0, 8), (2.0, 32), (2.0, 128)
    ]

    for gf, init_cap in test_cases:
        arr = DynamicArray(initial_capacity=init_cap, growth_factor=gf)
        for i in range(100000):
            arr.append(i)
            
        wasted = arr._capacity - arr._n
        print(f"| {gf:<13} | {init_cap:<16} | {arr._capacity:<8} | {arr.resize_count:<12} | {wasted:<13} |")

    print("\n---")


