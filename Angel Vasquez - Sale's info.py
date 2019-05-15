import csv

with open("Sales Records.csv", "r") as csv_file_thing:
    # Region
    asia_total_profit = 0
    australia_and_Oceania_profit = 0
    central_America_and_the_Caribbean_profit = 0
    europe_profit = 0
    middle_east_and_north_africa_profit = 0
    north_america_profit = 0
    sub_saharan_africa_profit = 0
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
    for row in reader:
        profit = row[13]
        items = row[2]
        region = row[0]
        # Items
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
        # Region
        if region == "Asia":
            asia_total_profit += float(profit)
        if region == "Australia and Oceania":
            australia_and_Oceania_profit += float(profit)
        if region == "Central America and the Caribbean":
            central_America_and_the_Caribbean_profit += float(profit)
        if region == "Europe":
            europe_profit += float(profit)
        if region == "Middle East and North Africa":
            middle_east_and_north_africa_profit += float(profit)
        if region == "North America":
            north_america_profit += float(profit)
        if region == "Sub-Saharan Africa":
            sub_saharan_africa_profit += float(profit)


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
print("Most profit = %s" % list_type[index])

print()

region_total = [asia_total_profit, australia_and_Oceania_profit, central_America_and_the_Caribbean_profit,
                europe_profit, middle_east_and_north_africa_profit, north_america_profit, sub_saharan_africa_profit]


region_type = ["Asia", "Australia and Oceania", "Central America and the Caribbean", "Europe",
               "Middle East and North Africa", "North America", "Sub-Saharan Africa"]

region_index = region_total.index(max(region_total))
print("The region with the most profit = %s" % region_type[index])
