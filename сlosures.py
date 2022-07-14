def a1(n1, n):
    count = 0
    index = 1

    def a2(q):
        nonlocal index
        nonlocal count
        while count < n:
            yield index * q
            count += 1
            index += 1
    return a2


x = a1(20, 10)
y = x(5)
for i in y:
    if i > 10:
        y.close()
    print(i)

def fib():
    n1 = 0
    n2 = 1

    def find_number():
        nonlocal n1
        nonlocal n2
        n3 = n1 + n2
        n1, n2 = n2, n3
        return n3

    return find_number


def sum_numbers():
    numbers = []

    def inner(number):
        if isinstance(number, int):
            numbers.append(number)
        return sum(numbers)
    return inner
