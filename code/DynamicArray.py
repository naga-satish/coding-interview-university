import ctypes


class DynamicArray:
    def __init__(self, size):
        assert size > 0
        self.filled_idx = -1
        self.size = size
        self.array = self._make_array(self.size)

    def _make_array(self, size):
        return (size * ctypes.py_object)()

    def _resize(self, new_size):
        resized_arr = self._make_array(new_size)

        for idx in range(self.filled_idx+1):
            resized_arr[idx] = self.array[idx]

        self.size = new_size
        self.array = resized_arr

    def append(self, item):
        if self.size == self.filled_idx+1:
            self._resize(2 * self.size)

        self.array[self.filled_idx+1] = item
        self.filled_idx += 1

    def insert(self, insert_at, value):
        if insert_at == self.filled_idx+1:
            self.append(value)
        elif 0 <= insert_at <= self.filled_idx:
            if self.filled_idx == self.size - 1:
                self._resize(2 * self.size)

            for idx in range(self.filled_idx, insert_at-1, -1):
                self.array[idx + 1] = self.array[idx]

            self.array[insert_at] = value
            self.filled_idx += 1
        else:
            raise ValueError("please provide valid index to insert.")

    def remove(self, value):
        flag = 0
        for idx in range(0, self.filled_idx+1, 1):
            if self.array[idx] == value:
                self.__delitem__(idx)
                flag = 1
                break

        if flag == 0:
            print('No Such element')

    def clear(self):
        self.array = self._make_array(self.size)
        self.filled_idx = -1

    def find(self, value):
        for idx in range(0, self.filled_idx+1, 1):
            if self.array[idx] == value:
                return idx
        print('No such element.')

    def pop(self):
        if self.filled_idx >= 0:
            last_element = self.array[self.filled_idx]

            self.array[self.filled_idx] = ctypes.py_object()
            self.filled_idx -= 1

            return last_element
        else:
            print("Empty Array. No element to pop.")

    def __delitem__(self, idx):
        if 0 <= idx <= self.filled_idx:
            for idx in range(idx, self.filled_idx, 1):
                self.array[idx] = self.array[idx + 1]

            self.array[self.filled_idx] = ctypes.py_object()
            self.filled_idx -= 1
        else:
            raise ValueError("Index out of range.")

    def __getitem__(self, idx):
        if 0 <= idx <= self.filled_idx:
            return self.array[idx]
        else:
            raise ValueError("Index out of range")

    def __setitem__(self, idx, value):
        if 0 <= idx <= self.filled_idx:
            self.array[idx] = value
        elif (self.filled_idx == -1) or (idx == self.filled_idx+1):
            self.array[idx] = value
            self.filled_idx += 1
        else:
            raise ValueError("Index out of range")

    def __len__(self):
        return self.size

    def __str__(self):
        return "[" + ", ".join([
            str(self.array[_]) if type(self.array[_]) is not str else f"'{str(self.array[_])}'"
            for _ in range(self.filled_idx+1)
        ]) + "]"


n = 5
a = DynamicArray(n)
for i in range(n):
    a[i] = 'i'*(i+1)

print(a)
print(len(a))
del a[3]
print(a)
a[3] = ''
print(a)
a.append(5)
print(a)
a.remove('')
print(a)
print(a.find('i'))
print(a)
