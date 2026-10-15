class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            print(f"У скарбничці: {self.coins}")
        else:
            print("Недостатньо місця в скарбничці")

box1 = MoneyBox(10)
box1.add(5)
print(box1.can_add(5))
box1.add(5)
