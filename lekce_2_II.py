seznam = [100, 200, 300, 400]
soucet = 0

for polozka in seznam:
  soucet += polozka

print(soucet)

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

print(sales["Zkus mě chytit"])

for klic in sales:
    print(klic)
    print(sales[klic])

for klic, hodnota in sales.items():
    print(f"nazev: {klic}, pocet prodanych kusu: {hodnota}")

for value in sales.values():
    print(value)