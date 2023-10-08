import json

with open("bonusy.json", mode="r", encoding="utf-8") as soubor:
  bonusy = json.load(soubor)

with open("body.json", mode="r", encoding="utf-8") as soubor:
  body = json.load(soubor)

znamky = {}

for key, value in body.items():
  bodycelkem = value
  for name, bonus in bonusy.items():
    if name == key:
      bodycelkem = value + bonus

  if bodycelkem <= 29:
    znamka = "5"
  elif bodycelkem >= 30 and bodycelkem <= 49:
    znamka = "4"
  elif bodycelkem >= 50 and bodycelkem <= 69:
    znamka = "3"
  elif bodycelkem >= 70 and bodycelkem <= 89:
    znamka = "2"
  else:
    znamka = "1"

  znamky[key] = znamka

print(znamky)

with open('znamky.json', mode='w', encoding='utf-8') as file:
    json.dump(znamky, file)