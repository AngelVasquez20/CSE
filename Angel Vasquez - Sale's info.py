import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    fruits_total = 0
    clothes_total = 0
    meat_total = 0
    beverages_total = 0
    office_supplies_total = 0
    cosmetics_total = 0
    snacks_total = 0
    personal_care_total = 0
    household_total = 0
    vegetables_total = 0
    baby_food_total = 0
    cereal_total = 0
    reader = csv.reader(csv_file_thing)
    for row in reader:
        profit = row[13]
        items = row[2]
        if items == "Fruits":
            fruits_total += float(profit)
        if items == "Clothes":
            clothes_total += float(profit)
        if items == "Meat":
            meat_total += float(profit)
        if items == "Beverages":
            beverages_total += float(profit)
        if items == "Office Supplies":
            office_supplies_total += float(profit)
        if items == "Cosmetics":
            cosmetics_total += float(profit)
        if items == "Snacks":
            snacks_total += float(profit)
        if items == "Personal Care":
            personal_care_total += float(profit)
        if items == "Household":
            household_total += float(profit)
        if items == "Vegetables":
            vegetables_total += float(profit)
        if items == "Baby Food":
            baby_food_total += float(profit)
        if items == "Cereal":
            cereal_total += float(profit)

print("Fruits total profit = ", fruits_total)
print("Clothes total profit = ", clothes_total)
print("Meat total profit = ", meat_total)
print("Beverages total profit = ", beverages_total)
print("Office Supplies total profit = ", office_supplies_total)
print("Cosmetics total profit = ", cosmetics_total)
print("Snacks total profit = ", snacks_total)
print("Personal care total profit = ", personal_care_total)
print("Household total profit = ", household_total)
print("Vegetables total profit = ", vegetables_total)
print("Baby food total profit = ", baby_food_total)
print("Cereal total profit = ", cereal_total)

print()

list_total = [fruits_total, clothes_total, meat_total, baby_food_total, office_supplies_total, cosmetics_total,
              snacks_total, personal_care_total, household_total, vegetables_total, baby_food_total,cereal_total]

list_type = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal",
             "Household", "Vegetables", "Baby food", "Cereal"]

index = list_total.index(max(list_total))
print("Most profit = %s" % list_type[index])

