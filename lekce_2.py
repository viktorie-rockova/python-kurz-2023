jmena = ['Martin', 'Michal', 'Milada', 'Jana']

print(jmena[2])
print(jmena[3])

knihy = ['Temna noc', 450, True, True]
knihy2 = {
  'Nazev': 'ananas na pizzu patri',
  'Cena': 0,
  'Skladem': True,
  'Autor': 'jan malinsky'
}

print(knihy2)

#vyhodi seznam klicu
print(knihy2.keys())

# vyhodi 
print(knihy2.values())

print(knihy2['Nazev'])

print(f"Kniha: {knihy2['Nazev']}, cena: {knihy2['Cena']}, skladem: {knihy2['Skladem']}, autor: {knihy2['Autor']}")

# cviceni 1> vysvedceni
vysvedceni = {
  "anglicky jazyk": 1,
  "matematika": 2,
  "dejepis": 1
}
print(vysvedceni)

# cviceni 2: detektivky
sales = {
  "Zkus mě chytit": 4165,
  "Vrah zavolá v deset": 5681,
  "Zločinný steh": 2565,
}

sales['Noc, ktera me zabila'] = 0

sales["Vrah zavolá v deset"] += 100

print(sales)

# cviceni 3: tombola
tombola = {
  7: "Láhev kvalitního vína Château Headache",
  15: "Pytel brambor z místního družstva",
  23: "Čokoládový dort",
  47: "Kniha o historii města",
  55: "Šiška salámu",
  67: "Vyhlídkový let balónem",
  79: "Moderní televizor",
  91: "Roční předplatné městského zpravodaje",
  93: "Společenská hra Sázky a dostihy",
}

cislo_listku = int(input('Zadej cislo listku:'))

if (cislo_listku) in tombola:
  vyhra = tombola[cislo_listku]
else:
  vyhra = 'Bohuzel nic nevyhravas.'

print(f'Vyhrál jsi: {vyhra}')

# vynda polozku se seznamu
# tombola.pop(cislo_listku)
# tombola.pop(15)

print(tombola)

# bonusovy ukol: paranoidni vecirek
# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."
# chybí dořešit indi heslo na řádku 84
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

jmeno = input('Jak se jmenujes, chlape?')

if (jmeno) in passwords:
  heslo = input('Rekni heslo!')
  if (heslo) in passwords.values():
    print('Smis vstoupit.')
else:
  print('Smula, hochu.')

