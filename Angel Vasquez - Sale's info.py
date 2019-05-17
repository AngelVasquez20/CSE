import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    # Region
    asia_total = 0
    australia_and_Oceania_total = 0
    central_America_and_the_Caribbean_total = 0
    europe_total = 0
    middle_east_and_north_africa_total = 0
    north_america_total = 0
    sub_saharan_africa_total = 0
    # Items
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
    # Units
    fruits_units_total = 0
    clothes_units_total = 0
    meat_units_total = 0
    beverages_units_total = 0
    office_supplies_units_total = 0
    cosmetics_units_total = 0
    snacks_units_total = 0
    personal_care_units_total = 0
    household_units_total = 0
    vegetables_units_total = 0
    baby_food_units_total = 0
    cereal_units_total = 0
    for row in reader:
        profit = row[13]
        items = row[2]
        region = row[0]
        units_sold = row[8]
        # Items
        if items == "Fruits":
            fruits_total += float(profit)
            fruits_units_total += int(units_sold)
        if items == "Clothes":
            clothes_total += float(profit)
            clothes_units_total += int(units_sold)
        if items == "Meat":
            meat_total += float(profit)
            meat_units_total += int(units_sold)
        if items == "Beverages":
            beverages_total += float(profit)
            beverages_units_total += int(units_sold)
        if items == "Office Supplies":
            office_supplies_total += float(profit)
            office_supplies_units_total += int(units_sold)
        if items == "Cosmetics":
            cosmetics_total += float(profit)
            cosmetics_units_total += int(units_sold)
        if items == "Snacks":
            snacks_total += float(profit)
            snacks_units_total += int(units_sold)
        if items == "Personal Care":
            personal_care_total += float(profit)
            personal_care_units_total += int(units_sold)
        if items == "Household":
            household_total += float(profit)
            household_units_total += int(units_sold)
        if items == "Vegetables":
            vegetables_total += float(profit)
            vegetables_units_total += int(units_sold)
        if items == "Baby Food":
            baby_food_total += float(profit)
            baby_food_units_total += int(units_sold)
        if items == "Cereal":
            cereal_total += float(profit)
            cereal_units_total += int(units_sold)
        # Region
        if region == "Asia":
            asia_total += float(profit)
        if region == "Australia and Oceania":
            australia_and_Oceania_total += float(profit)
        if region == "Central America and the Caribbean":
            central_America_and_the_Caribbean_total += float(profit)
        if region == "Europe":
            europe_total += float(profit)
        if region == "Middle East and North Africa":
            middle_east_and_north_africa_total += float(profit)
        if region == "North America":
            north_america_total += float(profit)
        if region == "Sub-Saharan Africa":
            sub_saharan_africa_total += float(profit)

fruits_units_average = fruits_total / fruits_units_total
clothes_units_average = clothes_total / clothes_units_total
meat_units_average = meat_total / meat_units_total
beverages_units_average = beverages_total / beverages_units_total
office_supplies_units_average = office_supplies_total / office_supplies_units_total
cosmetics_units_average = cosmetics_total / cosmetics_units_total
snacks_units_average = snacks_total / snacks_units_total
personal_care_units_average = personal_care_total / personal_care_units_total
household_units_average = household_total / household_units_total
vegetables_units_average = vegetables_total / vegetables_units_total
baby_food_units_average = baby_food_total / baby_food_units_total
cereal_units_average = cereal_total / cereal_units_total


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
              snacks_total, personal_care_total, household_total, vegetables_total, baby_food_total, cereal_total]

list_type = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal",
             "Household", "Vegetables", "Baby food", "Cereal"]

index = list_total.index(max(list_total))
print("Item with the highest profit = %s" % list_type[index])

print()

region_total = [asia_total, australia_and_Oceania_total, central_America_and_the_Caribbean_total,
                europe_total, middle_east_and_north_africa_total, north_america_total, sub_saharan_africa_total]


region_type = ["Asia", "Australia and Oceania", "Central America and the Caribbean", "Europe",
               "Middle East and North Africa", "North America", "Sub-Saharan Africa"]

print("Total profit for Asia = ", asia_total)
print("Total profit for Australia and Ocean = ", australia_and_Oceania_total)
print("Total profit for Central America and the Caribbean = ", central_America_and_the_Caribbean_total)
print("Total profit for Europe = ", europe_total)
print("Total profit for Middle East and North Africa = ", middle_east_and_north_africa_total)
print("Total profit for North America = ", north_america_total)
print("Total profit for Sub-Saharan Africa = ", sub_saharan_africa_total)

print()

region_index = region_total.index(max(region_total))
print("The region with the highest profit = %s" % region_type[region_index])

print()

print("The units sold for fruits = ", fruits_units_average)
print("The units sold for clothes = ", clothes_units_average)
print("The units sold for meat = ", meat_units_average)
print("The units sold for beverages = ", beverages_units_average)
print("The units sold for office supplies = ", office_supplies_units_average)
print("The units sold for baby food = ", baby_food_units_average)
print("The units sold for cosmetics = ", cosmetics_units_average)
print("The units sold for snacks = ", snacks_units_average)
print("The units sold for personal care = ", personal_care_units_average)
print("The units sold for household = ", household_units_average)
print("The units sold for vegetables = ", vegetables_units_average)
print("The units sold for cereal = ", cereal_units_average)

units_average = [fruits_units_average, clothes_units_average, meat_units_average, baby_food_units_average,
                 office_supplies_units_average, cosmetics_units_average,
                 snacks_units_average, personal_care_units_average, household_units_average, vegetables_units_average,
                 baby_food_units_average, cereal_units_average]

units_type = ["Fruits", "Clothes", "Meat", "Beverages", "Office Supplies", "Cosmetics", "Snacks", "Personal",
              "Household", "Vegetables", "Baby food", "Cereal"]

print()

units_index = units_average.index(max(units_average))
print("The Item with the most units sold = %s" % units_type[units_index])
