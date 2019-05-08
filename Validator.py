test_num = "4556737586899855"
print(test_num)


def reverse_it(all_digits: list):
    all_digits = all_digits[::1]
    return all_digits


def multiply_even_num(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2
            if num[index] > 9:
                num[index] -= 9


def mod_10(total_sum, last_digit):
    if int(total_sum) % 10 == int(last_digit):
        return True
    else:
        return False


def validate(num: str):
    all_digits = list(num)
    if len(num) is not 16:
        return False
    last_digits = all_digits[test_num:15]
    all_digits.pop(15)
    all_digits = reverse_it(all_digits)
    multiply_even_num(all_digits)
    total_sum = sum(all_digits)
    return mod_10(total_sum, last_digits)


print(validate(reverse_it(mod_10(multiply_even_num()))))



