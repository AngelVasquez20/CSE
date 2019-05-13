import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    fruits_total = 0
    reader = csv.reader(csv_file_thing)
    for row in reader:
        profit = row[13]
        items = row[2]
        if items == "Fruits":
            fruits_total += float(profit)

print("fruits = ", fruits_total)
