test_num = "4712839550684070"
print(test_num)


def remove_num(string):
    return string[:15]


remove_num(test_num[:15])

print(remove_num(test_num))


def reverse_it(string):
    return string[::-1]


print(reverse_it(remove_num(test_num)))


def validate(num: str):
    for index in range(len(num)):
        int_version = int(num[index])
        print(validate(test_num))
