import json

with open("lekce_3.json", mode="r", encoding="utf-8") as soubor:
  pizzy = json.load(soubor)

print(pizzy)
