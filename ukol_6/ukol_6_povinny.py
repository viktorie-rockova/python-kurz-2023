# Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

# Registrační značka	Značka a typ vozidla	Počet najetých kilometrů
# 4A2 3020	Peugeot 403 Cabrio	47534
# 1P3 4747	Škoda Octavia	41253
# Vytvoř třídu Auto, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

# - registrační značka automobilu registracni_znacka,
# - značka a typ vozidla typ_vozidla,
# - počet najetých kilometrů najete_km,
# - informaci o tom, jestli je vozidlo aktuálně volné dostupne (pravdivostní hodnota -- True pokud je volné a False pokud je
# vypůjčené).
# - Vytvoř metodu __init__() pro třídu Auto. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry
# funkce __init__ a ulož je jako atributy objektu. Poslední atribut rovnou nastav jako True, tj. na začátku je vozidlo vždy
# volné.

# Vytvoř objekty, které reprezentují oba automobily půjčovny.

# Třídě Auto přidej metodu pujc_auto(), která nebude mít (kromě obligátního self) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu dostupne, který určuje, zda je vozidlo půjčené, a vrátí text "Potvrzuji zapůjčení vozidla". Pokud je vozidlo již půjčené, vrátí text "Vozidlo není k dispozici".

# Dále tříde Auto přidej funkci get_info(), která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

# Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit.
# Uživatel může zadávat hodnoty Peugeot nebo Škoda. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí
# funkce get_info() a následně použij funkci pujc_auto().

# Otestuj, že program nedovolí půjčit stejné auto dvakrát.

class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, pocet_najetych_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.pocet_najetych_km = pocet_najetych_km
        self.dostupnost = True

    def pujceni_auta(self):
        if self.dostupnost:
            self.dostupnost = False
            return "Potvrzuji úspešnou zápujčku vozidla."
        else:
            return "Vozidlo bohužel není k dispozici."  

    def get_info(self):
        return f"Auto typu {self.typ_vozidla} má registrační značku {self.registracni_znacka}."    

auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

pokracuj = True

while  pokracuj:
    vyber_auta = input("Zadejte značku vozidla (Peugeot nebo Škoda) pro výběr vozu nebo ukončete program zadáním 'Konec': ")

    if vyber_auta.lower() == "konec":
        print("Ukončili jste program.")
        pokracuj = False
    
    elif vyber_auta.lower() == "peugeot":
        print(auto1.get_info())
        print(auto1.pujceni_auta())

    elif vyber_auta.lower() == "škoda":
        print(auto2.get_info())
        print(auto2.pujceni_auta())

    else:
        print("Neplatná volba značky vozidla.")