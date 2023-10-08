import json

with open("znamky.json", mode="r", encoding="utf-8") as soubor:
  znamky = json.load(soubor)

prospech = {}

for key, value in znamky.items():
  mark = "Fail"
  if value >= 60:
    mark = "Pass"
  prospech[key] = mark

print(prospech)

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(prospech, file)