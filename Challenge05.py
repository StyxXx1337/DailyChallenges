# [ MEDIUM ]
# These 2 function takes one pair as Arguments:
# 			pair: a pair from the constructor.
#   Function car(pair) returns the first element of the pair
#   Function cdr(pair) returns the last/second element of the pair
#
#
# 	2021-07-21


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


# First Try but wrong order....
def car_f(a, b):
    return a


def cdr_f(a, b):
    return b


# test = cons(1,2)
# print(test(cdr_f))
# print(test(car_f))

# Correct Order Try
def car(con):
    def first(a, b):
        return a

    f = con(first)
    return f


def cdr(con):
    def last(a, b):
        return b

    l = con(last)
    return l


print(cdr(cons(100, 200)))
print(car(cons(100, 200)))
