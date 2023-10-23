# Zkus svoji první funkci upravit tak, že si bude umět poradit s mezerami v telefonním čísle. Mezer se zbavíš například tak, že použiješ metodu .replace(). První parametr metody replace je znak, který chceš nahradit, a druhý parametr nový znak. Pokud se chceš nějakého znaku zbavit, "nahraď" ho prázdným řetězcem "".


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