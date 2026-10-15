import random

class Coin:
    def __init__(self, heads = 0, tails = 1):
        self.heads = heads
        self.tails = tails

    def toss(self, times=1):
        for i in range(times):
            result = random.randint(self.heads, self.tails)
            if result == self.heads:
                print("Вітаємо, у вас Орел!")
            else:
                print("Вітаємо, у вас Решка")

coin1 = Coin()

coin1.toss(5)