# ------------------------------- TASK 01 -----------------------------------
# Načti od uživatele matematický operátor a 2 čísla a vypiš výsledek výpočtu.
# Program bude podporovat operátory +, -, / a *.
'''
Zadej operátor: +
Zadej první číslo: 3
Zadej druhé číslo: 9
Výsledek příkladu 3 + 9 je 12.
'''
#operator = input("Zadej operator:")

#cislo1 = int(input("Zadej 1. cislo:"))

# cislo2 = int(input("Zadej 2. cislo:"))

# if operator == "+":
#   result = cislo1+cislo2
#   print("Vysledek prikladu je:", "" + str(result))

# elif operator == "-":
#   result = cislo1-cislo2
#   print("Vysledek prikladu je:", " " + str(result))

# elif operator == "*":
#   result = cislo1*cislo2
#   print("Vysledek prikladu je:", " " + str(result))

# elif operator == "/":
#   result = cislo1/cislo2
#   print("Vysledek prikladu je:", " " + str(result))

# else:
#   print("Zadali jste neplatne zadani.")

# ------------------------------- TASK 02 -----------------------------------
# Proměnná medal_table tentokrát obsahuje zisky jednotlivých druhů medailí států
# na olympiádě 2020.
# Vypiš název státu, který získal nejvíc bronzových medailí.

# medal_table = {
#           "Cuba": { "gold": 7, "silver": 3, "bronze": 5 },
#           "Spain": { "gold": 3, "silver": 8, "bronze": 6 },
#           "Uganda": { "gold": 2, "silver": 1, "bronze": 1 },
#           "Bahamas": { "gold": 2, "silver": 0, "bronze": 0 },
#           "Ukraine": { "gold": 1, "silver": 6, "bronze": 12 },
#           "San Marino": { "gold": 0, "silver": 1, "bronze": 2 },
#       }

# most_bronze_country = ()
# most_bronze_count = 0

# for key, value in medal_table.items():
#   if value["bronze"] > most_bronze_count:
#     most_bronze_count = value["bronze"]
#     most_bronze_country = key

# print("Nejvic bronzovych mediali ziskala: " + most_bronze_country)









# ------------------------------- TASK 03 -----------------------------------
# V seznamu people máme seznam lidí s jejich daty narození. Vypište jména lidí,
# kteří se narodili v sudý rok.
# people = [
#     ["Jeong-Hui Mun", "09/12/1984"],
#     ["Cezário Torres", "31/08/1993"],
#     ["Josefina Löwe", "03/11/1982"],
#     ["Gavrilo Milojević", "28/03/2002"],
#     ["Liidia Tamm", "10/07/1963"],
#     ["Matxin Zubizarreta", "19/02/1956"],
#     ["Mykhail Klymenko", "01/10/1988"],
#     ["Bibek Joshi", "05/03/2007"],
#     ["Jan Vlk", "26/09/1995"],
#     ["Xuân Hoàng", "29/08/1974"]
# ]

# suda = [0, 2, 4, 6, 8]

# for value in people:
#   if int(value[1][9:]) in suda:
#     print(value[0])


# ------------------------------- TASK 04 -----------------------------------
# Načti od uživatele celé číslo, zjisti, zda je dělitelné 8 a informuj
# o tom uživatele.
celecislo = int(input("zadej cislo:"))


if celecislo % 8 == 0:
  print("Zadane cislo je delitelne 8.")
else:
  print("Zadane cislo neni delitelne 8.")
