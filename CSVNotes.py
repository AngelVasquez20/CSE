import csv


def validate(num: str):
    if divisible_by_2(num) and divisible_by_three(num):
        return True
    return False


def divisible_by_three(num: str):
    first_num = int(num[0])  # this is the first number
    if first_num % 3 == 0:
        return True
    return False


def divisible_by_2(num: str):
    first_num = int(num[0])  # this is the first number
    if first_num % 2 == 0:
        return True
    return False


def is_first_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 1:
        return True
    return False

def is_second_num_odd(num: str):
    first_num = int(num[0])
    if first_num % 2 == 0:
        return True
    return False


 with open("Book1.csv", 'r') as old_csv:
    with open("MyFile.csv", 'w', newline='') as new_csv:

 with open("Book1.csv", 'r') as old_csv:
    with open("MyFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")
        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0] # this is a string
            if first_num == 4: # this is the first number
                writer.writerow(row)
            # print (int(old_number) + 1
            # print(old_number)
        print("OK")


with open("Book1.csv", 'r') as old_csv:
    with open("MyFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            # old_number = int(row[0]) + 1
            old_number = row[0]  # this is a string
            if validate(old_number):
                writer.writerow(row)
            # print (int(old_number) + 1
            # print(old_number)
    print("OK")
