from functools import reduce


def area(s, b=0, h=0):
    if b == 0:
        if h == 0:
            return s * s
    elif b != 0 and h == 0:
        return s * b
    else:
        return s * b * h


print(area(5))
print(area(5, 3))
print(area(5, 3, 4))


def print_details(id=None, name=None, category="General"):
    if id is None:
        if name is None:
            return "Invalid information is given"
        else:
            return "Name: " + name + " Category: " + category
    else:
        if name is not None:
            # return "ID: " + str(id) + " Name: " + name + " Category: " + category
            return id, name, category
        else:
            return "Name is missing"


print(print_details())
print(print_details(id=1))
print(print_details(name="Harsh"))
print(print_details(id=1, name="Harsh"))
print(print_details(id=2, name="Raman", category="Reserved"))
print(print_details(2, name="Raman", category="Reserved"))
print(print_details(2, name="Raman", category="Reserved")[1])


def square(x): return x*x


def product(a, b): return a*b


def applier(q, x, y=0):
    if y == 0:
        return q(x)
    else:
        return q(x, y)


print(applier(square, 7))
print(applier(product, 7, 8))


def fahrenheit(T):
    return float("%.2f" % ((float(9)/5)*T + 32))


def celsius(T):
    return (float(5)/9)*(T - 32)


temp = (36.5, 37, 37.5, 39)
F = list(map(fahrenheit, temp))
C = list(map(celsius, F))

print(F)
print(C)

email = ['the', 'this', 'annoy', 'the', 'the', 'annoy']


def in_email(x):
    if x == "the":
        return 1
    else:
        return 0


spamCheck = map(in_email, email)

print("Sum :", reduce(lambda x, y: x + y, spamCheck))

numbers = [9, 41, 12, 3, 74, 15]
avg = reduce(lambda x, y: x + y, numbers)/len(numbers)
print("Average:", avg)
print("Average: %.2f" % avg)
print("Average: {0:.2f}".format(avg))


