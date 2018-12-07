# Challenge number 1


def challenge1(firstname, lastname):
    print(lastname, firstname)


challenge1("Angel", "Vasquez")


# Challenge number 4


def challenge4(number):
    if number < 0:
        return "Negative"
    if number == 0:
        return "Zero"
    if number > 0:
        return "positive"


print(challenge4(6))


# Challenge number 3


def challenge3(b, h):
    return 5 * b * h


print(challenge3(3, 6))


# Challenge number 5


def challenge5(radius):

    return 3.14 * radius ** 2


print(challenge5(6))


# Challenge number 6

def challenge6(radius):
    return 4/3 * 3.14 * radius ** 3


print(challenge6(7))
