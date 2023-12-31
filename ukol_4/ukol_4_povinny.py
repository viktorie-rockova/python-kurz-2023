# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Tipy:

# Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili.
# Pro kontrolu předvolby použijte slicing (viz první lekce) pro získání prvních 4 znaků řetězce. Ty porovnejte s řetězcem "+420".

def overeni_formatu(telefonni_cislo):
  telefonni_cislo = telefonni_cislo.replace(" ", "")
  if len(telefonni_cislo) == 9 or (len(telefonni_cislo) == 13 and telefonni_cislo[:4] == "+420"):
    return True
  else:
    return False

def cena_zpravy(zprava):
  pocet_zapocatych_180_znaku = (len(zprava) // 180) + 1
  cena = pocet_zapocatych_180_znaku * 3
  return cena

while True:
  telefonni_cislo = input("Zadejte telefonni cislo prijemce: ")

  if overeni_formatu(telefonni_cislo):
    zprava = input("Zadejte zpravu k odeslani: ")
    print(f"Cena odeslani bude {cena_zpravy(zprava)}.")
    break
  else:
    print(f"Zadali jste neplatny format telefonniho cisla. Zadejte telefonni cislo ve formatu +420 XXX XXX XXX nebo XXX XXX XXX.")