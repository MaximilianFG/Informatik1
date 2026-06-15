class box:
    def __init__(self, length: float, width: float, height: float):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f"{self.length} L x {self.width} W x {self.height} H"

    def is_cubic(self):
        if self.length == self.width == self.height:
            return True
        else:
            return False

    def __eq__(self, other):
        if (
            self.length == other.length
            and self.width == other.width
            and self.height == other.height
        ):
            return True
        else:
            return False


small_box = box(5, 10, 4)
big_box = box(20, 20, 20)


print(small_box)
print(big_box)
print(small_box.volume())
print(big_box.volume())
print(small_box.is_cubic())
print(big_box.is_cubic())
print(small_box.__eq__(big_box))
