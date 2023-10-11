# ------------------------------UKOL 1------------------------------
# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.


# def mult(cislo1, cislo2):
#   return cislo1 * cislo2

# print(mult(2, 6))


# ------------------------------UKOL 2------------------------------
# Převod kilometrů na míle a zpět
# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.

# def kilometry_na_mile(kilometry):
#   return kilometry * 0.621371

# def mily_na_kilometry(mile):
#   return mile * 1.6

# Převod metrů na stopy a zpět
# Napište funkce: metry_na_stopy(metry) a stopy_na_metry(stopy), které umožňují převod mezi metry a stopami.

# def metry_na_stopy(metry):
#   return metry * 3.28084

# def stopy_na_metry(stopy):
#   return stopy * 0.3048

# Převod centimetrů na palce a zpět
# Vytvořte dvě funkce: centimetry_na_palec(centimetry) a palce_na_centimetry(palce), které umožní převod mezi centimetry a palci.

# def centimetry_na_palec(centimetry):
#   return centimetry * 0.3937

# def palce_na_centimetry(palce):
#   return palce * 2.54

# Převod hmotnosti kilogramů na libry a zpět
# Napište funkce: kilogramy_na_libry(kilogramy) a libry_na_kilogramy(libry), které provedou převod mezi kilogramy a librami.

# def kilogramy_na_libry(kilogramy):
#   return kilogramy * 2.2

# def libry_na_kilogramy(libry):
#   return libry * 0.45359237

# Převod objemu litrů na galony a zpět
# Vytvořte dvě funkce: litry_na_galony(litry) a galony_na_litry(galony), které umožní převod mezi litry a galony.

# def litry_na_galony(litry):
#   return litry * 0.264172

# def galony_na_litry(galony):
#   return galony * 3.78541

# Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět
# Napište funkce: kmh_na_mph(kmh) a mph_na_kmh(mph), které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu.

# def kmh_na_mph(kmh):
#   return kmh * 0.621371192

# def mph_na_kmh(mph):
#   return mph * 1.60934

# Převod teploty ze stupňů Celsia na Fahrenheit a zpět
# Vytvořte dvě funkce: celsia_na_fahrenheit(teplota) a fahrenheit_na_celsia(teplota), které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.

# def celsia_na_fahrenheit(teplota_c):
#   return (teplota_c * 1.8) + 32

# def fahrenheit_na_celsia(teplota_f):
#   return (teplota_f - 32) / 1.8

#  ------------------------------UKOL 3------------------------------
# Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.
#
#  Zadej slovo: ahoj
# ********
# * ahoj *
# ********
# Nápověda: 8 * '*' == '********'

# Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

# Lukas comments:
# a co ti na tvém řešení nehraje? akorát bych tam zauvažoval jak ta funkce vezme parametr než aby řešila input.. ?
# a navíc to má být rámeček okolo celého slova, ještě dám hint, zkus si napsat slovo: nejkulataoulinkatejsikulicka

def ramecek(slovo):
  print("********\n* " + slovo + " *\n********")

ramecek(input("Zadej slovo: "))

#  ------------------------------UKOL 4------------------------------
# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup.
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.