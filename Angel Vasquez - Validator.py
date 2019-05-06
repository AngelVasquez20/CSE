test_num = "4556737586899855"
print(test_num)


def remove_num(string):
    return string[:15]


def reverse_it(string):
    return string[::-1]


print(reverse_it(remove_num(test_num)))


def validate(num: str):
    for index in range(len(num)):
        int_version = int(num[index])
        print(validate(test_num))
    cut_nums = remove_num(test_num[:15])
    # print(cut_nums)
    reversed_nums = reverse_it(cut_nums)
    # print(reversed_nums)
    list_nums = list(reversed_nums)
    print(list_nums)
    for index in range(len(list_nums)):
        list_nums[index] = int(list_nums[index])
        print(list_nums)


print(validate(test_num))