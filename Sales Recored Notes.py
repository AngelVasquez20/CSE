TotalRevenue = row[11]
UnitCost = row[10]
TotalCost = row[12]
UnitPrice = row[9]
UnitSold = row[8]
Meat = row[2]


index = list_total.index(max(list_total))
print("Most profit = %s" % list_type[index])