
def overeni_formatu(telefonni_cislo: str) -> str:
  telefonni_cislo = telefonni_cislo.replace(" ", "")
  if len(telefonni_cislo) == 9 or (len(telefonni_cislo) == 13 and telefonni_cislo[:3] == "+42"):
    return True
  else:
    return False

def cena_zpravy(zprava: str) -> int:
  pocet_zapocatych_180_znaku = (len(zprava) // 180) + 1
  cena = pocet_zapocatych_180_znaku * 3
  return cena

telefonni_cislo = input("Zadejte telefonni cislo prijemce: ")
if overeni_formatu(telefonni_cislo):
  zprava = input("Zadejte zpravu k odeslani: ")
  print(f"Cena odeslani bude {cena_zpravy(zprava)}.")
else:
  print(f"Zadali jste neplatny format telefonniho cisla.")