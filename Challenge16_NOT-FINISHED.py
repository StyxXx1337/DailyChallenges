# You run an e-commerce website and want to record the last N order ids in a log.
# Implement a data structure to accomplish this, with the following API:
# •	record(order_id): adds the order_id to the log
# •	get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
# You should be as efficient with time and space as possible.


class OrdersLog:
    def __init__(self, amt: int) -> None:
        self.index = 0
        self.record = [None] * amt

    def record(self, order_id: int) -> None:
        self.record[self.index] = order_id
        self.index += 1
        if self.index == len(self.record):
            self.index = 0

    def get_last(self, element: int) -> int:
        return self.record[element]

    def __repr__(self) -> str:
        string = "[ "
        for el in self.record:
            string += str(el) + ' '

        string += "]\n"
        return string


log = OrdersLog(3)
print(log)

log.record(10)
log.record(11)
log.record(12)
print(log)

log.record(13)
print(log)

print(log.get_last(1))
print(log)
