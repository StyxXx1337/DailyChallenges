# [ EASY ]
# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# • record(order_id): adds the order_id to the log
# • get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class OrdersLog:
    def __init__(self, amt: int) -> None:
        self.index = 0
        self.log = [None] * amt

    def record(self, order_id: int) -> None:
        self.log[self.index] = order_id
        self.index += 1
        if self.index == len(self.log):
            self.index = 0

    def get_last(self, element: int) -> int:
        if element >= len(self.log):
            return None

        id = self.index - (element + 1)  # +1 is because the index is on the next slot
        if id < 0:
            id = len(self.log) + (id)  # wrap around, in case the id gets below 0

        return self.log[id]

    def __repr__(self) -> str:
        string = "[ "
        for el in self.log:
            string += str(el) + ' '

        string += "]"
        return string


# Test Code
log = OrdersLog(3)  # [None, None, None]
print(log)  # [None, None, None]

log.record(10)  # [10, None, None]
log.record(11)  # [10, 11, None]
log.record(12)  # [10, 11, 12]
print(log)

log.record(13)  # [13, 11, 12]
print(log)  # [13, 11, 12]

print(log.get_last(0))  # 13
print(log.get_last(1))  # 12
print(log.get_last(2))  # 11
print(log.get_last(3))  # Error - > None
print(log)
