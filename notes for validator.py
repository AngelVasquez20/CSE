
print(5 + 3)
print(5 - 3)
print(4 * 5)
print(6 / 5)
print()


def multiply_even_num(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9

