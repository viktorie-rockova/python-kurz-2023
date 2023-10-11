# Ukol 2.1
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kod_soucastky_zakaznik = input("Zadej kod soucastky:")

if (kod_soucastky_zakaznik) in sklad:
  pocet_kusu_zakaznik = int(input("Zadej pocet kusu:"))
  if sklad[kod_soucastky_zakaznik] < pocet_kusu_zakaznik:
    print(f"Nemame dostatecny pocet kusu na sklade. Lze prodat pouze {sklad [kod_soucastky_zakaznik]}.")
    sklad.pop(kod_soucastky_zakaznik)
    print(f"Stav skladu je: {sklad}")
  else:
    print("Mame na sklade dostatek kusu.")
    sklad[kod_soucastky_zakaznik] -= pocet_kusu_zakaznik
    print(f"Stav skladu je: {sklad}")
else:
  print("Polozka neni na sklade.")
  print(f"Stav skladu je: {sklad}")