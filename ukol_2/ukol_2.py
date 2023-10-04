# Ukol 2.1
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

kodsoucastkyzakaznik = input("Zadej kod soucastky:")

pocetkusuzakaznik = int(input("Zadej pocet kusu:"))

if (kodsoucastkyzakaznik) in sklad:
  if sklad[kodsoucastkyzakaznik] < pocetkusuzakaznik:
    print(f"Nemame dostatecny pocet kusu na sklade. Lze prodat pouze {sklad [kodsoucastkyzakaznik]}.")
    sklad.pop(kodsoucastkyzakaznik)
  else:
    print("Mame na sklade dostatek kusu.")
    sklad[kodsoucastkyzakaznik] -= pocetkusuzakaznik
else:
  print("Polozka neni na sklade.")

print(sklad)
