class ResizableArray:

    # ratio of element to size of array on witch it should be downsized
    RESIZE_FACTOR_UP = 1/2
    # ratio of element to size of array on witch it should be upsized
    RESIZE_FACTOR_DOWN = 1/3
    # minimal size of the array (the size is not shrinked below this size)
    MIN_SIZE = 10

    def __init__(self, size=10):
        self._size = size
        # current amount of the elements in array
        self._filled = 0
        # initialize and prepopulate list of length size given in constructor
        self._element = [None for _ in range(size)]

    def contains(self, value):
        for e in self._element:
            if e == value:
                return True
        return False

    def add(self, value):
        # increment amount of element if you add new element
        if not self.contains(value):
            for i, v in enumerate(self._element):
                # find first empty place in underlying array
                if not v:
                    self._element[i] = value
                    break
            self._filled += 1
            self._resize()

    def delete(self, value):
        # decrement amount of elements if you remove element that existed
        if self.contains(value):
            self._filled -= 1

            for i, v in enumerate(self._element):
                if v == value:
                    self._element[i] = None
                    break
            self._resize()

    # resize array if there is to much or not enougth free space
    def _resize(self):
        capacity_ratio = float(self._filled) / self._size
        # shrink array if there is less than RESIZE_FACTOR_DOWN elements
        if capacity_ratio < ResizableArray.RESIZE_FACTOR_DOWN and self._size / 2 >= ResizableArray.MIN_SIZE:
            new_element_array = [None for _ in range(int(self._size/2))]
            i = 0
            for e in self._element:
                if e:
                    new_element_array[i] = e
                    i += 1
            self._element = new_element_array
            self._size = len(new_element_array)
        # grow arrary if there is more than then RESIZE_FACTOR_UP elements
        if capacity_ratio > ResizableArray.RESIZE_FACTOR_UP:
            for i in range(self._size):
                self._element.append(None)
            self._size *= 2

    def __str__(self):
        return f"size: {self._size} elements: {self._element}"


if __name__ == '__main__':
    set = ResizableArray()
    for i in range(40):
        set.add(i * 4)
        print(set)

    print(set.contains(4))
    print(set.contains(44))
    print(set.contains(40))

    print(set.contains(41))

    print(set.contains(41))
    # for e in set:
    #     print(e)


    for i in range(40):
        set.delete(i * 4)
        print(set)