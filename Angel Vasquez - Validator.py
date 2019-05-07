test_num = "4556737586899855"
print(test_num)


def remove_num(string):
    return string[:15]


def reverse_it(string):
    return string[::-1]


def validate(num: str):
    cut_nums = remove_num(test_num[:15])
    reversed_nums = reverse_it(cut_nums)
    list_nums = list(reversed_nums)
    print(list_nums)
    for index in range(len(list_nums)):
        list_nums[index] = int(list_nums[index])
        print(list_nums[index])


def multiply_even_num(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9


print(validate(test_num))
